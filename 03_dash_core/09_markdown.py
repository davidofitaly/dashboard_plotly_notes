import dash
from dash import dcc, html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

markdown = """
Nagłówki:

#H1
## H2
### H3
#### H4
##### H5
###### H6

Znaczniki tekstu:

Kursywa: *tekst kursywa* lub _tekst kursywa_  
Pogrubienie: **tekst pogrubiony** lub __tekst pogrubiony__  
Kursywa i pogrubieni: **_pogrubienie i kursywa_**  
Przekreślenie ~~Przekreslenie~~


Listy:

Lista uporzadkowana:  
1. Python  
2. SQL  
3. Java  

Lista nieuporzadkowana:  
* Python  
* SQL  
* JAVA  

Linkowanie:  

[Google.com](http://www.google.com) 


Kod:  

Uzyj  `print('Hello World)`  


```
import numpy as np

x = np.random.randn(100)
print(x)

```
```
SELECT * FROM products;
```

Table:

|UserID|Rating|Age|
|------|------|---|
|001   |4.5   |23 |
|002   |5     |34 |


Cytowanie:  

> Python jest bardzo poręczny i łatwy do nauki.


Linie horyzontalne  

---

"""

app.layout = html.Div([

    dcc.Markdown(markdown)

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8065)
