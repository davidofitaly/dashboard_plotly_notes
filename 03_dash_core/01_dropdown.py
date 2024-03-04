"""Tworzenie rozwijanych list (dropdowns) za pomocą komponentu dcc.Dropdown w Dash

Poniższy kod tworzy rozwijane listy (dropdowns) dla różnych zastosowań, używając komponentu dcc.Dropdown w bibliotece Dash.

1. Tworzenie rozwijanej listy z jednym wyborem:
   - `options`: Określa dostępne opcje w rozwijanej liście. Każda opcja jest reprezentowana jako słownik, zawierający etykietę (`label`) widoczną dla użytkownika oraz wartość (`value`) odpowiadającą wybranej opcji.
   - `value`: Określa domyślną wartość wybraną na początku.

2. Tworzenie rozwijanej listy z wieloma wyborami:
   - Parametr `multi` ustawiony na `True` umożliwia użytkownikowi wybór wielu opcji jednocześnie. Parametr `value` może być listą wartości, które są domyślnie zaznaczone.

3. Ustawienie rozwijanej listy jako niemożliwej do wyszukania:
   - Parametr `searchable` ustawiony na `False` uniemożliwia użytkownikowi wyszukiwanie w rozwijanej liście.

4. Ustawienie tekstu zastępczego dla rozwijanej listy:
   - Parametr `placeholder` określa tekst wyświetlany w rozwijanej liście, gdy nie została jeszcze wybrana żadna opcja.

5. Wyłączenie możliwości wybierania w rozwijanej liście:
   - Parametr `disabled` ustawiony na `True` blokuje rozwijaną listę, uniemożliwiając użytkownikowi wybieranie opcji.

Dzięki tym parametrom można dostosować zachowanie i wygląd rozwijanych list w aplikacji Dash do konkretnych potrzeb użytkowników i wymagań projektu.
"""
import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([



    html.Label('Wybierz preferowaną technologie'),

    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value':'java'}
        ],
        value='py',
    ),

    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java'}
        ],
        value='py',
        multi=True
    ),

    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java'}
        ],
        searchable=False
    ),

    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java'}
        ],
        placeholder='Wybierz technologie...'
    ),

    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'java'}
        ],
        disabled=True
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8057),
