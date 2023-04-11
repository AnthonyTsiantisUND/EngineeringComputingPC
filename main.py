import plotly.io as pio
import plotly.express as px
gapminder_df = px.data.gapminder()
fig = px.choropleth(gapminder_df, locations='iso_alpha', color='lifeExp',
                    hover_name='country', animation_frame='year', range_color=[10, 100])
pio.write_html(fig, file='index.html', auto_open=True, full_html=True) # creates one html page with the viz embedded