import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import time

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H3('Wprowadź tekst...'),
    dcc.Input(
        id='input-1',
        value='',
        placeholder='Wprowadź tekst...',
    ),
    dcc.Loading(
        id='loading-1',
        children=[
            html.Div(id='loading-div-1')
        ],
        type='default'
    ),

    dcc.Input(
        id='input-2',
        value='',
        placeholder='Wprowadź tekst...',
    ),
    dcc.Loading(
        id='loading-2',
        children=[
            html.Div(id='loading-div-2')
        ],
        type='circle'
    ),
])

@app.callback(
    Output('loading-div-1','children'),
    [Input('input-1', 'value')]
)
def input_trigger_1(value):
    time.sleep(1)
    print(value)

@app.callback(
    Output('loading-div-2','children'),
    [Input('input-2', 'value')]
)
def input_trigger_2(value):
    time.sleep(1)
    print(value)



if __name__ == '__main__':
    app.run_server(debug=True, port=8083)
