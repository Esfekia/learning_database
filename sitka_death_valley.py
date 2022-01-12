import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_weather_data(filename,dates,highs,lows,date_index, high_index, low_index):
	"""Get the highs and lows from the data file."""
	
	with open (filename) as f:
		reader = csv.reader(f)
		header_row =next(reader)

		#Get dates, high and low temperatures from this file.
		for row in reader:
			current_date = datetime.strptime(row[date_index],'%Y-%m-%d')
			try:
				high = int(row[high_index])
				low = int(row[low_index])
			except ValueError:
				print (f"Missing data for {current_date}")
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)

#Get weather data for Sitka:
filename = 'data/sitka_weather_2018_simple.csv'
dates,highs,lows =[],[],[]
get_weather_data(filename, dates,highs,lows,date_index=2, high_index=5, low_index=6)

#Plot Sitka Weather Data:

plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.ylim([20, 130])
ax.plot(dates,highs,c='red', alpha =0.5)
ax.plot(dates,lows,c='blue', alpha =0.5)
plt.fill_between(dates,highs,lows,facecolor ='blue', alpha =0.1)


#Get weather data for Death Valley, CA:
filename = 'data/death_valley_2018_simple.csv'
dates,highs,lows =[],[],[]
get_weather_data(filename, dates,highs,lows,date_index=2, high_index=4, low_index=5)

#Plot Death Valley, CA Data:
ax.plot(dates,highs,c='red', alpha =0.3)
ax.plot(dates,lows,c='blue', alpha =0.3)
plt.fill_between(dates,highs,lows,facecolor ='blue', alpha =0.1)

#Format plot.
plt.title("Daily high and low temperatures Sitka vs Death Valley - 2018", fontsize=14)
plt.xlabel('', fontsize =16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize =16)
plt.tick_params(axis ='both',which = 'major', labelsize =16)

plt.show()