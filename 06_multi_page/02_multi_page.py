import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')


])

index_page = html.Div([

    html.H3('Menu'),
    dcc.Link('Choose language of programming', href='/technology'),
    html.Br(),
    dcc.Link('State your experience',href='/experience')
])

tech_layout = html.Div([

    html.H4('Choose language of programming from the following'),
    dcc.Dropdown(
        id='tech-1-dropdown',
        options = [{'label': i, 'value':i} for i in ['Python', 'SQL', 'Java']],
    ),
    html.Div(id='tech-1-div'),
    html.Br(),
    dcc.Link('Return to menu', href='/'),
    html.Br(),
    dcc.Link('State your experience', href='/experience')


])

experience_layout = html.Div([

    html.H4('State your experience'),
    dcc.RadioItems(
        id='experience-1-radios',
        options = [{'label': i, 'value': i} for i in ['below 1 year', 'since 1 to 3', 'over 3 years']],
    ),
    html.Div(id='experience-1-div'),
    html.Br(),
    dcc.Link('Return to menu', href='/'),
    html.Br(),
    dcc.Link('Choose language of programming from the following', href='/technology')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/technology':
        return tech_layout
    elif pathname == '/experience':
        return experience_layout
    else:
        return index_page

@app.callback(
    Output('tech-1-div', 'children'),
    [Input('tech-1-dropdown','value')]
)
def tech_1_dropdown(value):
    return f'You choosed {value}'


@app.callback(
    Output('experience-1-div', 'children'),
    [Input('experience-1-radios','value')]
)
def experience_1_radios(value):
    return f'You choosed {value}'


if __name__ == '__main__':
    app.run_server(debug=True, port=8091)
