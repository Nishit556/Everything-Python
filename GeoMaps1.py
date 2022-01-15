import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)
data = dict(type = 'choropleth',
            locations = ['AZ', 'CA', 'NY'],
            locationmode = 'USA-states',
            colorscale = 'Greens',
            text = ['text 1','text 2', 'text 3'],
            z = [1.0, 2.0, 3.0],
            colorbar = {'title': 'ColourBar Title goes here'})
layout = dict(geo={'scope' : 'usa'})
choromap = go.Figure(data=[data], layout=layout)
plot(choromap)



