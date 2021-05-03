import pyautogui
import time
import pytesseract
import pyscreenshot as ImageGrab
import cv2
import numpy as np

mine = ['data/mine2.png', 'data/mine3.png']
claim = ['data/claim4.png', 'data/claim5.png', 'data/claim6.png']
approve = ['data/approve.png']
hub = ['data/hub3.png', 'data/hub4.png']

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
            
      
