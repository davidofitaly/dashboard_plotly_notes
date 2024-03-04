"""
Pobieranie i wyświetlanie notowań spółki Amazon za pomocą biblioteki pandas_datareader i Dash

Poniższy kod pobiera notowania spółki Amazon z określonego źródła danych i wyświetla je w formie tabeli za pomocą biblioteki Dash.

1. Definiowanie funkcji do pobierania danych finansowych:
   - `fetch_financial_data(company='AMZN')`: Funkcja pobiera notowania finansowe spółki o nazwie `company` z
   określonego źródła danych (w tym przypadku 'stooq') za pomocą biblioteki pandas_datareader. Domyślnie nazwa spółki jest ustawiona na 'AMZN' (Amazon).
   - Funkcja zwraca obiekt DataFrame zawierający pobrane dane.

2. Pobieranie danych finansowych i przetwarzanie:
   - `df = fetch_financial_data()`: Wywołuje funkcję `fetch_financial_data()` i zapisuje wynik w obiekcie DataFrame `df`.
   - `df.reset_index(inplace=True)`: Resetuje indeksy w obiekcie DataFrame `df`.
   - `df = df[:30]`: Wybiera pierwsze 30 wierszy (lub mniej, jeśli danych jest mniej) z obiektu DataFrame `df`.
   - `min_val = min(len(df), 30)`: Określa minimalną wartość między długością obiektu DataFrame `df` a 30 i zapisuje wynik w zmiennej `min_val`.

3. Definiowanie układu interfejsu użytkownika:
   - `app.layout = html.Div([...])`: Definiuje układ interfejsu użytkownika za pomocą elementów HTML z biblioteki Dash. Głównym kontenerem jest `html.Div`.
   - `html.H4('Notowania spółki Amazon')`: Dodaje nagłówek "Notowania spółki Amazon" czwartego poziomu w hierarchii HTML.
   - `html.Table([...])`: Tworzy tabelę HTML.
      - `html.Tr([html.Th(col) for col in df.columns])`: Tworzy wiersz nagłówków tabeli, gdzie każdy nagłówek odpowiada nazwie kolumny w obiekcie DataFrame `df`.
      - `html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(min_val)`: Tworzy wiersze z danymi tabeli, gdzie każda komórka odpowiada wartości w odpowiedniej kolumnie dla każdego wiersza w obiekcie DataFrame `df` (do minimalnej wartości `min_val`).

Wynikiem działania tego kodu jest tabela zawierająca notowania spółki Amazon z określonego zakresu danych.

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
df = df[:30]
min_val = min(len(df), 30)

app.layout = html.Div([

    html.H4('Notowania spółki Amazon'),
    html.Table([
        html.Tr([html.Th(col) for col in df.columns])] +

        [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(min_val)]

    )

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8055)
