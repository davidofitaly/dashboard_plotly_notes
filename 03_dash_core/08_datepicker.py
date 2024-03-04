"""

1. Tworzenie pojedynczego pola wyboru daty:
   - `date`: Określa datę, która będzie wyświetlana początkowo w polu wyboru daty.
   - Brak innych parametrów, co oznacza, że domyślny format daty będzie używany do wyświetlania.

2. Tworzenie pojedynczego pola wyboru daty z określonym formatem wyświetlania:
   - `date`: Określa datę, która będzie wyświetlana początkowo w polu wyboru daty.
   - `display_format='YYYY-MM-DD'`: Określa niestandardowy format wyświetlania daty.
   W tym przypadku, data będzie wyświetlana w formacie 'RRRR-MM-DD'.

3. Tworzenie pojedynczego pola wyboru daty z innym niestandardowym formatem wyświetlania:
   - `date`: Określa datę, która będzie wyświetlana początkowo w polu wyboru daty.
   - `display_format='DD-MM-YYYY'`: Określa niestandardowy format wyświetlania daty.
   W tym przypadku, data będzie wyświetlana w formacie 'DD-MM-RRRR'.

4. Tworzenie zakresu wyboru daty:
   - `start_date`: Określa datę początkową zakresu, która będzie wyświetlana początkowo.
   - `end_date`: Określa datę końcową zakresu, która będzie wyświetlana początkowo.
   - `display_format='DD-MM-YYYY'`: Określa niestandardowy format wyświetlania daty.
   W tym przypadku, data będzie wyświetlana w formacie 'DD-MM-RRRR'.

"""
import dash
from dash import dcc, html
import plotly.graph_objects as go
from datetime import datetime as dt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.DatePickerSingle(

        date=dt(2019, 1, 1)
    ),

    html.Br(),

    dcc.DatePickerSingle(

        date=dt(2019, 1, 1),
        display_format='YYYY-MM-DD'
    ),

    html.Br(),

    dcc.DatePickerSingle(

        date=dt(2019, 1, 1),
        display_format='DD-MM-YYYY'
    ),

    html.Br(),

    dcc.DatePickerRange(

        start_date=dt(2019,9, 1),
        end_date=dt(2019,10,31),
        display_format='DD-MM-YYYY'
    ),


])

if __name__ == '__main__':
    app.run_server(debug=True, port=8064)
