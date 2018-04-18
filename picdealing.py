# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:32:52 2017

@author: P7XXDMX
"""

import os
from PIL import Image
from PIL import ImageEnhance
import re

Start_path = 'D:/HWDB1/chinese_hand_write_rec/src/'

list = os.listdir(Start_path)
#print list
count = 0
for pic in list:
    path = Start_path + pic
    print (path)
    im = Image.open(path)
    enh_con = ImageEnhance.Contrast(im)  
    contrast = 1.5  
    image_contrasted = enh_con.enhance(contrast)
    image_file = image_contrasted.convert('1')
    new_pic=re.sub(pic[:-4],pic[:-4]+'_new',pic)
    #print new_pic
    new_path=Start_path+new_pic
    image_file.save(new_path)
    


      
