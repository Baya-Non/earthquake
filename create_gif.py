from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, date, timedelta

read_img_path = "./png/"
im = []

today = datetime.today()
first_day = today.replace(day=1)
first_day = first_day - timedelta(days=1)
day = datetime.strftime(first_day, '%Y-%m-%d')

for i in range(1,300):
	png = read_img_path + str(day)+".png"
	print(png)
	img = Image.open(png)
	draw = ImageDraw.Draw(img)
	# font = ImageFont.truetype(<font-file>, <font-size>)
	font = ImageFont.truetype("Arial Bold.ttf", 100)
	# draw.text((x, y),"Sample Text",(r,g,b))
	draw.text((40, 40),str(day),font=font,fill=(0,0,0))
	im.append(img)
	first_day = first_day - timedelta(days=1)
	day = datetime.strftime(first_day, '%Y-%m-%d')

im[0].save('pillow_imagedraw3.gif',
               save_all=True, append_images=im[1:], optimize=False, duration=400, loop=0)