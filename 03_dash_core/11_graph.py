"""
worzenie wykresu słupkowego:
   - `figure`: Określa dane i układ wykresu za pomocą obiektu klasy go.Figure z biblioteki Plotly.
      - `data`: Lista obiektów klasy go.Bar, określających dane dla poszczególnych serii danych.
         - Dla każdej serii danych definiowane są:
            - `x`: Wartości na osi X.
            - `y`: Wartości na osi Y.
            - `name`: Nazwa serii danych, która będzie wyświetlana w legendzie.
            - `marker`: Określa stylizację słupków, w tym kolor, za pomocą obiektu klasy go.bar.Marker.
      - `layout`: Obiekt klasy go.Layout, określający układ wykresu, takie jak tytuł i legenda.
         - `title`: Tytuł wykresu.
         - `showlegend`: Określa, czy legenda powinna być wyświetlana (True) czy nie (False).


"""
import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Graph(
        figure = go.Figure(

            data = [
                go.Bar(
                    x=[2017, 2018, 2019],
                    y=[219, 146, 167],
                    name='Sprzedaż USA',
                    marker=go.bar.Marker(
                        color='rgb(55,83,109)'
                    )
                ),
                go.Bar(
                    x=[2017,2018,2019],
                    y=[230,180,260],
                    name='Sprzedaż Europa',
                    marker=go.bar.Marker(
                        color='rgb(26,118,255)'
                    )
                )
            ],
            layout = go.Layout(
                title='Sprzedaż',
                showlegend=True,

            )
        )

    )

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8067)
