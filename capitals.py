import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data.
filename = 'data/capitals.topo.json'
with open (filename) as f:
	all_cp_data = json.load(f)

all_cp_dicts=all_cp_data
lons,lats,hover_texts =[],[],[]
for geometry in all_cp_dicts['objects']['capitals']['geometries']:
	
	lons.append(geometry['coordinates'][0])
	lats.append(geometry['coordinates'][1])
	hover_texts.append(geometry['properties'].get('city',""))

#Map the earthquakes.
data = Scattergeo(
	lat= lats,
	lon = lons,
	text = hover_texts,
	marker= dict(
		size =5)
		)
	
	
my_layout = Layout(title="Capital Cities")

fig ={'data':data, 'layout':my_layout}
offline.plot(fig, filename ='capital_cities.html')