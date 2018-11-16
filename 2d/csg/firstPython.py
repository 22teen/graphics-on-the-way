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

def min(a, b):
    return  a if a< b else b
def max(a, b):
    return a if a > b else b
def sqrt(a, b):
    return  (a**2 + b**2)**0.5
def clamp(a, min, max):
    return min if a <= min else max if a >= max else a

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
    return (ux + uy)**0.5 - r

def planeSDF(x,y, cx, cy, nx, ny):
    return (x - cy)*nx + (y - cy)*ny

def segmentSDF(x,y, ax, ay, bx,by):
    vx = x - ax
    vy = y - ay
    ux = bx - ax
    uy = by - ay
    t = (vx*ux + vy*uy)/(ux**2 + uy**2)
    t = clamp(t, 0, 1)
    dx =vx - ux*t
    dy = vy -uy*t
    return (dx**2 + dy**2)**0.5



def boxSDF(x,y,cx,cy, thetha, w,h):
    costheta = math.cos(thetha)
    sintheta = math.sin(thetha)
    bx = math.fabs((x - cx)*costheta + (y-cy)*sintheta)
    by = math.fabs(-(x-cx)*sintheta + (y-cy)*costheta)
    dx = bx - w
    dy = by - h
    ax = max(dx, 0)
    ay = max(dy, 0)
    return sqrt(ax,ay) + min(max(dx,dy), 0)

def capuleSDF(x,y, ax,ay, bx, by, r):
    return segmentSDF(x,y, ax,ay, bx,by) - r

def scene(x,y):
    #a = Result(cicleSDF(x, y, 0.5, 0.5, 0.2), 1.0)
    # b = Result(planeSDF(x, y, 0.0, 0.5, 0.0, 1.0), 0.8)
    # return  intersectop(a, b)
    #return  Result(capuleSDF(x, y, 0.3,0.3, 0.6, 0.6, 0.1), 1)
    return  Result(boxSDF(x, y, 0.5,0.5, TWO_PI/16.0, 0.3, 0.1), 0.7)

step = 8
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

times = 8
def sample(x, y):
    sum = 0.0
    for i in range(times):
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


