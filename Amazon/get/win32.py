from PIL import Image
from PIL import ImageGrab
import time

time.sleep(2)
size = (540, 225, 1428, 594)
# img = ImageGrab.grab(size)
# img.save("cut.jpg")
# img.show()

def screenshot(size, file_path):
    img = ImageGrab.grab(size)
    img.save(file_path)
    img.show()

screenshot(size, "cut.jpg")