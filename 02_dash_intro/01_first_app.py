"""
Tworzenie prostej aplikacji internetowej za pomocą Dash i Plotly

Poniższy kod demonstruje sposób tworzenia prostej aplikacji internetowej w języku Python za pomocą bibliotek Dash do budowania interfejsu użytkownika oraz Plotly do generowania wykresów.

1. Importowanie niezbędnych bibliotek:
   - `import dash`: Importuje bibliotekę Dash, która umożliwia tworzenie interfejsu internetowego w stylu aplikacji jednostronicowej.
   - `from dash import dcc, html`: Importuje moduły `dcc` (Dash Core Components) i `html` z biblioteki Dash, które są używane do tworzenia elementów interfejsu użytkownika.
   - `import plotly.graph_objects as go`: Importuje moduł `graph_objects` z biblioteki Plotly, który jest wykorzystywany do tworzenia wykresów.

2. Definiowanie arkuszy stylów zewnętrznych:
   - `external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']`: Określa arkusze stylów CSS zewnętrznych, które zostaną zastosowane do aplikacji.
   W tym przypadku używany jest gotowy arkusz stylów z CodePen.

3. Inicjalizacja aplikacji Dash:
   - `app = dash.Dash(__name__, external_stylesheets=external_stylesheets)`: Tworzy obiekt aplikacji Dash, a parametr `external_stylesheets` definiuje używane arkusze stylów zewnętrznych.

4. Definiowanie układu interfejsu użytkownika:
   - `app.layout = html.Div(...)`: Definiuje układ interfejsu użytkownika za pomocą elementów HTML z biblioteki Dash.
   W tym przypadku jest to prosty kontener `html.Div`, który zawiera nagłówek (`html.H2`), opis (`html.Div`) oraz wykres (`dcc.Graph`).

5. Uruchamianie aplikacji:
   - `app.run_server(debug=True, port=8052)`: Uruchamia aplikację na serwerze lokalnym, nasłuchując na porcie 8052.
   Parametr `debug=True` włącza tryb debugowania, umożliwiając wyświetlanie komunikatów debugowania w przypadku błędów.

Opis komponentów interfejsu użytkownika:
   - `html.H2`: Komponent Dash reprezentujący nagłówek drugiego poziomu HTML.
   - `html.Div`: Komponent Dash reprezentujący kontener na inne elementy interfejsu użytkownika.
   - `dcc.Graph`: Komponent Dash używany do wyświetlania wykresów Plotly w interfejsie użytkownika.
      - `figure`: Parametr określający konkretny wykres Plotly, który zostanie wyświetlony. W tym przypadku jest to wykres słupkowy (`go.Bar`).

"""

import dash
from dash import dcc, html
import plotly.graph_objects as go
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H2(children='Hello Dash'),
    html.Div(children='To moja pierwsza aplikacja w Pythonie'),
    dcc.Graph(
        figure=go.Figure(
            go.Bar(
                x=[1,2,3],
                y=[2,1,3]
            )
        )
    )
])


if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
