import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open (filename) as f:
	reader = csv.reader(f)
	header_row =next(reader)
	#for index, column_header in enumerate(header_row):
		#print (index,column_header)

	#Get dates and high temperatures from this file.
	dates,rainfall=[],[]
	for row in reader:
		current_date = datetime.strptime(row[2],'%Y-%m-%d')
		prcp= float(row[3])
		dates.append(current_date)
		rainfall.append(prcp)
	
	#Plot the high temperatures.
	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	ax.plot(dates,rainfall,c='blue', alpha =1)
	
	#Format plot.
	plt.title("Daily rainfall in Sitka - 2018", fontsize=24)
	plt.xlabel('', fontsize =16)
	fig.autofmt_xdate()
	plt.ylabel("Rainfall", fontsize =16)
	plt.tick_params(axis ='both',which = 'major', labelsize =16)

	plt.show()