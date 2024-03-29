import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from dash import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def fetch_financial_data(company='AMZN'):
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

df = fetch_financial_data()
df = df.reset_index()
df = df[:30]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dash_table.DataTable(
        id='table-1',
        columns = [{'name': col, 'id': col, 'deletable': True, 'selectable': True} for col in df.columns],
        data = df.to_dict('records'),
        editable=True,
        filter_action='native',
        sort_action='native',
        page_action='native',
        page_current=0,
        page_size=10,
        column_selectable='multi',
        row_selectable='multi',
        row_deletable=True,
        selected_columns=[],
        selected_rows=[]


    )
])

@app.callback(
    Output('table-1', 'style_data_conditional'),
    [Input('table-1', 'selected_columns'),
     Input('table-1', 'selected_rows')]
)
def update_style(selected_columns, selected_rows):
    styles = []
    if selected_columns:
        styles.extend([{
            'if': {'column_id': col},
            'background_color': '#EFB5B5'
        } for col in selected_columns])
    if selected_rows:
        styles.extend([{
            'if': {'row_index': row},
            'background_color': '#EFB5B5'
        } for row in selected_rows])
    return styles



if __name__ == '__main__':
    app.run_server(debug=True, port=8086)
