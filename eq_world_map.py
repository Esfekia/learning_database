import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open (filename) as f:
	all_eq_data = json.load(f)

all_eq_dicts=all_eq_data['features']

mags,lons,lats, hover_texts =[],[],[],[]
for eq_dicts in all_eq_dicts:
	mags.append(eq_dicts['properties']['mag'])
	lons.append(eq_dicts['geometry']['coordinates'][0])
	lats.append(eq_dicts['geometry']['coordinates'][1])
	hover_texts.append(eq_dicts['properties']['title'])

#Map the earthquakes.
#data = [Scattergeo(lon=lons, lat =lats)]
#We will use an alternative way to specify chart data for further customization
data = [{
	'type':'scattergeo',
	'lon':lons,
	'lat':lats,
	'text': hover_texts,
	'marker':{
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'plasma',
		'reversescale':True,
		'colorbar':{'title':'Magnitude'},
	},
}]
my_layout = Layout(title='Global Earthquakes')

fig ={'data':data, 'layout':my_layout}
offline.plot(fig, filename ='global_earthquakes.html')