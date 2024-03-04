"""
Tworzenie interaktywnego wykresu za pomocą bibliotek Dash i Plotly

Poniższy kod demonstruje sposób wykorzystania biblioteki Dash do tworzenia interaktywnego interfejsu użytkownika oraz
biblioteki Plotly do generowania wykresów.

1. Importowanie niezbędnych bibliotek:
   - `from dash import dcc, html`: Importuje moduły `dcc` (Dash Core Components) i `html` z biblioteki Dash.
   - `import plotly.graph_objects as go`: Importuje moduł `graph_objects` z biblioteki Plotly i nadaje mu alias `go`.

2. Inicjalizacja aplikacji Dash:
   - `app = dash.Dash(__name__)`: Tworzy obiekt aplikacji Dash i przypisuje go do zmiennej `app`.

3. Tworzenie układu interfejsu użytkownika:
   - `app.layout = html.Div(...)`: Definiuje układ interfejsu użytkownika za pomocą elementów HTML z biblioteki Dash.

4. Dodawanie komponentów do interfejsu użytkownika:
   - `html.H2(children='Hello Dash!')`: Dodaje nagłówek "Hello Dash!" do interfejsu użytkownika.
   - `dcc.Graph(figure=go.Figure([...]))`: Dodaje interaktywny wykres do interfejsu użytkownika, gdzie `go.Figure([...])`
    definiuje wykres za pomocą modułu `graph_objects` z biblioteki Plotly.

5. Uruchamianie aplikacji:
   - `app.run_server(port=8050)`: Uruchamia aplikację na serwerze lokalnym, nasłuchując na porcie 8050.

Opis komponentów wykresu:

- `dcc.Graph`: Komponent Dash używany do wyświetlania wykresów Plotly w interfejsie użytkownika.
   - `figure`: Parametr określający konkretny wykres Plotly, który zostanie wyświetlony.
      - `go.Figure([...])`: Tworzenie obiektu `Figure` z biblioteki Plotly, który zawiera wszystkie dane i
      ustawienia wykresu.
         - `go.Bar(...)`: Dodaje słupki do wykresu.
            - `x`: Dane dla osi X, w tym przypadku lata.
            - `y`: Dane dla osi Y, w tym przypadku liczba sprzedaży.
            - `name`: Nazwa serii danych, w tym przypadku "local" i "online", odpowiadające lokalnej i online sprzedaży
            dla każdego roku.

"""

import dash
from dash import dcc, html
import plotly.graph_objects as go


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H2(children='Hello Dash!'),

    dcc.Graph(
        figure = go.Figure([
            go.Bar(
                x = ['2017', '2018', '2019'],
                y = [150, 180, 220],
                name='local'
            ),
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[80, 160, 240],
                name='online'
            ),
        ])
    )

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)