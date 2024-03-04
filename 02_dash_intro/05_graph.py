"""
Tworzenie interaktywnych wykresów notowań spółki Amazon za pomocą Dash i Plotly

Poniższy kod tworzy interaktywne wykresy cen zamknięcia i wolumenu spółki Amazon. Wykresy te są wyświetlane w formie linii (dla cen zamknięcia) i słupków (dla wolumenu).

1. Definiowanie układu interfejsu użytkownika:
   - `app.layout = html.Div([...])`: Definiuje układ interfejsu użytkownika za pomocą elementów HTML z biblioteki Dash. Głównym kontenerem jest `html.Div`.
   - `html.H4('Notowania spółki Amazon')`: Dodaje nagłówek "Notowania spółki Amazon" czwartego poziomu w hierarchii HTML.

2. Dodawanie pierwszego wykresu (liniowego):
   - `dcc.Graph([...])`: Dodaje komponent Dash do wyświetlania wykresów Plotly.
      - `go.Figure([...])`: Tworzy obiekt figury, który będzie zawierał dane i ustawienia wykresu.
         - `data`: Definiuje dane dla wykresu.
            - `go.Scatter([...])`: Tworzy wykres liniowy.
               - `x=df.Date`: Określa wartości na osi X, które są datami.
               - `y=df.Close`: Określa wartości na osi Y, które są cenami zamknięcia.
               - `mode='lines'`: Określa tryb rysowania linii.
               - `fill='tozeroy'`: Wypełnia obszar pod krzywą.
               - `name='Amazon'`: Określa nazwę serii danych.
         - `layout`: Definiuje układ wykresu.
            - `yaxis_type='log'`: Ustawia skalę osi Y na logarytmiczną.
            - `height=500`: Ustawia wysokość wykresu na 500 pikseli.
            - `title='Wykres ceny'`: Ustawia tytuł wykresu.
            - `showlegend=True`: Wyświetla legendę wykresu.

3. Dodawanie drugiego wykresu (słupkowego):
   - Analogicznie do pierwszego wykresu, ale używając wykresu słupkowego (`go.Bar`) zamiast wykresu liniowego. Dane na osi Y są teraz wolumenem, a reszta parametrów jest podobna do pierwszego wykresu.

Wynikiem działania tego kodu jest wyświetlanie dwóch interaktywnych wykresów: wykresu cen zamknięcia spółki Amazon oraz wykresu wolumenu na przestrzeni określonego przedziału czasowego.

"""

import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def fetch_financial_data(company='AMZN'):
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')


df = fetch_financial_data()
df.reset_index(inplace=True)
df = df[df.Date > '2019-01-01']

app.layout = html.Div([

    html.H4('Notowania spółki Amazon'),

    dcc.Graph(
        figure = go.Figure(
            data=[
                go.Scatter(
                    x = df.Date,
                    y=df.Close,
                    mode='lines',
                    fill='tozeroy',
                    name='Amazon'
                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=500,
                title='Wykres ceny',
                showlegend=True
            )
        )

    ),

    dcc.Graph(
        figure = go.Figure(
            data=[
                go.Bar(
                    x=df.Date,
                    y=df.Volume,
                    name='Wolumen'
                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=300,
                title='Wykres Volumenu',
                showlegend=True
            )
        )
    )


])

if __name__ == '__main__':
    app.run_server(debug=True, port=8056)
