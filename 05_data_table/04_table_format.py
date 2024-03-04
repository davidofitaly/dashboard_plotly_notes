import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from dash import dash_table
from dash.dash_table.Format import Format
import pandas as pd
from collections import OrderedDict

df = pd.DataFrame(OrderedDict([
    ('country',['Poland', 'USA', 'Germany']),
    ('gdp', [100, 200, 150]),
    ('change', [0.07, 0.05, 0.04])
]))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dash_table.DataTable(
        columns = [
            {'name': 'country', 'id': 'country', 'type': 'text'},
            {'name': 'GDP $', 'id': 'gdp', 'type': 'numeric', 'format': Format(symbol='$')},
            {'name': ' Change %', 'id': 'change', 'type': 'numeric'},
        ],
        data = df.to_dict('records')

    )

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8087)
