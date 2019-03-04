# coding: utf-8
# python version 3.6.0
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta


#####################################################################
# 気象庁から各日付の地震データのページをクローリングします。                  	   	#
# 出力はhtml形式で出力します。                    	         	#
#####################################################################

# クラスの宣言を行います。
# クラスの練習も兼ねてクラスで作成します。
class Crawling:
	
	# __init__は各クラス定義から個々のオブジェクトを作るときにそれを初期化するメゾットに付けられた特殊名
	# self引数は、作られたオブジェクト自体を参照することを示す。
	# ※クラス定義で__init()__を定義するときは第一引数をselfでなければならない。
	def __init__(self):
		print("open Crawling program file")
		super(Crawling, self).__init__()

	def MakeHTML():
		# 日にちのフォーマット設定
		today = datetime.today()
		first_day = today.replace(day=1)
		day = datetime.strftime(first_day, '%Y%m%d')

		#設定した現在から任意の日数までデータをクロールします。
		b_day = 500

		# リスト型lineの確保されているリスト数の長さ分forを回します。
		for i in range(1,b_day):
			print(str(day))
			# 任意のurlを取得してresponseにurlのサイトデータを格納していきます。
			url = 'http://www.data.jma.go.jp/svd/eqev/data/daily_map/{}.html'.format(str(day))
			save_pass = './Crawling/'
			response = requests.get(url)
			soup = BeautifulSoup(response.content, 'html.parser')

			# 書き込み処理
			fout = open(save_pass + str(day) + '.html', mode = 'wb')
			fout.write(response.content)
			fout.close()

			# クローリングする際、一秒時間を空けます。
			time.sleep(1)

			first_day = first_day - timedelta(days=1)
			day = datetime.strftime(first_day, '%Y%m%d')

# mainからCrawlingクラスのMakeHTML関数を呼び出します。
if __name__ == '__main__':

	Crawling.MakeHTML()
