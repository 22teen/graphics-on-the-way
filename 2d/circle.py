# -*- coding: utf-8 -*-
import random
import math
from svpng.svpng import svpng

TWO_PI = 6.28318530718

def cicleSDF(x,y,cx,cy,r):
    ux = x -cx
    uy = y -cy
    return (ux**2 + uy**2)**0.5 - r

step = 10
def trace(ox, oy, dx, dy):
    t = 0.0
    for i in range(step):
        sd = cicleSDF(ox + dx *t, oy + dy*t, 0.5, 0.5, 0.1)
        if sd < 0.0000001:
            return 2.0
        t += sd;
        if t >= 2.0 :
            break
    return 0.0

times = 64
def sample(x, y):
    sum = 0.0
    for i in range(times):
        #a = TWO_PI*(random.randint(1,360)/360) #蒙地卡罗积分法
        #a = TWO_PI * i / times #分层 
        a = TWO_PI*(i + random.randint(1,360)/360)/times #抖动采样
        sum += trace(x, y, math.cos(a), math.sin(a));
    return sum/times

w = h = 256

color = []
for j in range(w):
    for i in range(h):
         x = sample(i/w, j / h)*255;
         x = int(x) if x < 255 else 255
         color.append(x)
         color.append(x)
         color.append(x)

# for j in range(512):
#     y = (j - 0)**2
#     for i in range(512):
#          x = (i - 0)**2
#          color.append((x + y)%256)
#          color.append((x + y)%256)
#          color.append(128)

# for j in range(512):
#     y = (j - 0)**2
#     for i in range(512):
#          x = (i - 0)**2
#          ss = (x + y)**0.5
#          ss = int(ss)
#          color.append(ss%256)
#          color.append(ss%256)
#          color.append(128)

f = open('D:\work\python\opengl\swatch.png', 'wb')
sv = svpng(f,256,256)
sv.save(color)
f.close()
