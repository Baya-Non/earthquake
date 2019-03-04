# coding: utf-8
# python version 3.6.0
from bs4 import BeautifulSoup
import requests
import csv
import lxml
import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta

######################################################################
# crawling.pyを用いてディレクトリに獲得したページのソースをスクレイピングします。           #
# 出力はutf-8またはcp932でcsv形式で出力します。                             	 #
# 読み込むファイルのパスは任意で指定してください                                 	 #
######################################################################

# delay_sumはグローバル関数とするので初期値をあらかじめ与えておきます
delay_sum = 0

# 任意のurlからコンテンツとしてデータを取得します
def scraping(file_name,list_name):
	
	# bsを用いてhtmlデータの獲得
	with open(file_name, 'rb') as f:
		response = f.read()
	f.close
	print(list_name)
	soup = BeautifulSoup(response,"html.parser")
	# dataにクロールしたデータを格納します。
	data = []
	data1 = []

	# <p class="v2_listDelayDataDay v2_boxSp v2_noWide">09月20日（水）</p>
	# から情報を抜き出す。
	for a in soup.find_all('ul', class_='subMenu'):
		data.append(a.text)

	#print(data[0])
	data1 = data[0].splitlines()
	for i in range(len(data1)):
		if data1[i] != '':
			if data1[i][26] == ' ':
				str_list=list(data1[i])
				str_list[26] = str_list[26].replace(' ', '')
				data1[i] = "".join(str_list)
			
			if data1[i][37] == ' ':
				str_list=list(data1[i])
				str_list[37] = str_list[37].replace(' ', '')
				data1[i] = "".join(str_list)

			if data1[i][36] == ' ':
				str_list=list(data1[i])
				str_list[36] = str_list[36].replace(' ', '')
				data1[i] = "".join(str_list)

			data1[i] = data1[i].split()
			#print(data1[i])
	
	data2 = [x for x in data1 if x]

	shape_data = Shaping(data2)

	file_pass = './Scraping/{}.csv'.format(list_name)
	with open(file_pass, 'w') as f:
		writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
		writer.writerows(data2)     # list（1次元配列）の場合

	csv_pass = './csv/today.csv'
	with open(csv_pass, 'a') as f:
		writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
		writer.writerows(shape_data) 





def Shaping(data):
	shape_data = []
	l = list(range(9))
	print(shape_data)
	del data[:3]
	for i in range(len(data)):
		child_list = []

		#日付
		date_str = data[i][0] + data[i][1].zfill(2) + data[i][2].zfill(2)
		datetime_formatted1 = datetime.strptime(date_str, "%Y%m%d")
		date = datetime_formatted1.date()

		#時間
		t1_spilit = data[i][4].split(".")
		t1 = t1_spilit[0]
		t2 = t1_spilit[1]
		time_str = data[i][3] + ":" + t1.zfill(2)

		datetime_formatted2 = datetime.strptime(time_str, "%H:%M:%S")
		time = datetime_formatted2.time()

		#longitude 英語で経度(60進法に変換)
		longitude = data[i][5]
		Longitude_sp = longitude.split("°")
		x_1 = int(Longitude_sp[0])
		Longitude_sp = Longitude_sp[1].split(".")
		x_2 = int(Longitude_sp[0])
		Longitude_sp = Longitude_sp[1].split("'")
		x_3 = int(Longitude_sp[0])

		calc_logitude = x_1 + x_2/60 + x_3/3600

		#latitude 英語で緯度(60進法に変換)
		latitude = data[i][6]
		latitude_sp = latitude.split("°")
		y_1 = int(latitude_sp[0])
		latitude_sp = latitude_sp[1].split(".")
		y_2 = int(latitude_sp[0])
		latitude_sp = latitude_sp[1].split("'")
		y_3 = int(latitude_sp[0])

		calc_latitude = y_1 + y_2/60 + y_3/3600

		deep = int(data[i][7])
		if(str(data[i][8]) == '-'):
			magnitude = 0
		else:
			magnitude = data[i][8]

		location = str(data[i][9])

		#print(str(date) + " " + str(time) + " " + str(calc_logitude) + " " + str(calc_latitude) + " " + str(deep) + " " +str(magnitude) + " " +location)
		
		child_list.append(date)
		child_list.append(time)
		child_list.append(calc_logitude)
		child_list.append(calc_latitude)
		child_list.append(deep)
		child_list.append(magnitude)
		child_list.append(location)

		shape_data.append(child_list)

	#for i in range(len(shape_data)):
		#print(shape_data[i])

	return shape_data

if __name__ == '__main__':

	today = datetime.today()
	first_day = today.replace(day=1)
	day = datetime.strftime(first_day, '%Y%m%d')

	# プログラムが置いてあるディレクトリ上のCrawlingディレクトリにスクレイピングしたCSVファイルを書き込みます
	file_pass = './Crawling/'

	b_day = 500

	# ファイルを開いてCSVファイルに書き込んでいきます。
	for i in range(1,b_day):
		file_name = file_pass + str(day) + '.html'
		print(file_name)
		scraping(file_name,str(day))
		
		first_day = first_day - timedelta(days=1)
		day = datetime.strftime(first_day, '%Y%m%d')