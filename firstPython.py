# -*- coding: utf-8 -*-
# import struct
# try:
#     bytes('', 'ascii')
#     def strtobytes(x): return bytes(x, 'iso8859-1')
#     def bytestostr(x): return str(x, 'iso8859-1')
# except (NameError, TypeError):
#     # We get NameError when bytes() does not exist (most Python
#     # 2.x versions), and TypeError when bytes() exists but is on
#     # Python 2.x (when it is an alias for str() and takes at most
#     # one argument).
#     strtobytes = str
#     bytestostr = str
#
# print( int(1 == 1))
#
# bytess = strtobytes("\x89PNG\r\n\32\n")
# print(len(bytess))
#
# for i in range(5):
#     print(i)
#
# for i in bytess:
#     print(i)
#
# print(strtobytes("IHDR"))
# print(struct.pack('8B', 137, 80, 78, 71, 13, 10, 26, 10))
#
# print( 3 << 2)

#import png
#
# color = []
# colorTmp = []
# for j in range(255):
#  colorTmp.clear()
#  for i in range(255):
#      colorTmp.append(i)
#      colorTmp.append(j)
#      colorTmp.append(128)
#  color.append(colorTmp)
#
# f = open('D:\work\python\opengl\swatch.png', 'wb')
#w = png.Writer(255, 255)
# w.write(f, color) ; f.close()


# import png
# p = [[255,0,0, 0,255,0, 0,0,255],
#      [128,0,0, 0,128,0, 0,0,128]]
# f = open('D:\work\python\opengl\swatch.png', 'wb')
# w = png.Writer(3, 2)
# w.write(f, p) ; f.close()


# import png
# import numpy
#
# color = []
# colorTmp = []
# for j in range(255):
#  colorTmp.clear()
#  for i in range(255):
#      colorTmp.append([i,j,128])
#  color.append(colorTmp)
# png.from_array(color, 'RGB').save("D:\work\python\opengl\small_smiley.png")

try:
    bytes('', 'ascii')
    def strtobytes(x):
        return bytes(x, 'iso8859-1')
    def bytestostr(x):
        return str(x, 'iso8859-1')
except (NameError, TypeError):
    # We get NameError when bytes() does not exist (most Python
    # 2.x versions), and TypeError when bytes() exists but is on
    # Python 2.x (when it is an alias for str() and takes at most
    # one argument).
    strtobytes = str
    bytestostr = str


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
