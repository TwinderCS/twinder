from dash import Dash, dcc, html, Input, Output, State, ctx,callback
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

heading = html.H4(
    "Twinder, l'application qui réunit passion et amour", className="bg-primary text-white p-2", style={'textAlign': 'center'}
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


button = dbc.Button(
    id='submit',
    children="Submit",
    n_clicks=0,
    size="lg",
    className="mt-2",
)

app.layout = html.Div(
    [heading,dbc.Row([dbc.Col(control_panel, md = 4)],justify = "center"), dbc.Row([dbc.Col(button,md=4)],justify="center"),
    html.Div(id='my-output')]
)

@callback(
    Output(component_id='my-output', component_property='children'),
    #Input(component_id='user', component_property='value'),
    Input(component_id="submit", component_property="n_clicks"),
    State(component_id="user",component_property="value")
)
def update_output_div(__,name):
    button_clicked = ctx.triggered_id
    if button_clicked == 'submit':
        return f'Output: {name}'


if __name__ == '__main__':
    app.run(debug=True)