import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import json
import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go

from navbar import Navbar
nav = Navbar()

df = gpd.read_file('/home/akube/mysite/California_County_Boundaries.geojson')
df.County_FIPS_ID = df.County_FIPS_ID.apply(int)

df['Tested'] = "No"

df.loc[(df['CountyName'] == 'Fresno') | (df['CountyName'] == 'Los Angeles') | (df['CountyName'] == 'Monterey') | (df['CountyName'] == 'Kern') | (df['CountyName'] == 'Mendocino'),'Tested'] = "Yes"
df.set_index("CountyName")

def display_choropleth(df, title):
    fig = px.choropleth(df, geojson=df.geometry, color="Tested",
        locations=df.index, hover_name="CountyName",
        title=title, center={"lat": 36.7783,"lon": 119.4179})
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, width = 700, showlegend=False)
    return fig

body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H2("CAN Network - Data Science for Social Impact"),
                     html.H3("Mapping a Healthier Future: Investigating the Human and Ecological Consequences of Pesticide Use in California"),
                     html.P(
                         """\
                         Summary Here"""
                           ),
                           #dbc.Button("View details", color="secondary"),
                   ],
                  md=6,
               ),
              dbc.Col(
                 [
                     #html.H2("Graph"),
                     dcc.Graph(
                         figure=display_choropleth(df, "CA Counties"), style={'width': '70vh', 'height': '70vh'}
                            ),
                        ]
                     ),
                ]
            )
       ],
className="mt-4",
)

def Homepage():
    layout = html.Div([
    nav,
    body
    ])
    return layout
