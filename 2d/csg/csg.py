# -*- coding: utf-8 -*-

def unionop(a, b):
    return a if a.sd < b.sd else b

def intersectop(a,b):
    # r = b if a.sd > b.sd else a
    # r.sd = a.sd if a.sd > b.sd else b.sd
    # return r
    return a if a.sd > b.sd else b

def subtractop(a,b):
    r = a
    r.sd = a.sd if a.sd > -b.sd else -b.sd
    return r


class Result:
    def __init__(self, sd,emssive):
        self.sd = sd
        self.emssive = emssive

import random
import math
from svpng import svpng

TWO_PI = 6.28318530718

def cicleSDF(x,y,cx,cy,r):
    ux = x -cx
    uy = y -cy
    return (ux**2 + uy**2)**0.5 - r

def scene(x,y):
    # r1 = Result(cicleSDF(x,y, 0.3, 0.3, 0.1),2.0)
    # r2 = Result(cicleSDF(x,y, 0.3, 0.7, 0.05),0.8)
    # r3 = Result(cicleSDF(x,y, 0.7, 0.5, 0.1),0.1)
    # return unionop(unionop(r1,r2),r3)
    a = Result(cicleSDF(x, y, 0.4, 0.5, 0.2), 1.0)
    b = Result(cicleSDF(x, y, 0.6, 0.5, 0.2), 0.5)
    #return unionop(a,b)
    #return  intersectop(a, b)
    return  subtractop(a,b)
    #return  subtractop(b, a)

step = 64
def trace(ox, oy, dx, dy):
    t = 0.0
    for i in range(step):
        r = scene(ox + dx *t, oy + dy*t)
        if r.sd < 0.0000001:
            return r.emssive
        t += r.sd;
        if t >= 2 :
            break
    return 0.0

times = 64
def sample(x, y):
    sum = 0.0
    for i in range(times):
        #a = TWO_PI*(random.randint(1,360)/360) #蒙地卡罗积分法
        #a = TWO_PI * i / times
        a = TWO_PI*(i + random.randint(1,1000000000)/1000000000)/times
        sum += trace(x, y, math.cos(a), math.sin(a));
    return sum/times

w = h = 512
color = []
for j in range(w):
    for i in range(h):
         x = sample(i/w, j / h)*255;
         x = int(x) if x < 255 else 255
         color.append(x)
         color.append(x)
         color.append(x)

f = open('D:\work\python\opengl\swatch.png', 'wb')
sv = svpng(f,w,h)
sv.save(color)
f.close()


