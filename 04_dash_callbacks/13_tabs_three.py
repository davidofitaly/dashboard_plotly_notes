import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H2('Dash Tab Template'),
    dcc.Tabs(
        id='tabs-1',
        children=[
            dcc.Tab(label='Bar Plot', value='tab-1'),
            dcc.Tab(label='Line Plot', value='tab-2'),
            dcc.Tab(label='Scatter Plot', value='tab-3'),
        ],
        value='tab-1'
    ),
    html.Div(id='div-1')
])
@app.callback(
    Output('div-1', 'children'),
    [Input('tabs-1', 'value')]
)
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Bar Plot Content'),
            dcc.Graph(
                figure= {
                    'data':[{'x': [1,3,4],
                             'y':[2,1,3],
                             'type': 'bar'
                             }]
                }
            )
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Line Content'),
            dcc.Graph(
                figure= {
                    'data':[{'x': [1,3,4,5,8],
                             'y':[2,1,3,4,1],
                             'type': 'line'
                             }]
                }
            )
        ])
    elif tab == 'tab-3':

        return html.Div([
            html.H3('Scatter Content'),
            dcc.Graph(
                figure= {
                    'data':[{'x': [1,3,4,5,8],
                             'y':[2,1,3,4,1],
                             'mode': 'markers'
                             }]
                }
            )
        ])

if __name__ == '__main__':
    app.run_server(debug=True, port=8081)
