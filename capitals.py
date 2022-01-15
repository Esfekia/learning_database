import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data.
filename = 'data/capitals.topo.json'
with open (filename) as f:
	all_cp_data = json.load(f)

all_cp_dicts=all_cp_data
lons,lats,hover_texts =[],[],[]
for cp_dicts in all_cp_dicts['objects']['capitals']:
	lons.append(cp_dicts['geometries']['coordinates'][0])
	lats.append(cp_dicts['geometries']['coordinates'][1])
	hover_texts.append(cp_dicts['properties']['capital'])

#Map the earthquakes.
data = [{
	'type':'scattergeo',
	'lon':lons,
	'lat':lats,
	'text': hover_texts,
	'marker':{
		'size': [5],
		#'color': mags,
		#'colorscale': 'plasma',
		#'reversescale':True,
		#'colorbar':{'title':'Magnitude'},
	},
}]
my_layout = Layout(title="Capital Cities")

fig ={'data':data, 'layout':my_layout}
offline.plot(fig, filename ='capital_cities.html')