import json

#Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open (filename) as f:
	all_eq_data = json.load(f)

all_eq_dicts=all_eq_data['features']

mags, lons,lats =[],[],[]
for eq_dicts in all_eq_dicts:
	mag = eq_dicts['properties']['mag']
	lon = eq_dicts['geometry']['coordinates'][0]
	lat = eq_dicts['geometry']['coordinates'][1]

	mags.append(mag)
	lons.append(lon)
	lats.append(lat)

print (mags[:10])
print (lons[:5])
print (lats[:5])
#print (len(all_eq_dicts))

#readable_file = 'data/readable_eq_data.json'
#with open (readable_file, 'w') as f:
	#json.dump(all_eq_data, f, indent =4)