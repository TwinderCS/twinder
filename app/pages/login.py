"""Module providing a function that send a message when the button is clicked"""
import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, State, ctx, callback, dcc

dash.register_page(__name__)

#app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

heading = html.H4(
    "Twinder, l'application qui réunit passion et amour",
    className="bg-primary text-white p-2", style={'textAlign': 'center'}
)

user_id = html.Div(
    [dbc.Label("User ID",html_for="User"), dbc.Input(id ="user", type="text",value="")],
    className="mt-2",
)

control_panel = dbc.Card(
    dbc.CardBody(
        [user_id],
        className="bg-primary text-white p-2",
    )
)

button = dbc.Button(
    id='submit',
    children="Submit",
    n_clicks=0,
    href="feed",
    size="lg",
    className="mt-2",
)

layout = html.Div(
    [heading,
    dbc.Row([dbc.Col(control_panel, md = 4)],justify = "center"),
    dbc.Row([dbc.Col(button,md=4)],justify="center"),
    html.Div(id='my-output')]
)

@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id="submit", component_property="n_clicks"),
    State(component_id="user_state",component_property="value"),
    prevent_initial_call=True    
)
def update_output_div(__,name):
    """
    Update the output with the current text when the button is clicked
    """
    print(name)
    button_clicked = ctx.triggered_id
    if button_clicked == 'submit':
        return f'Output: {name}'
