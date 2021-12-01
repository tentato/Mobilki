import pyautogui as pt
import pyperclip as pc

from pynput.mouse import Button, Controller
from time import sleep

pt.FAILSAFE = True
mouse = Controller()

copy_path = "Images/copy_dark.png"
attachment_path = "Images/attachment_dark.png"
x_path = "Images/x_dark.png"
unread_path = "Images/unread_dark.png"

# Do obrazu
def go_to_img(img_path, clicks, offset_x = 0, offset_y = 0):
    pos = pt.locateCenterOnScreen(img_path, confidence = .8)

    if pos is None:
        print("Image {} not found...".format(img_path))
        return 0
    else:
        pt.moveTo(pos, duration = 1)
        pt.moveRel(offset_x, offset_y, duration = .3)
        pt.click(clicks = clicks, interval = .1)

def get_message():
    go_to_img(attachment_path, 0, offset_y = -65)
    mouse.click(Button.left ,3)
    pt.rightClick()

    copy = go_to_img(copy_path, 1)
    sleep(.5)
    return pc.paste() if copy != 0 else 0

def send_message(msg):
    go_to_img(attachment_path, 2, offset_x = 100)
    pt.typewrite(msg, interval = .1)
    pt.typewrite("\n")

def open_new_msg():
    go_to_img(unread_path, 3, offset_x = -30)

def main():
    while(1):
        sleep(3)
        open_new_msg()

        send_message("Test elo 123")

main()