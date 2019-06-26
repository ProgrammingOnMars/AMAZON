import win32gui
import win32con
import win32api

from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
# click(1044, 183)
# time.sleep(2)
# click(82, 232)
# time.sleep(2)
# click(82, 286)
# time.sleep(2)
# click(275, 245)
# time.sleep(2)
# click(405, 295)
# time.sleep(2)
# k.type_string('19121131085')
#
#
# time.sleep(2)
# k.tap_key(13)
# time.sleep(10)
# handles2 = driver.window_handles
# print("handle\t, ",handles2)
# driver.switch_to.window(handles2[-1])
# time.sleep(10)
# #
# print(driver.page_source)
# driver.switch_to.frame("frset1")
# #_sweclient
#
#
#
# print(driver.page_source)

def click(x, y):
    # 鼠标单击事件
    #鼠标定位到(30,50)
    win32api.SetCursorPos([x,y])
    #执行左单键击，若需要双击则延时几毫秒再点击一次即可
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


    from pymouse import PyMouse
    from pykeyboard import PyKeyboard
    m = PyMouse()
    k = PyKeyboard()
    k.type_string('Hello, World!')

