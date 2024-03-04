"""
Tworzenie suwaków za pomocą komponentu dcc.Slider w Dash

Poniższy kod tworzy suwaki dla różnych zastosowań, używając komponentu dcc.Slider w bibliotece Dash.

1. Tworzenie suwaka podstawowego:
   - `min`: Określa minimalną wartość suwaka.
   - `max`: Określa maksymalną wartość suwaka.
   - `step`: Określa wartość kroku, o którą suwak się przesuwa.
   - value: Początkowa wartość suwaka

2. Tworzenie suwaka z niestandardowymi etykietami:
   - `marks`: Pozwala na zdefiniowanie niestandardowych etykiet dla określonych wartości na suwaku. Jest to słownik, gdzie kluczami są wartości na suwaku, a wartościami są odpowiadające im etykiety.

3. Tworzenie suwaka z automatycznie generowanymi etykietami:
   - `marks`: Możemy również wygenerować etykiety automatycznie za pomocą składni słownikowej. W przykładzie `marks={i:f'Label {i}' for i in range(4)}` każda wartość suwaka od 0 do 3 będzie miała etykietę "Label i".

Parametry te pozwalają na dostosowanie suwaków do różnych potrzeb i umożliwiają użytkownikowi interakcję poprzez wybieranie wartości z określonego zakresu. W połączeniu z innymi komponentami Dash można tworzyć interaktywne aplikacje do wizualizacji danych i analizy.

"""
import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Label('Slider'),

    dcc.Slider(
        min=0,
        max=3,
        step=1
    ),
    html.Br(),

    dcc.Slider(
        min=0,
        max=3,
        step=1,
        marks={0:'Label 0', 1: 'Label 1', 2: 'Label 2', 3: 'Label 3'}
    ),
    html.Br(),

    dcc.Slider(
        min=0,
        max=3,
        step=1,
        marks={i:f'Label {i}' for i in range(4)}
    ),


])

if __name__ == '__main__':
    app.run_server(debug=True, port=8058)
