# import libraries
import folium
import pandas as pd
import csv
from datetime import datetime, date, timedelta

 
def plot_earthquack(data_set):

	save_html_path = "./plot_html/"

	today = datetime.today()
	first_day = today.replace(day=1)
	day = datetime.strftime(first_day, '%Y-%m-%d')
	for k in range(1,500):
		print(day)
		
		lat1 = []
		lot1 = []
		locate1 = []
		magnitude1 = []
		day1 = []
		for j in range(len(data_set)):
			if str(data_set[j][0]) == str(day):
				lat1.append(float(data_set[j][2]))
				lot1.append(float(data_set[j][3]))
				magnitude1.append(abs(float(data_set[j][5])))
				locate1.append(str(data_set[j][6]))
				day1.append(str(data_set[j][0]))

		# Make a data frame with dots to show on the map
		data = pd.DataFrame({
		'lat':lot1,
		'lon':lat1,
		'name':locate1,
		'mag':magnitude1,
		'day':day1
		})

		
		#print(data)
		
		# Make an empty map
		m = folium.Map(location=[35.681236, 139.767125], tiles="Mapbox Bright",  zoom_start=5)
		
		for i in range(0,len(data)):
			if data.iloc[i]['mag'] >= 1.0 and data.iloc[i]['mag'] < 3.0:
				#folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(m)

				folium.CircleMarker([data.iloc[i]['lon'], data.iloc[i]['lat']],
					radius= 5 * data.iloc[i]['mag'],
					popup=data.iloc[i]['name'],
					color='#b7fffd',
					fill_color='#b7fffd'
					).add_to(m)

			if data.iloc[i]['mag'] >= 3.0 and data.iloc[i]['mag'] < 5.0:
			#folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(m)

				folium.CircleMarker([data.iloc[i]['lon'], data.iloc[i]['lat']],
					radius= 5 * data.iloc[i]['mag'],
					popup=data.iloc[i]['name'],
					color='#004cff',
					fill_color='#004cff'
					).add_to(m)

			if data.iloc[i]['mag'] >= 5.0 and data.iloc[i]['mag'] < 6.0:
				#folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(m)

				folium.CircleMarker([data.iloc[i]['lon'], data.iloc[i]['lat']],
					radius= 5 * data.iloc[i]['mag'],
					popup=data.iloc[i]['name'],
					color='#e66bff',
					fill_color='#e66bff'
					).add_to(m)

			if data.iloc[i]['mag'] >= 6.0 and data.iloc[i]['mag'] < 7.0:
				#folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(m)

				folium.CircleMarker([data.iloc[i]['lon'], data.iloc[i]['lat']],
					radius= 5 * data.iloc[i]['mag'],
					popup=data.iloc[i]['name'],
					color='#f90081',
					fill_color='#f90081'
					).add_to(m)

			if data.iloc[i]['mag'] >= 7.0:
				#folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(m)

				folium.CircleMarker([data.iloc[i]['lon'], data.iloc[i]['lat']],
					radius= 7 * data.iloc[i]['mag'],
					popup=data.iloc[i]['name'],
					color='#f91800',
					fill_color='#f91800'
					).add_to(m)

		first_day = first_day - timedelta(days=1)
		day = datetime.strftime(first_day, '%Y-%m-%d')

		# Save it as html
		m.save(save_html_path + str(day) + '.html')

def get_data():
	data = []
	with open('./csv/today.csv',  newline='') as f:
		dataReader = csv.reader(f)
		for row in dataReader:
			data.append(row)

	print(len(data))
	#del data[60:]
	#for i in range(len(data)):
		#print(data[i])
	return data

def main():
	data = get_data()
	plot_earthquack(data)


if __name__ == '__main__':
	main()