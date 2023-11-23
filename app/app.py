"""
Code responsible for rendering the app and calling the database to interact with the user.
"""

import sys
import dash
from dash import Dash, html, Input, Output, State, callback, dcc
import dash_bootstrap_components as dbc
import pandas as pd
sys.path.append("metrics_handlers")
from metrics import get_closest_users, get_random_tweet_user

LAYOUT_ID = "login"

app = Dash(__name__,external_stylesheets=[dbc.themes.SPACELAB])

def user_data_creation(username, n = 10):
    """
    Creates a dataframe with the n closest users.
    string, int -> dataframe
    """
    user_array = get_closest_users(username, n)
    user_data = {
        'user_id_closest' : [user_array[i] for i in range(n)],
    }
    data = pd.DataFrame(user_data)
    return data
user_id = html.Div(
    [dbc.Label("User ID",html_for="User"), dbc.Input(id ="user_state", type="text",value="")],
    className="mt-2",
)

users_df = user_data_creation("scotthamilton")
"""
Initializing a default user dataframe
"""

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

def serve_layout():
    """
    Wrapper that renders the different pages of the app
    None -> html.Div
    """
    if LAYOUT_ID == "login":
        return html.Div(
            [heading,
            dbc.Row([dbc.Col(control_panel, md = 4)],justify = "center"),
            dbc.Row([dbc.Col(button,md=4)],justify="center"),
            html.Div(id='my-output'),
            html.Div(id="yes-button"),
            html.Div(id="no-button"),
            html.Div(id="user-index"),
            html.Div(id="user-priofile")]
        )
    if LAYOUT_ID == "feed":
        global users_df
        name_d = ""
        with open("app/cookie.txt", "r", encoding="utf-8") as cookie:
            name_d = cookie.readline()
            users_df = user_data_creation(name_d)
        yes_button = dbc.Button("Yes", id='yes-button', color="success", className="mr-2", style={"border-radius": "50%"})
        no_button = dbc.Button("No", id='no-button', color="danger", style={"border-radius": "50%"})
        display =  html.Div([
            dcc.Store(id='user-index', data=user_index),
            html.Div(id='user-profile', children=display_user_profile(users_df.iloc[user_index])),
            html.Div([yes_button, no_button], className='d-flex justify-content-center')
            ], className='mt-2', style={'textAlign': 'center'})
        display_panel = dbc.Card(
            dbc.CardBody(
                [display],
                className="bg-light",
                )
        )       
        return html.Div(
            [heading,
            dbc.Row([dbc.Col(display_panel, md = 4)],justify = "center"),]
        )
    return html.H1("AAAA")

heading = html.H4(
    "Twinder, l'application qui réunit passion et amour",
    className="bg-primary text-white p-2", style={'textAlign': 'center'}
)


@callback(
    Output(component_id='my-output', component_property='children', allow_duplicate=True),
    Input(component_id="submit", component_property="n_clicks"),
    State(component_id="user_state",component_property="value"),
    prevent_initial_call = True
)
def update_output_div(n_clicks,name):
    """
    Update the output with the current text when the button is clicked
    """
    global LAYOUT_ID
    if n_clicks > 0:
        with open("app/cookie.txt", "w", encoding="utf-8") as cookie:
            cookie.write(name)
        LAYOUT_ID = "feed"
        app.run(debug=True)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def display_user_profile(user):
    """
    Wrapper defining the layout of a user card.
    string(username) -> html.Div
    """
    return html.Div([
        html.H3(user["user_id_closest"]),
        html.P(get_random_tweet_user(user['user_id_closest']))
    ])

user_index = 0

@callback(
    Output('user-profile', 'children', allow_duplicate=True),
    Output('user-index', 'data', allow_duplicate=True),
    Input('yes-button', 'n_clicks'),
    Input('no-button', 'n_clicks'),
    State('user-index', 'data'),
    prevent_initial_call = True,
)
def update_user_profile(yes_button, no_button, current_index):
    """
    Callback function that retrieves the input of the yes/no buttons and returns the next profile.
    WIP: The buttons don't do anything now except switching to the next profile.
    callback.Input, callback.Input, callback.State -> html.Div, int 
    """
    new_index = (current_index + 1) % len(users_df)

    return display_user_profile(users_df.iloc[new_index]), new_index

app.layout = serve_layout

if __name__ == '__main__':
    app.run(debug=True)
