import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, path='/')

heading = html.H4(
    "Bienvenu sur Twinder",
    className="bg-primary text-white p-2", style={'textAlign': 'center'}
)

user_id = html.Div(
    [dbc.Label("Trouve le twittos qui te convient !",html_for="User")],
    className="mt-2",
)


control_panel = dbc.Card(
    dbc.CardBody(
        [user_id],
        className="bg-light",
    )
)

button = dbc.Button(
    id='log',
    children="Login",
    n_clicks=0,
    href="login",
    size="lg",
    className="mt-2",
)

layout = html.Div(
    [heading,
    dbc.Row([dbc.Col(control_panel, md = 4)],justify = "center"),
    dbc.Row([dbc.Col(button,md=4)],justify="center"),]
)

"""layout = dcc.Markdown('''
# Bienvenue sur Twinder !

[Cliquez ici pour vous connecter](login).
''')"""
