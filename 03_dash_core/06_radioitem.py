"""
Tworzenie przycisków wyboru za pomocą komponentu dcc.RadioItems w Dash

Poniższy kod tworzy przyciski wyboru dla różnych zastosowań, używając komponentu dcc.RadioItems w bibliotece Dash.

1. Tworzenie podstawowego zestawu przycisków wyboru:
   - `options`: Określa dostępne opcje przycisków wyboru. Każda opcja jest reprezentowana jako słownik, zawierający etykietę (`label`) widoczną dla użytkownika oraz wartość (`value`) odpowiadającą wybranej opcji.

2. Tworzenie zestawu przycisków wyboru z domyślnie zaznaczoną opcją:
   - `value`: Określa domyślnie zaznaczoną opcję na zestawie przycisków wyboru.

3. Tworzenie zestawu przycisków wyboru z opcją niemożliwą do wybrania:
   - W słowniku reprezentującym opcję można użyć parametru `disabled=True`, aby sprawić, że opcja będzie niemożliwa do zaznaczenia.

4. Tworzenie zestawu przycisków wyboru z niestandardowym układem etykiet:
   - `labelStyle={'display': 'inline-block'}`: Pozwala na ustawienie niestandardowego stylu etykiet przycisków, takiego jak wyświetlanie ich obok siebie (`inline-block`).

Parametry te pozwalają na tworzenie zestawów przycisków wyboru i dostosowywanie ich wyglądu oraz zachowania do potrzeb użytkownika oraz wymagań projektowych.

"""
import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.RadioItems(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java'}
        ]

    ),

    html.Br(),

    dcc.RadioItems(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java'}
        ],
        value='py'
    ),

    html.Br(),

    dcc.RadioItems(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java', 'disabled': True}
        ],
        value='py'
    ),

    html.Br(),

    dcc.RadioItems(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java', 'disabled': True}
        ],
        value='py',
        labelStyle={'display': 'inline-block'}
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8062)
