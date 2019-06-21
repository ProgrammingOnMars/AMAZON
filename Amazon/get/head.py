import pymouse,pykeyboard,os,sys
from pymouse import *
from pykeyboard import PyKeyboard
import time

m = PyMouse()
k = PyKeyboard()

# m.click(int(297),int(53),int(-1),int(5)) #–鼠标点击
x_dim, y_dim = m.screen_size() # –获得屏幕尺寸
k.tap_key('G') # –模拟点击H键
print("x_dim, y_dim", x_dim, y_dim)
m.move(1444,400)
time.sleep(3)
m.click(1444,327,-1, 2) #–鼠标点击

k.type_string('Hello, World!')