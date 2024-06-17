import dash_core_components as dcc
import dash_html_components as html
from layout import sanitization_df

layout = html.Div([
    html.Div([
        html.H1("Dashboard de Água Potável e Saneamento Básico"),
        html.Div([
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in sanitization_df['País'].unique()],
                value=['Afeganistão'],
                multi=True,
                style={'margin-bottom': '10px'}
            ),
        ], style={'padding': '10px'}),
        dcc.Graph(id='sanitization-graph', style={'height': '50vh'}),
        dcc.Graph(id='water-graph', style={'height': '50vh'})
    ], style={'max-width': '1200px', 'margin': 'auto'})
])
