import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Button('Click Here',id='button-1'),
    html.Div(id='div-1')
])
@app.callback(
    Output('div-1', 'children'),
    Input('button-1', 'n_clicks')

)
def update_output(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return f"Bardzo cenna informacja: kliknąłeś {n_clicks} razy."



if __name__ == '__main__':
    app.run_server(debug=True, port=8076)
