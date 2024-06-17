from dash.dependencies import Input, Output
import plotly.express as px
from layout import sanitization_data, water_data

def register_callbacks(app):
    @app.callback(
        [Output('sanitization-graph', 'figure'),
         Output('water-graph', 'figure')],
        [Input('country-dropdown', 'value')]
    )
    def update_graphs(selected_countries):
        sanitization_df = sanitization_data.get_total_population_data()
        water_df = water_data.get_data()

        filtered_sanitization = sanitization_df[sanitization_df['País'].isin(selected_countries)]
        filtered_water = water_df[water_df['País'].isin(selected_countries)]

        sanitization_fig = px.line(filtered_sanitization, x='Ano', y='Percentual de Saneamento', color='País',
                                   title='Serviços de Saneamento nos Países Selecionados',
                                   markers=True)

        water_fig = px.line(filtered_water, x='Ano', y='Percentual de Água', color='País',
                            title='Serviços de Água Potável nos Países Selecionados',
                            markers=True)

        return sanitization_fig, water_fig
