#!/usr/bin/python3
#coding:utf-8

#PIL的使用，图片的打开、获取大小、缩放、模糊以及存储
#生成字母验证码，暂时只知道该功能，暂时不研究原理，以后知道怎么用就行，如果有需要再研究

from PIL import Image,ImageFilter,ImageDraw,ImageFont

#打开一个文件，注意路径
im = Image.open('/users/alpha/Desktop/logo.png')

#获得头像的尺寸
w,h = im.size

print('original size:%s %s'%(w,h))

#图片缩放50%
im.thumbnail((w//2,h//2))
print('new size: %s %s'%(w//2,h//2))

#把缩放后的图像用jpeg格式保存
# im.save('/users/alpha/Desktop/thumbnail.jpg','jpeg')

#应用模糊滤镜
im.filter(ImageFilter.BLUR)
# im.save('blur.jpg','jpeg')

#---------我是华丽丽的分割线----------

#生成字母验证码
import random

#随机字母
def rndChar():
	return chr(random.randint(65,90))

#随机颜色1
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 60 * 4
height = 60

#创建图片
image = Image.new('RGB',(width,height),(255,255,255))

#创建font对象
font = ImageFont.truetype('/Library/Fonts/Arial.ttf',36)

#创建draw对象
draw = ImageDraw.Draw(image)

#填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())

#输出文字
for t in range(4):
	draw.text((60*t + 10,10),rndChar(),font=font,fill=rndColor2())

#模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')


