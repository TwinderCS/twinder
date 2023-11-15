# Des objets que l'on va rappeler souvent dans l'application app.py pour ne pas avoir à les réécrire.
# Ils sont nommés "ao.<nom de l'objet>"


from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_ag_grid as dag


# BOUTONS

left_swipe_btn = html.Div([
    dmc.ActionIcon(
        DashIconify(icon="streamline:disable-heart", width=100),
        size=150,
        id="left-swipe-icon",
        n_clicks=0,
    ),
    dmc.Text(id="left-swipe-action")
])

right_swipe_btn = html.Div([
    dmc.ActionIcon(
        DashIconify(icon="streamline:tinder", width=100),
        size=150,
        id="right-swipe-icon",
        n_clicks=0,
    ),
    dmc.Text(id="right-swipe-action")
])

@callback(
    Output("left-swipe-action", "children"),
    Input("left-swipe-icon", "n_clicks"),
)
def update_aaa(n_clicks):
    return f"AAA {n_clicks} times."

@callback(
    Output("right-swipe-action", "children"),
    Input("right-swipe-icon", "n_clicks"),
)
def update_clicks(n_clicks):
    return f"Clicked {n_clicks} times."