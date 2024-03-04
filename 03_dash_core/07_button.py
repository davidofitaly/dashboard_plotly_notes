"""
Tworzenie przycisków za pomocą komponentu html.Button w Dash

Poniższy kod tworzy przyciski dla różnych zastosowań, używając komponentu html.Button w bibliotece Dash.

1. Tworzenie podstawowego przycisku:
   - Tekst przycisku jest określany jako tekst znajdujący się między znacznikami `<html.Button>`.
   - W tym przypadku nie dodano żadnych dodatkowych parametrów, co oznacza, że przycisk będzie aktywny.

2. Tworzenie wyłączonego przycisku:
   - `disabled=True`: Parametr `disabled` ustawiony na True powoduje, że przycisk staje się nieaktywny (wyłączony), czyli użytkownik nie może na niego kliknąć.

3. Tworzenie wyłączonego przycisku z typem 'submit':
   - `disabled=True`: Parametr `disabled` ustawiony na True powoduje, że przycisk staje się nieaktywny (wyłączony), czyli użytkownik nie może na niego kliknąć.
   - `type='submit'`: Określa typ przycisku jako 'submit', co oznacza, że przycisk będzie wysyłał formularz, jeśli zostanie kliknięty. W tym przypadku, chociaż przycisk jest wyłączony, zachowa on swoje zachowanie związane z formularzem.

Parametry te pozwalają na tworzenie przycisków i dostosowywanie ich wyglądu oraz zachowania do potrzeb użytkownika oraz wymagań projektowych.

"""
import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Button("Zapisz"),

    html.Br(),

    html.Button('Zapisz', disabled=True),

    html.Br(),

    html.Button('Zapisz', disabled=True, type='submit')

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8063)
