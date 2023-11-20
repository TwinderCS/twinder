import dash
from dash import html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
import dash
from dash import Dash, html, Input, Output, State, ctx, callback, dcc

#creation of a fake test dataset to be used by my app bc the AI dataset hasn't been downloaded yet

user_data = {
    'user_id': range(1, 101),
    'name': [f'User {i}' for i in range(1, 101)],
    'age': [20 + i % 10 for i in range(1, 101)],
    'bio': [f'This is a bio of User {i}' for i in range(1, 101)]
}

#to create my interface im using the dash module from python and its functions

users_df = pd.DataFrame(user_data)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Improved user profile display using Bootstrap cards
def display_user_profile(user):
    return dbc.Card([
        dbc.CardBody([
            html.H4(user['name'], className='card-title'),
            html.P(f"Age: {user['age']}", className='card-text'),
            html.P(user['bio'], className='card-text')
        ])
    ], className='mb-3')
    
user_index=0

# Enhance buttons with Tinder-like style
yes_button = dbc.Button("Yes", id='yes-button', color="success", className="mr-2", style={"border-radius": "50%"})
no_button = dbc.Button("No", id='no-button', color="danger", style={"border-radius": "50%"})

app.layout = html.Div([
    dcc.Store(id='user-index', data=user_index),
    html.Div(id='user-profile', children=display_user_profile(users_df.iloc[user_index])),
    html.Div([yes_button, no_button], className='d-flex justify-content-center')
], className='container')

@callback(
    Output('user-profile', 'children'),
    Output('user-index', 'data'),
    Input('yes-button', 'n_clicks'),
    Input('no-button', 'n_clicks'),
    State('user-index', 'data'),
)

# i adjust my callback function so as to limit the suggestions to 50 profiles (to improve the quality of the AI generated selection)

def update_user_profile(yes_clicks, no_clicks, current_index):
    new_index = (current_index + 1) % len(users_df)

    if yes_clicks and new_index < 50:
        matched_user = users_df.iloc[current_index]
    return display_user_profile(users_df.iloc[new_index]), new_index

if __name__ == '__main__':
    app.run_server(debug=True)
