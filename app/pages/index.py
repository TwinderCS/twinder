import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = dcc.Markdown('''
# Bienvenue sur Twinder !

[Cliquez ici pour vous connecter](login).
''')
