import pyautogui as pt
import pyperclip as pc

from pynput.mouse import Button, Controller
from time import sleep

pt.FAILSAFE = True
mouse = Controller()

# Global variables
new_msg_received = False

startMsg = "Witaj w elektronicznym systemie automatycznej rejestracji do Pani Doktor Zabek. Wybierz jedna z dostepnych opcji:"
choice1 = "1. Umow wizyte."
choice2 = "2. Sprawdz termin swojej wizyty."
choice3 = "0. Zakoncz."

copy_path = "Images/copy_dark.png"
attachment_path = "Images/attachment_dark.png"
x_path = "Images/x_dark.png"
unread_path = "Images/unread_dark.png"

get_message_error = "No response found"
find_att_error = "Undefined UI error"
close_reply_field_error = "Cannot close the reply field"
find_new_msg_error = "No new messages found"

def go_to_img(img_path, error_msg, clicks, offset_x = 0, offset_y = 0):
    pos = pt.locateCenterOnScreen(img_path, confidence = .8)
    
    if pos is None:
        print(error_msg)
        return 0
    else:
        pt.moveTo(pos, duration = .1)
        pt.moveRel(offset_x, offset_y, duration = .1)
        pt.click(clicks = clicks, interval = .1)

def get_message():
    go_to_img(attachment_path, find_att_error, 0, offset_y = -65)
    mouse.click(Button.left, 3)
    pt.rightClick()

    copy = go_to_img(copy_path, get_message_error, 1)
    sleep(.5)
    return pc.paste() if copy != 0 else 0

def send_message(msg):
    go_to_img(attachment_path, find_att_error, 2, offset_x = 100)
    pt.typewrite(msg, interval = .001)
    pt.typewrite("\n")

def open_new_msg(img_path):
    pos = pt.locateCenterOnScreen(img_path, confidence = .8)
    
    if pos is  None:
        print(find_new_msg_error)
        return 0
    else:
        pt.moveTo(pos, duration = .1)
        pt.moveRel(-50, 0, duration = .1)
        pt.click(clicks = 1, interval = .1)
        new_msg_received = True
        return new_msg_received
        

def close_reply_field():
    go_to_img(x_path, close_reply_field_error, 1)

def book_term():
    send_message("Booking a term...")

def change_term():
    send_message("Changing term...")

def main():
    while(1):
        sleep(3)
        new_msg_received = open_new_msg(unread_path)   
        while(new_msg_received):
            send_message(startMsg)
            send_message(choice1)
            send_message(choice2)
            send_message(choice3)
            sleep(10)
            user_message = get_message()

            while((user_message != "1") or (user_message != "2") or (user_message != "0")):
                close_reply_field()
                send_message("Nie rozumiem co mam zrobic, wybierz jedna z podanych opcji...")
                sleep(10)
                user_message = get_message()
                
            if user_message == "1":
                book_term()
            elif user_message == "2":
                change_term()
            elif user_message == "0":
                send_message("Dziekuje za kontakt i zycze milego dnia. Wyslij kolejna wiadomosc, aby zaczac od nowa.")
        new_msg_received = False


if __name__ == '__main__':
    main()