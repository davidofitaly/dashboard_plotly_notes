"""
Tworzenie list wyboru za pomocą komponentu dcc.Checklist w Dash

Poniższy kod tworzy listy wyboru dla różnych zastosowań, używając komponentu dcc.Checklist w bibliotece Dash.

1. Tworzenie podstawowej listy wyboru:
   - `options`: Określa dostępne opcje w liście wyboru. Każda opcja jest reprezentowana jako słownik, zawierający etykietę (`label`) widoczną dla użytkownika oraz wartość (`value`) odpowiadającą wybranej opcji.

2. Tworzenie listy wyboru z domyślnie zaznaczoną opcją:
   - `value`: Określa domyślnie zaznaczoną opcję lub opcje w liście wyboru. Może to być pojedyncza wartość lub lista wartości, które są domyślnie zaznaczone.

3. Tworzenie listy wyboru z wieloma domyślnie zaznaczonymi opcjami:
   - Parametr `value` może być listą wartości, które są domyślnie zaznaczone.

4. Tworzenie listy wyboru z opcją niemożliwą do wybrania:
   - W słowniku reprezentującym opcję można użyć parametru `disabled=True`, aby sprawić, że opcja będzie niemożliwa do zaznaczenia.

Parametry te pozwalają na tworzenie list wyboru i dostosowywanie ich wyglądu oraz zachowania do potrzeb użytkownika oraz wymagań projektowych.

"""

import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Checklist(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java'}
        ],

    ),

    html.Br(),

    dcc.Checklist(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java'}
        ],
        value=['py']
    ),

    html.Br(),

    dcc.Checklist(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java'}
        ],
        value=['py', 'sql']
    ),

    html.Br(),

    dcc.Checklist(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java', 'disabled':True}
        ],
        value=['py', 'sql']
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8061)
