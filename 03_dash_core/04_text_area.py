"""
Tworzenie obszarów tekstowych za pomocą komponentu dcc.Textarea w Dash

Poniższy kod tworzy obszary tekstowe dla różnych zastosowań, używając komponentu dcc.Textarea w bibliotece Dash.

1. Tworzenie podstawowego obszaru tekstowego:
   - `placeholder`: Określa tekst zastępczy, który jest wyświetlany w obszarze tekstowym, gdy nie ma wprowadzonych żadnych danych.
   - `style={'width': '100%'}`: Określa szerokość obszaru tekstowego na 100% szerokości kontenera, w którym się znajduje.
   - `value=''`: Określa wartość domyślną dla obszaru tekstowego.

2. Tworzenie niestandardowego obszaru tekstowego z określoną szerokością:
   - `placeholder`: Określa tekst zastępczy, który jest wyświetlany w obszarze tekstowym, gdy nie ma wprowadzonych żadnych danych.
   - `style={'width': '60%'}`: Określa szerokość obszaru tekstowego na 60% szerokości kontenera, w którym się znajduje.
   - `value='xxx'`: Określa wartość domyślną dla obszaru tekstowego.

Parametry te pozwalają na tworzenie obszarów tekstowych o różnych rozmiarach i dostosowywanie ich wyglądu do potrzeb użytkownika oraz wymagań projektowych.

"""

import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Textarea(
        placeholder='Wprowadź wartość',
        style={'width': '100%'},
        value=''
    ),

    html.Br(),

    dcc.Textarea(
        placeholder='Wrpwoadź wartość',
        style={'width': '60%'},
        value='xxx'
    ),



])

if __name__ == '__main__':
    app.run_server(debug=True, port=8060)
