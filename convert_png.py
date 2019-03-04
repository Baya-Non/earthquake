import os
import time
from selenium import webdriver
from datetime import datetime, date, timedelta


read_html_path = "./plot_html/"
save_img_path = "./png/"

today = datetime.today()
first_day = today.replace(day=1)
first_day = first_day - timedelta(days=1)
day = datetime.strftime(first_day, '%Y-%m-%d')

driver_path = "./chromedriver.exe"
delay=5

for i in range(1,500):
	fn = str(day)+".html"
	tmpurl='file://{path}/plot_html/{mapfile}'.format(path=os.getcwd(),mapfile=fn)
	print(tmpurl)
	driver = webdriver.Chrome(driver_path)
	driver.get(tmpurl)
	#Give the map tiles some time to load
	time.sleep(delay)

	save = save_img_path + str(day) + ".png"
	driver.save_screenshot(save)
	driver.quit()

	first_day = first_day - timedelta(days=1)
	day = datetime.strftime(first_day, '%Y-%m-%d')

