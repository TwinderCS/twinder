import dash
from dash import html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, State, ctx, callback, dcc


dash.register_page(__name__)


user_data = {
    'user_id': range(1, 101),
    'name': [f'User {i}' for i in range(1, 101)],
    'age': [20 + i % 10 for i in range(1, 101)],
    'bio': [f'This is a bio of User {i}' for i in range(1, 101)]
}
users_df = pd.DataFrame(user_data)

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def display_user_profile(user):
    return html.Div([
        html.H3(user['name']),
        html.P(f"Age: {user['age']}"),
        html.P(user['bio'])
    ])

user_index = 0

layout = html.Div([
    dcc.Store(id='user-index', data=user_index),
    html.Div(id='user-profile', children=display_user_profile(users_df.iloc[user_index])),
    dbc.Button("Yes", id='yes-button', color="success", className="mr-2"),
    dbc.Button("No", id='no-button', color="danger")
])

@callback(
    Output('user-profile', 'children'),
    Output('user-index', 'data'),
    Input('yes-button', 'n_clicks'),
    Input('no-button', 'n_clicks'),
    State('user-index', 'data'),
)
def update_user_profile(yes_clicks, no_clicks, current_index):
    new_index = (current_index + 1) % len(users_df)

    if yes_clicks and new_index < 50:
        matched_user = users_df.iloc[current_index]
    return display_user_profile(users_df.iloc[new_index]), new_index

if __name__ == '__main__':
    app.run_server(debug=True)

    