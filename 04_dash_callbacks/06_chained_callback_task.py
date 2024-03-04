import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'Polska': ['Warszawa', 'Kraków', 'Wrocław'],
    'Stany Zjednoczone': ['New York', 'Los Angeles']
}

app.layout = html.Div([

    dcc.RadioItems(
        id='radio-1',
        options=[{'label': key, 'value': key} for key in all_options.keys()],
        value='Polska'
    ),
     html.Hr(),

    dcc.RadioItems(
        id='radio-2',
        value= 'Warszawa'
    ),

    html.Hr(),

    html.Div(id='div-1')
])

@app.callback(
    Output(component_id='radio-2',component_property='options'),
    [Input(component_id='radio-1', component_property='value')]
)
def  set_otpions(selected_value):
    return [{'label': i, 'value': i} for i in all_options[selected_value]]

@app.callback(
    Output('div-1', 'children'),
    [Input('radio-1', 'value'),Input('radio-2', 'value')]

)
def update_div(selected1, selected2):
    return f'Wybrałeś {selected1} oraz {selected2}'

if __name__ == '__main__':
    app.run_server(debug=True, port=8075)
