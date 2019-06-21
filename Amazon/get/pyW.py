import win32gui
import win32con
import win32api

# 鼠标单击事件
#鼠标定位到(30,50)
win32api.SetCursorPos([392,50])
#执行左单键击，若需要双击则延时几毫秒再点击一次即可
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


from pymouse import PyMouse
from pykeyboard import PyKeyboard
m = PyMouse()
k = PyKeyboard()
k.type_string('Hello, World!')
