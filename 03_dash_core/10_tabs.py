"""

1. Tworzenie zakładki:
   - `label`: Określa etykietę (nazwę) zakładki, która będzie wyświetlana jako tytuł zakładki.
   - `children`: Określa zawartość (treść) zakładki. Może to być pojedynczy komponent lub lista komponentów, które będą wyświetlane w zakładce.


"""
import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H3('Hello World - Porównanie'),
    html.Br(),

    dcc.Tabs(
        children=[
            dcc.Tab(
                label='Python',
                children=[
                    dcc.Markdown(
                        """
                        ```
                        print('Hello World!')
                        ```
                        """
                    )
                ]
            ),
            dcc.Tab(
                label='Java',
                children = [
                    dcc.Markdown(
                        """
                        ```
                        public class Hello {
                        public static void main(String[] args)}
                        System.out.print('Hello World')
                        ```
                        """


                    )
                ]
            )
        ]
    )

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8066)
