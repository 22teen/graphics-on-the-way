# -*- coding: utf-8 -*-
from svpng import svpng

color = []
colorTmp = []
for j in range(255):
 for i in range(255):
     color.append(i)
     color.append(j)
     color.append(128)

f = open('D:\work\python\opengl\swatch.png', 'wb')
sv = svpng(f,255,255)
sv.save(color)
f.close()
