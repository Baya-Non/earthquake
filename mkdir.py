import os.path

def Crawling_makeF():
	path = './Crawling/'
	if os.path.isdir(path) == False :
		os.mkdir("Crawling")

def Scraping_makeF():
	path = './Scraping/'
	if os.path.isdir(path) == False :
		os.mkdir("Scraping")

def csv_makeF():
	path = './csv/'
	if os.path.isdir(path) == False :
		os.mkdir("csv")

def plot_makeF():
	path = './plot_html/'
	if os.path.isdir(path) == False :
		os.mkdir("plot_html")

def png_makeF():
	path = './png/'
	if os.path.isdir(path) == False :
		os.mkdir("png")

if __name__ == '__main__':
	Crawling_makeF()
	Scraping_makeF()
	csv_makeF()
	plot_makeF()
	png_makeF()