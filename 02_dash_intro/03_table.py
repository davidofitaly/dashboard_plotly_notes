"""
Tworzenie tabeli z notowaniami spółki Amazon

Poniższy kod tworzy tabelę z notowaniami spółki Amazon, zawierającą informacje o dacie,
cenie otwarcia, cenie najwyższej, cenie najniższej, cenie zamknięcia oraz wolumenie.

1. Definiowanie układu interfejsu użytkownika:
   - `app.layout = html.Div([...])`: Definiuje układ interfejsu użytkownika za pomocą elementów HTML z biblioteki Dash.
   Głównym kontenerem jest `html.Div`.

2. Dodawanie nagłówka:
   - `html.H4('Notowania spółki Amazon')`: Dodaje nagłówek "Notowania spółki Amazon" czwartego poziomu w hierarchii HTML.

3. Tworzenie tabeli:
   - `html.Table([...])`: Tworzy tabelę HTML.
      - `html.Tr([...])`: Definiuje wiersz tabeli.
         - `html.Th('Date')`: Tworzy komórkę nagłówka dla kolumny "Date" (Data).
         - `html.Td('2019-09-01')`: Tworzy komórkę danych dla konkretnej daty.
         - Analogicznie dla pozostałych kolumn: "Open" (Otwarcie), "High" (Najwyższy), "Low" (Najniższy), "Close" (Zamknięcie), "Volume" (Wolumen).

Wynikiem działania tego kodu jest tabela zawierająca notowania spółki Amazon z określonych dat oraz odpowiadających im danych dotyczących ceny akcji.

"""

import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H4('Notowania spółki Amazon'),

    html.Table([

        html.Tr([
            html.Th('Date'),
            html.Th('Open'),
            html.Th('High'),
            html.Th('Low'),
            html.Th('Close'),
            html.Th('Volume')
        ]),
        html.Tr([
            html.Td('2019-09-01'),
            html.Td('100'),
            html.Td('102'),
            html.Td('98'),
            html.Td('100'),
            html.Td('150000')
        ]),
        html.Tr([
            html.Td('2019-09-02'),
            html.Td('101'),
            html.Td('103'),
            html.Td('98'),
            html.Td('100'),
            html.Td('140000')
        ])
    ])





])

if __name__ == '__main__':
    app.run_server(debug=True, port=8054)
