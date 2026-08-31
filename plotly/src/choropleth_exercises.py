import plotly.graph_objs as go
import pandas as pd
import plotly.io as pio
pio.renderers.default = "browser"

usdf = pd.read_csv('plotly/data/2012_Election_Data')

def choropleth_map_vap_per_state():
    data = dict(type='choropleth',
            colorscale = 'Viridis',
            reversescale = True,
            locations = usdf['State Abv'],
            z = usdf['Voting-Age Population (VAP)'],
            locationmode = 'USA-states',
            text = usdf['State'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
            colorbar = {'title':"Voting-Age Population (VAP)"}
            )
    layout = dict(title = '2012 General Election Voting Data',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )
    choromap = go.Figure(data = [data],layout = layout)
    pio.show(choromap)

def main():
    print("Check the head of the DataFrame.")
    print(usdf.head())
    print("Create a plot that displays the Voting-Age Population (VAP) per state. If you later want to play around with other columns, make sure you consider their data type.")
    choropleth_map_vap_per_state()


if __name__ == "__main__":
    main()