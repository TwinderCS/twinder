import dash
from dash import Dash, html, dcc
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, State, ctx, callback, dcc
import dash
from dash import html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, State, ctx, callback, dcc
import sys
sys.path.append("metrics_handlers")
from metrics import get_closest_users, get_random_tweet_user
from random import randint 


global layout_id
layout_id = "login"
print("bonjour")

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.QUARTZ])

def user_data_creation(username, n = 10):
    user_array = get_closest_users(username, n)
    user_data = {
        'user_id_closest' : [user_array[i] for i in range(n)]
    }
    users_df = pd.DataFrame(user_data)
    return users_df
user_id = html.Div(
    [dbc.Label("User ID",html_for="User"), dbc.Input(id ="user_state", type="text",value="")],
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

users_df = user_data_creation("scotthamilton")

def serve_layout():
    if layout_id == "login":
        print("login")
        return html.Div(
            [heading,
            dbc.Row([dbc.Col(control_panel, md = 4)],justify = "center"),
            dbc.Row([dbc.Col(button,md=4)],justify="center"),
            html.Div(id='my-output')]
        )
    if layout_id == "feed":
        global users_df
        print("feed")
        name_d = ""
        with open("app/cookie.txt", "r") as cookie:
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
    print(name)
    global layout_id
    if n_clicks > 0:
        with open("app/cookie.txt", "w") as cookie:
            cookie.write(name)
        layout_id = "feed"
        print("AAAAAA")
        app.run(debug=True)


#to create my interface im using the dash module from python and its functions

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#i need to create a graphic function showing off the pretendant profile after tking the original user id as an argument

def display_user_profile(user):
    return html.Div([
        html.H3(user["user_id_closest"]),
        html.P(f"Age: {randint(15,30)}"),  #html.P(f"Age: {user['age']}"),
        html.P(get_random_tweet_user(user['user_id_closest'])) #html.P(user['bio'])
    ])

user_index = 0

#im adjusting the layout so as to make it more beautiful or in the current extent at least acceptable
#im implementing a callback function which updates the page whenever the button yes or no is pushed. If the yes button is pushed, then the pretendant user id is put in an additional dataset

@callback(
    Output('user-profile', 'children', allow_duplicate=True),
    Output('user-index', 'data', allow_duplicate=True),
    Input('yes-button', 'n_clicks'),
    Input('no-button', 'n_clicks'),
    State('user-index', 'data'),
    prevent_initial_call = True
)


# i adjust my callback function so as to limit the suggestions to 50 profiles (to improve the quality of the AI generated selection)


def update_user_profile(yes_clicks, no_clicks, current_index):
    new_index = (current_index + 1) % len(users_df)

    if yes_clicks and new_index < 50:
        matched_user = users_df.iloc[current_index]
    return display_user_profile(users_df.iloc[new_index]), new_index


app.layout = serve_layout

if __name__ == '__main__':
    app.run(debug=True)