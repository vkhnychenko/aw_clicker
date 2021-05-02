import pyautogui
import time
import pytesseract
import pyscreenshot as ImageGrab
import cv2
import numpy as np

mine = ['mine2.png', 'mine3.png']
claim = ['claim4.png', 'claim5.png', 'claim6.png']
approve = ['approve.png']
hub = ['hub3.png', 'hub4.png']

def click(img_list):
    for img in img_list:
            obj = pyautogui.locateCenterOnScreen(img)
            if obj:
                x, y = obj
                pyautogui.click(x, y)


if __name__ == '__main__':
    while True:
        time.sleep(1)
        print('mine')
        click(mine)
        print('claim')
        click(claim)
        print('approve')
        click(approve)
        print('hub')
        click(hub)
            
      
