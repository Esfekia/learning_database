import geojson

#Explore the structure of the data.
filename = 'data/1_month.geojson'
with open (filename, 'rb') as f:
	all_eq_data = geojson.load(f)

readable_file = 'data/readable_1_month.json'
with open (readable_file, 'w') as f:
	geojson.dump(all_eq_data, f, indent =4)


#import geojson
#with open(path_to_file) as f:
#gj = geojson.load(f)
#features = gj['features'][0]