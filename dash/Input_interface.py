from dash import Dash, dcc, html, Input, Output, callback
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

heading = html.H4(
    "Twinder, l'application qui réunit passion et amour", className="bg-primary text-white p-2"
)

user_id = html.Div(
    [dbc.Label("User ID",html_for="User"), dbc.Input(id ="user", type="text",value="")],
    className="mt-2",
)

control_panel = dbc.Card(
    dbc.CardBody(
        [user_id],
        className="bg-light",
    )
)

app.layout = html.Div(
    [heading,dbc.Row([dbc.Col(control_panel, md = 4)])]
)

"""app.layout = html.Div(
    html.Br(),
    html.Div(id='my-output'))"""
#user interface object
"""app.layout = html.Div([
    html.H6("Twinder"),
    html.Div([
        "User ID: ",
        dcc.Input(id='my-input', value='', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])"""



"""@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='user', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'"""


if __name__ == '__main__':
    app.run(debug=True)
