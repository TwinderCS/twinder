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
    id="right-swipe-icon"
    ),
    dmc.Text(id="left-swipe-action")
])

right_swipe_btn = html.Div([
    dmc.ActionIcon(
        DashIconify(icon="streamline:tinder", width=100),
        size=150,
    id="right-swipe-icon"
    ),
    dmc.Text(id="right-swipe-action")
])