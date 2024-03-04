"""
Tworzenie interaktywnego wykresu z suwakiem za pomocą komponentów dcc.Graph i dcc.Slider w Dash

Poniższy kod demonstruje tworzenie interaktywnego wykresu, który reaguje na zmiany wartości suwaka, wykorzystując komponenty dcc.Graph i dcc.Slider w bibliotece Dash.

1. Tworzenie wykresu:
   - `dcc.Graph`: Komponent do wyświetlania interaktywnych wykresów.
      - `id='graph-1'`: Unikalny identyfikator dla komponentu wykresu, używany w funkcji zwrotnej (callback) do aktualizacji wykresu.
   - `dcc.Slider`: Komponent do tworzenia suwaka.
      - `id='slider-01'`: Unikalny identyfikator dla komponentu suwaka, używany w funkcji zwrotnej (callback) do reakcji na zmiany wartości suwaka.
      - `min`, `max`: Minimalna i maksymalna wartość suwaka, zgodnie z wartościami danych.
      - `value`: Domyślna wartość suwaka, ustawiona na minimalną wartość roku w danych.
      - `marks`: Słownik określający podziałkę na suwaku, z etykietami opisującymi wartości.
      - `step=None`: Określa, że suwak może być przesuwany o dowolną wartość.

2. Aktualizacja wykresu w zależności od wartości suwaka:
   - Funkcja zwrotna `update_graph` jest wywoływana za każdym razem, gdy wartość suwaka zostanie zmieniona.
   - Na podstawie wybranej wartości roku `selected_year` z suwaka, wykres jest aktualizowany.
   - Dane są filtrowane dla wybranego roku, a następnie wykres jest tworzony na podstawie tych danych.
   - Wartości `gdpPercap` są umieszczane na osi X, a wartości `lifeExp` na osi Y, tworząc wykres punktowy (scatter plot).
   - Każdy punkt na wykresie reprezentuje jeden kraj, a kształt i rozmiar punktów są dostosowane za pomocą parametrów stylizacji markerów.

3. Parametry wykresu:
   - `title_text`: Tytuł wykresu.
   - `xaxis`: Konfiguracja osi X, w tym typ skali (`'log'`) i tytuł osi.
   - `yaxis`: Konfiguracja osi Y, w tym tytuł osi.
   - `hovermode`: Tryb interaktywnego wyświetlania informacji na wykresie.

Ten przykład ilustruje, jak można tworzyć interaktywne wykresy w Dash, które reagują na działania użytkownika, takie jak przesuwanie suwaka.

"""
import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/dash_course/data.csv')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-1'),
    dcc.Slider(
        id='slider-01',
        min=df.year.min(),
        max=df.year.max(),
        value=df.year.min(),
        marks={str(year): str(year) for year in df.year.unique()},
        step=None
    )
])
@app.callback(
    Output('graph-1', 'figure'),
    [Input('slider-01', 'value')]

)
def update_graph(selected_year):
    dff = df.query(f'year == {selected_year}')
    traces = []
    for cont in df.continent.unique():
        dff_cont = dff[dff.continent == cont]
        traces.append(
            go.Scatter(
                x=dff_cont.gdpPercap,
                y=dff_cont.lifeExp,
                mode='markers',
                name=cont,
                opacity=0.6,
                marker={
                    'size': 15,
                    'line': {'width': 1.5, 'color': 'white'}
                }
            )
        )
    return {
        'data': traces,
        'layout': go.Layout(
            title_text='Wykres',
            xaxis={'type': 'log', 'title':'PKG per capita'},
            yaxis={'title': 'Oczekiwana długosc zycia'},
            hovermode='closest'
        )
    }



if __name__ == '__main__':
    app.run_server(debug=True, port=8072)
