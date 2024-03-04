"""
Tworzenie interaktywnej aplikacji internetowej za pomocą Dash i Plotly

Poniższy kod demonstruje sposób tworzenia interaktywnej aplikacji internetowej w języku Python za pomocą bibliotek Dash
do budowania interfejsu użytkownika oraz Plotly do generowania wykresów.

1. Importowanie niezbędnych bibliotek:
   - `import dash`: Importuje bibliotekę Dash, która umożliwia tworzenie interfejsu internetowego w stylu aplikacji jednostronicowej.
   - `from dash import dcc, html`: Importuje moduły `dcc` (Dash Core Components) i `html` z biblioteki Dash, które są używane do tworzenia elementów interfejsu użytkownika.
   - `import plotly.graph_objects as go`: Importuje moduł `graph_objects` z biblioteki Plotly, który jest wykorzystywany do tworzenia wykresów.

2. Definiowanie arkuszy stylów zewnętrznych:
   - `external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']`: Określa arkusze stylów CSS zewnętrznych,
   które zostaną zastosowane do aplikacji. W tym przypadku używany jest gotowy arkusz stylów z CodePen.

3. Definiowanie kolorów:
   - `colors`: Słownik zawierający definicje kolorów używanych w aplikacji, takie jak tło (`background`) i tekst (`text`).

4. Inicjalizacja aplikacji Dash:
   - `app = dash.Dash(__name__, external_stylesheets=external_stylesheets)`: Tworzy obiekt aplikacji Dash, a parametr
   `external_stylesheets` definiuje używane arkusze stylów zewnętrznych.

5. Definiowanie układu interfejsu użytkownika:
   - `app.layout`: Określa układ interfejsu użytkownika, który składa się z nagłówka, opisu oraz wykresu słupkowego.
      - `html.H2`: Nagłówek drugiego poziomu HTML z tekstem 'Hello Dash', stylizowany za pomocą definicji kolorów i wyśrodkowany (`textAlign`).
      - `html.Div`: Kontener na opis, również stylizowany i wyśrodkowany.
      - `dcc.Graph`: Wykres słupkowy, który zawiera dwa serie danych, każda z nich zdefiniowana przez obiekt `go.Bar`.
      Stylizowany jest tło wykresu (`plot_bgcolor`) oraz tło papieru (`paper_bgcolor`).

6. Uruchamianie aplikacji:
   - `app.run_server(debug=True, port=8053)`: Uruchamia aplikację na serwerze lokalnym, nasłuchując na porcie 8053.
   Parametr `debug=True` włącza tryb debugowania, umożliwiając wyświetlanie komunikatów debugowania w przypadku błędów.

Opis stylów CSS:
   - `style`: Stylizuje główny kontener `html.Div`, określając tło (`backgroundColor`) na podstawie definicji kolorów.
   - `style` w `html.H2` i `html.Div`: Stylizuje tekst w nagłówku i opisie, określając kolor tekstu i wyśrodkowanie tekstu (`textAlign`).
   - `marker_color`: Określa kolor wypełnienia słupków wykresu.
    - `marker_line_color`: Określa kolor krawędzi (linii) słupków wykresu.
    - `marker_line_width`: Określa szerokość krawędzi (linii) słupków wykresu.

`plot_bgcolor`: Określa kolor tła obszaru roboczego wykresu. Jest to tło znajdujące się za samymi wykresami, obejmujące
obszar, gdzie znajdują się wszystkie elementy wykresu, takie jak tło samego wykresu, tytuł, osie itp.
 Wartość tego parametru może być ustawiona na konkretny kolor lub być zdefiniowana wcześniej w słowniku kolorów.

`paper_bgcolor`: Określa kolor tła papieru. Jest to tło znajdujące się za samymi wykresami, poza obszarem roboczym wykresu.
Obejmuje ono obszar, który otacza wykres. Wartość tego parametru może być ustawiona na konkretny kolor.

"""

import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background':'#b1f2c2',
    'text':' #4c524d'

}

app.layout = html.Div([

    html.H2('Hello Dash',
            style={'color': colors['text'],
                   'textAlign': 'center'
             }),

    html.Div('Dash: A web application framework for Python',
             style = {
                 'color': colors['text'],
                 'textAlign': 'center'
             }),

    dcc.Graph(

        figure = go.Figure([
            go.Bar(
                x=['2017','2018', '2019'],
                y=[150, 180, 220],
                marker_color='#9ed6f9',
                marker_line_color='#4c524d',
                marker_line_width=3
            ),
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[120, 160, 280],
                marker_color='#077eb5',
                marker_line_color='#4c524d',
                marker_line_width=3
            )],
            layout=go.Layout(
                title='Wizualizacja danych',
                plot_bgcolor=colors['background'],
                paper_bgcolor='#08825f',

            )
        )
    )

], style= {
    'backgroundColor': colors['background']
})

if __name__ == '__main__':
    app.run_server(debug=True, port=8053)
