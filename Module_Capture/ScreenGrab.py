import cv2
import pyautogui
import time
import numpy as np
from datetime import datetime


def Capture_NEW(filext='', interval=1, xstart=0, xend=0, ystart=0, yend=0):
    now = datetime.now()
    dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
    filename = f"{dt_string}.png"
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    width = xend - xstart
    height = yend - ystart
    if width <= 0 or height <= 0:
        height, width, _ = screen.shape
    ht, wt, _ = screen.shape
    if width > wt:
        _, width, _ = screen.shape
    if height > ht:
        height, _, _ = screen.shape
    filename_with_extension = filext + filename
    screen = screen[ystart:ystart + height, xstart:xstart + width, :]
    cv2.imwrite(filename_with_extension, screen)
    time.sleep(interval)

def Capture_NEW_ALL(filext='',gpsfileext='', interval=1, xstart=0, xend=0, ystart=0, yend=0 , xs=0,xe=0,ys=0,ye=0):
    now = datetime.now()
    dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
    filename = f"{dt_string}.png"
    gpsfilename = f"{dt_string}.jpg"
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    width = xend - xstart
    height = yend - ystart
    if width <= 0 or height <= 0:
        height, width, _ = screen.shape
    ht, wt, _ = screen.shape
    if width > wt:
        _, width, _ = screen.shape
    if height > ht:
        height, _, _ = screen.shape
    filename_with_extension = filext + filename
    gpsfilename_with_extension = gpsfileext + gpsfilename
    screen_cap = screen[ystart:ystart + height, xstart:xstart + width, :]
    screen_gps = screen[ys:ye, xs:xe, :]
    cv2.imwrite(filename_with_extension, screen_cap)
    cv2.imwrite(gpsfilename_with_extension, screen_gps)
    time.sleep(interval)


if __name__ == '__main__':
    while True:
        Capture_NEW('C:/Users/ishit/Desktop/DSS Server/Capture/', 1, 0, 1920, 0, 1080)
