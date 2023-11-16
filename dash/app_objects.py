# Des objets que l'on va rappeler souvent dans l'application app.py pour ne pas avoir à les réécrire.
# Ils sont nommés "ao.<nom de l'objet>"


import dash_ag_grid as dag
import update_candidate as uc
from dash_iconify import DashIconify
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc


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
def update_left(n_clicks):
    return uc.main(-1, n_clicks)

@callback(
    Output("right-swipe-action", "children"),
    Input("right-swipe-icon", "n_clicks"),
)
def update_clicks(n_clicks):
    return uc.main(1, n_clicks)