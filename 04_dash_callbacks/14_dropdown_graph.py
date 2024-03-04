import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Dropdown(
        id='drop-1',
        options=[
            {'label': 'Polska', 'value': 'PL'},
            {'label': 'Niemcy', 'value': 'GER'}
        ],
        value='PL'
    ),

    dcc.Graph(
        id='graph-1'
    )

])


@app.callback(
    Output('graph-1', 'figure'),
    [Input('drop-1', 'value')]
)
def update_graph(value):
    data_dict={
        'PL': [3,2,5,1,8,7],
        'GER': [9,3,6,1,2,7,2,0]
    }
    return {'data': [
        {'y': data_dict[value],
         'type':'scatter',
         'fill':'tozeroy'}
    ]}




if __name__ == '__main__':
    app.run_server(debug=True, port=8082)
