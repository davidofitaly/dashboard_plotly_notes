import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import base64

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
],
style={
    'background-color':'#caf0f8',
    'height': '1000px'
})

### index_page ###
index_page = html.Div([
    html.H3('MENU:'),

    html.Div([
        html.Hr(),
        dcc.Link('Choose language of programming', href='/technology'),
        html.Br(),
        dcc.Link('Display logo', href='/logo'),
        html.Hr(),
    ],style={'background-color': 'white'}),
    html.H6('You benefit from the application during the development.')
],
style={
    'text-align': 'center',
    'font-size': '28px',
    'color': '#393b3a'

})

### tech_layout ###
tab_style = {
    'background-color':'#0077b6'
}

selected_style = {
    'background-color':'#000814',
    'borderTop': '5px solid #f72585',
    'color': 'white'
}


tech_layout = html.Div([
    html.Div([
        html.H4('Choose logo from the following'),
        html.Hr(),
        dcc.Tabs(
            id='tech-1-tabs',
            children=[
                dcc.Tab(label='Python', value='tab-1', style=tab_style, selected_style=selected_style),
                dcc.Tab(label='SQL', value='tab-2', style=tab_style, selected_style=selected_style),
                dcc.Tab(label='Java', value='tab-3', style=tab_style, selected_style=selected_style)
            ],
        )
    ], style={'font-size': '20px', 'text-align': 'center'}),
    html.Div(id='tech-1-div'),
    html.Hr(),
    html.Div([
        dcc.Link('Return to MENU', href='/')
    ])
])

### logo_layout ###
logo_layout = html.Div([
    html.Div([
        html.H4('Select logo'),
    ], style={
        'fontSize': 32
    }),
    html.Hr(),
    dcc.RadioItems(
        id='logo-1-radio',
        options=[{'label': i, 'value': i} for i in ['Python', 'SQL', 'Java']]
    ),
    html.Div(id='logo-1-div'),
    html.Hr(),
    dcc.Link('Return do MENU', href='/')
],
style={'textAlign': 'center',
       'fontSize': '20px'})

### Image paths ###
img_python = r'C:\Users\Ryzen\PycharmProjects\dash-tut\07_case_studies\python-logo.png'
img_db = r'C:\Users\Ryzen\PycharmProjects\dash-tut\07_case_studies\db-logo.png'
img_java = r'C:\Users\Ryzen\PycharmProjects\dash-tut\07_case_studies\java-logo.png'

encode_img_python = base64.b64encode(open(img_python, 'rb').read())
encode_img_db = base64.b64encode(open(img_db, 'rb').read())
encode_img_java = base64.b64encode(open(img_java, 'rb').read())


### Callbacks ###
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/technology':
        return tech_layout
    elif pathname == '/logo':
        return logo_layout
    else:
        return index_page


@app.callback(
    Output('tech-1-div', 'children'),
    [Input('tech-1-tabs', 'value')]
)
def tech_1_tabs(value):
    if value == 'tab-1':
        return html.Div([
            dcc.Markdown('''
            ```python
            def fetch_financial_data(company='AMZN'):
                import pandas_datareader.data as web
                return web.DataReader(name=company, data_source='stooq')
            ```
            ''')
        ])
    elif value == 'tab-2':
        return html.Div([
            dcc.Markdown('''
            ```sql
            SELECT * FROM products;
            ```
            ''')
        ])
    else:
        return html.Div([
            dcc.Markdown('''
            ```java
            public class Hello {
              public static void main(String[] args){
                System.out.print("Hello World");
              }
            }
            ```
            ''')
        ])


@app.callback(
    Output('logo-1-div', 'children'),
    [Input('logo-1-radio', 'value')]
)
def logo_1_radio(value):
    if value is None:
        return html.Div([
            html.H6('Select logo')
        ])
    elif value == 'Python':
        return html.Div([
            html.Img(src=f'data:image/png;base64,{encode_img_python.decode()}',
                     style={'width':'300px',})
        ])
    elif value == 'SQL':
        return html.Div([
            html.Img(src=f'data:image/png;base64,{encode_img_db.decode()}',
                     style={'width':'300px'})
        ])
    else:
        return html.Div([
            html.Img(src=f'data:image/png;base64,{encode_img_java.decode()}',
                     style={'width':'300px'})
        ])


if __name__ == '__main__':
    app.run_server(debug=True, port=8093)
