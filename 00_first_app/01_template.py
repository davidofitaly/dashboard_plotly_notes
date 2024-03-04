import dash
from dash import dcc, html
import plotly.graph_objects as go

app = dash.Dash(__name__)

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)