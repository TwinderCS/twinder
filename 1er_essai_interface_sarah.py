import dash
from dash import html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd

#creating a test database to develop the interface although AI dataset hasn't been generated yet (17/11)

user_data = {
    'user_id': range(1, 101),
    'name': [f'User {i}' for i in range(1, 101)],
    'age': [20 + i % 10 for i in range(1, 101)],
    'bio': [f'This is a bio of User {i}' for i in range(1, 101)]
}
users_df = pd.DataFrame(user_data)

    
