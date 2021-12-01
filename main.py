import pyautogui as pt
import pyperclip

from pynput.mouse import Button, Controller
from time import sleep

pt.FAILSAFE = True
MOUSE = Controller()

# Do obrazu
def to_img(img_path, clicks, offset_x = 0, offset_y = 0):
    pos = pt.locateCenterOnScreen(img_path, confidence = .8)

    if pos is None:
        print("Image {} not found...".format(img_path))
        return 0
    else:
        pt.moveTo(pos, duration = 1)
        pt.moveRel(offset_x, offset_y, duration = .5)
        pt.click(clicks = clicks, interval = .1)