import cv2
import pyautogui
import time
import numpy as np
from collections.abc import MutableMapping
from datetime import datetime
def startCapture(filext = '',interval=1,xstart=0,ystart=0,width=0,height=0):
    now = datetime.now()
    dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
    while True:
        dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
        # if period==-1:
        #     pass
        # else:
        #     period -= 1
        filename = f"{dt_string}.png"
        screen = pyautogui.screenshot()
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
        if width == 0 or height == 0:
            height, width, _ = screen.shape
        filename_with_extension = filext+filename
        screen = screen[xstart:xstart+width][ystart:ystart+height]
        cv2.imwrite(filename_with_extension, screen)
        time.sleep(interval)

def startCapture_NEW(filext = '',interval=1,xstart=0,ystart=0,width=0,height=0):
    now = datetime.now()
    dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
    filename = f"{dt_string}.png"
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    if width == 0 or height == 0:
        height, width, _ = screen.shape
    filename_with_extension = filext+filename
    screen = screen[xstart:xstart+width][ystart:ystart+height]
    cv2.imwrite(filename_with_extension, screen)
    time.sleep(interval)

#startCapture('C:/Users/ishit/Desktop/DSS Server/Capture/', 1, 10, 0, 0, 0, 0)
if __name__ == '__main__':
    #startCapture('C:/Users/ishit/Desktop/DSS Server/Capture/', 1, 0, 120, 0, 700)
    while True:
        startCapture_NEW('C:/Users/ishit/Desktop/DSS Server/Capture/', 1, 0, 120, 0, 700)
