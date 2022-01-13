import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
filename = 'data/MODIS_C6_1_Global_7d.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#Get the latitudes, longitudes and brightness from this file.
	lats,lons,bris = [],[],[]
	for row in reader:
		lat = float(row[0])
		lon = float (row[1])
		bri = float (row[2])

		if bri >= 350:
			lats.append(lat)
			lons.append(lon)
			bris.append(bri)

#Map the wildfire.
#data = [Scattergeo(lon=lons, lat =lats)]
#We will use an alternative way to specify chart data for further customization
data = [{
	'type':'scattergeo',
	'lon':lons,
	'lat':lats,
	'marker':{
		'size': [bri/50 for bri in bris],
		'color': bris,
		'colorscale': 'YlOrRd',
		'reversescale':False,
		'colorbar':{'title':'Brightness'},
	},
}]
my_layout = Layout(title='Global Wildfires, Last Week')

fig ={'data':data, 'layout':my_layout}
offline.plot(fig, filename ='global_wildfires.html')