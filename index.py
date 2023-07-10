import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import App, build_graph
# from app_kern import App_Kern, build_graph
# from app_monterey import App_Mont, build_graph
# from app_los_angeles import App_LA, build_graph
# from app_mendocino import App_Mend, build_graph
from homepage import Homepage

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/fresno':
        return App(html.H2("Fresno County"))
    elif pathname == '/kern':
        return App(html.H2("Kern County"))
    elif pathname == '/monterey':
        return App(html.H2("Monterey County"))
    elif pathname == '/los-angeles':
        return App(html.H2("Los Angeles County"))
    elif pathname == '/mendocino':
        return App(html.H2("Mendocino County"))
    else:
        return Homepage()

@app.callback(
    Output('output', 'children'),
    [Input('pop_dropdown', 'value')]
)

def update_graph(city):
    graph = build_graph(city)
    return graph

if __name__ == '__main__':
    app.run_server(debug=True)