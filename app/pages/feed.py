import dash
from dash import html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, State, ctx, callback, dcc


dash.register_page(__name__)

<<<<<<< HEAD
#creation of a fake test dataset to be used by my app bc the AI dataset hasn't been downloaded yet 
=======
#creation of a fake test dataset to be used by my app bc the AI dataset hasn't been downloaded yet
>>>>>>> d10ff4a2cf6bb53cfa8e240869b5325fcc8ff7cd

user_data = {
    'user_id': range(1, 101),
    'name': [f'User {i}' for i in range(1, 101)],
    'age': [20 + i % 10 for i in range(1, 101)],
    'bio': [f'This is a bio of User {i}' for i in range(1, 101)]
}

#to create my interface im using the dash module from python and its functions

users_df = pd.DataFrame(user_data)

<<<<<<< HEAD
#to create my interface im using the dash module from python and its functions

=======
>>>>>>> d10ff4a2cf6bb53cfa8e240869b5325fcc8ff7cd
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#i need to create a graphic function showing off the pretendant profile after tking the original user id as an argument

def display_user_profile(user):
    return html.Div([
        html.H3(user['name']),
        html.P(f"Age: {user['age']}"),
        html.P(user['bio'])
    ])

user_index = 0

#im adjusting the layout so as to make it more beautiful or in the current extent at least acceptable

layout = html.Div([
    dcc.Store(id='user-index', data=user_index),
    html.Div(id='user-profile', children=display_user_profile(users_df.iloc[user_index])),
    dbc.Button("Yes", id='yes-button', color="success", className="mr-2"),
    dbc.Button("No", id='no-button', color="danger")
])

#im implementing a callback function which updates the page whenever the button yes or no is pushed. If the yes button is pushed, then the pretendant user id is put in an additional dataset

@callback(
    Output('user-profile', 'children'),
    Output('user-index', 'data'),
    Input('yes-button', 'n_clicks'),
    Input('no-button', 'n_clicks'),
    State('user-index', 'data'),
)

# i adjust my callback function so as to limit the suggestions to 50 profiles (to improve the quality of the AI generated selection)
<<<<<<< HEAD
=======

>>>>>>> d10ff4a2cf6bb53cfa8e240869b5325fcc8ff7cd
def update_user_profile(yes_clicks, no_clicks, current_index):
    new_index = (current_index + 1) % len(users_df)

    if yes_clicks and new_index < 50:
        matched_user = users_df.iloc[current_index]
    return display_user_profile(users_df.iloc[new_index]), new_index

if __name__ == '__main__':
    app.run_server(debug=True)

    
