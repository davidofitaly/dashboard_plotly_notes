"""Tworzenie pól wejściowych za pomocą komponentu dcc.Input w Dash

Poniższy kod tworzy pola wejściowe dla różnych zastosowań, używając komponentu dcc.Input w bibliotece Dash.

1. Tworzenie podstawowego pola wejściowego typu tekstowego:
   - `type='text'`: Określa typ pola wejściowego jako tekstowe.

2. Tworzenie pola wejściowego z tekstem zastępczym:
   - `placeholder`: Określa tekst zastępczy, który jest wyświetlany w polu wejściowym, gdy nie ma wprowadzonych żadnych danych.

3. Tworzenie pola wejściowego dla liczb:
   - `type='number'`: Określa typ pola wejściowego jako liczbowe.

4. Tworzenie pola wejściowego dla haseł:
   - `type='password'`: Określa typ pola wejściowego jako hasło, co oznacza, że wprowadzone dane są ukrywane.

5. Tworzenie pola wejściowego dla adresów e-mail:
   - `type='email'`: Określa typ pola wejściowego jako adres e-mail.

6. Tworzenie niestandardowego pola wejściowego z własnym stylem:
   - `id`: Unikalny identyfikator pola wejściowego, który może być używany do jego odniesienia w innych częściach kodu.
   - `style`: Określa niestandardowy styl pola wejściowego, takie jak szerokość, margines, rozmiar czcionki itp.

Parametry te pozwalają na tworzenie różnych typów pól wejściowych i dostosowywanie ich wyglądu i zachowania do potrzeb użytkownika oraz wymagań projektowych.
"""
import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Input(
        type='text',
    ),

    html.Br(),

    dcc.Input(
        type='text',
        placeholder='Wprowadź tekst...'
    ),

    html.Br(),

    dcc.Input(
        type='number',
        placeholder='Wprowadź liczbe..'
    ),

    html.Br(),

    dcc.Input(
        type='password',
        placeholder='Wprowadź haslo..'
    ),

    html.Br(),

    dcc.Input(
        type='email',
        placeholder='Wprowadź email.'
    ),

    html.Br(),

    dcc.Input(
        id='my-input',
        placeholder='Type something here...',
        style={
            'width': '50%',
            'padding': '10px',
            'font-size': '16px',
            'border': '2px solid #4CAF50',  # zielona ramka
            'border-radius': '5px',  # zaokrąglone rogi
            'margin': '10px'
        }
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8059)
