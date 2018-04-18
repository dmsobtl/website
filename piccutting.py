# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 18:07:30 2017

@author: P7XXDMX
"""

#coding:utf-8
import hashlib
import time
from PIL import Image

im=Image.open('captcha.gif')
#im = Image.open("captcha.gif")
#(将图片转换为8位像素模式)
im.convert("P")
im.show()

#測試代碼
#for xx in range(30):
#    for yy in range(30):
#        pix=im.getpixel((xx,yy))
#        print pix

#打印颜色直方图
#很坐標是0-255,表示P模式下面的0-255種顏色，縱坐標是表示圖片中對應的每個顏色的像素個數
print (im.histogram())
his=im.histogram()

#dict 創建一個字典，來保存圖片裏面的像素分布 
values={}

for i in range(256):
    values[i]=his[i]

#給dict排序，然後保存前10名
lists=sorted(values.items(),key=lambda x:x[1],reverse=True)[:10]

#l[0]是0-255中的一樣顏色，比如255是白色，l[1] 是對應的像素的個數
for l in lists:
    print( l[0],l[1])

#創建pic2
#以一個像素8bit的，大小是Im.size  背景顏色是255 白色
im2=Image.new("P",im.size,255)

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix=im.getpixel((y,x))
        #220 227 解釋一下 就是將紅色的像素 變成黑色
        if pix ==220 or pix==227:
            im2.putpixel((y,x),0)

#現在這張圖片是一張黑白的圖片，黑色是字符，白色是背景
#im2.show()
#嘗試着保存成jpg格式，結果失敗 原因 cannot write mode P as JPEG
#image = Image.new('RGB', (width, height), (255, 255, 255))
#好像這樣的才可以  
#記得以前數字圖像這門課好像講過  但是全tmd忘了
im2.save('222.gif','gif')

#得到單個的字符，纵向切割圖片
#size[0]是長
#size[1]是寬

#縱向遍歷圖片 找到每個字符的起始的位置
inletter = False
foundletter=False
start = 0
end = 0
letters = []

for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix=im2.getpixel((y,x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start,end))

    inletter=False
print (letters)


#將分割後的圖片保存
count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
    m.update("%s%s"%(time.time(),count))
    im3.save("./%s.gif"%(m.hexdigest()))
    count += 1
