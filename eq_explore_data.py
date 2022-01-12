import json

#Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open (filename) as f:
	all_eq_data = json.load(f)

all_eq_dicts=all_eq_data['features']

mags =[]
for eq_dicts in all_eq_dicts:
	mag = eq_dicts['properties']['mag']
	mags.append(mag)

print (mags[:10])
#print (len(all_eq_dicts))

#readable_file = 'data/readable_eq_data.json'
#with open (readable_file, 'w') as f:
	#json.dump(all_eq_data, f, indent =4)