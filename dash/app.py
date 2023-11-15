# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_ag_grid as dag
import app_objects as ao
# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Icons
rightswipe_icon = DashIconify(icon="streamline:tinder", width=100)
leftswipe_icon = DashIconify(icon="streamline:disable-heart", width=100)

# Initialize the app - incorporate a Dash Mantine theme
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = Dash(__name__, external_stylesheets=external_stylesheets)

dag.AgGrid(
    className="ag-theme-alpine-dark",
    # other props
)

# App layout
app.layout = dmc.Stack(
        spacing="xs",
        children=[
            dmc.Title('Twinder'),
            dmc.Card(    
                withBorder=True,
                shadow="sm",
                radius="md",
                style={"width": 350},
                children=[
                    dmc.Stack(
                        children=[
                            dmc.Text("Tu as le choix, on prend les deux"),
                            dmc.SimpleGrid(
                                cols=2,
                                children=[
                                    ao.left_swipe_btn,
                                    ao.right_swipe_btn
                                ]
                            )
                        ]
                    )
                ]
            )
        ],
        align="center"
    )

# Run the App
if __name__ == '__main__':
    app.run(debug=True)
