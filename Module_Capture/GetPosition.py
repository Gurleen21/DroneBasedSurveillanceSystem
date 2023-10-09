from tkinter import *
import os
from Config import *
from ScreenGrab import Capture_NEW_ALL
from ExtractGPS import GPS_Extract_FullImage
from SendServer import sendimg
from Cleanup import clean
import threading


ls = [0,0,0,0,0,0,0,0]
ss = 0
global x1start
global x1end
global y1start
global y1end
global x2start
global x2end
global y2start
global y2end
global pointerpath
def draw(pointerp=PointerPath):
    global pointerpath
    global ls
    global ss
    pointerpath = pointerp
    master = Tk()
    global x1start
    global x1end
    global y1start
    global y1end
    global x2start
    global x2end
    global y2start
    global y2end
    Label(master, text='Screen Grab').grid(row=0, column=1)
    Label(master, text=' ').grid(row=0, column=0)
    Label(master, text=' ').grid(row=0, column=2)
    Label(master, text='Xstart').grid(row=1, column=1)
    Label(master, text=' ').grid(row=1, column=0)
    Label(master, text=' ').grid(row=1, column=3)
    Label(master, text='Xend').grid(row=2, column=1)
    Label(master, text=' ').grid(row=2, column=0)
    Label(master, text=' ').grid(row=2, column=3)
    Label(master, text='Ystart').grid(row=3, column=1)
    Label(master, text=' ').grid(row=3, column=0)
    Label(master, text=' ').grid(row=3, column=3)
    Label(master, text='Yend').grid(row=4, column=1)
    Label(master, text=' ').grid(row=4, column=0)
    Label(master, text=' ').grid(row=4, column=3)
    Label(master, text='GPS Extract').grid(row=5, column=1)
    Label(master, text=' ').grid(row=5, column=0)
    Label(master, text=' ').grid(row=5, column=2)
    Label(master, text='Xstart').grid(row=6, column=1)
    Label(master, text=' ').grid(row=6, column=0)
    Label(master, text=' ').grid(row=6, column=3)
    Label(master, text='Xend').grid(row=7, column=1)
    Label(master, text=' ').grid(row=7, column=0)
    Label(master, text=' ').grid(row=7, column=3)
    Label(master, text='Ystart').grid(row=8, column=1)
    Label(master, text=' ').grid(row=8, column=0)
    Label(master, text=' ').grid(row=8, column=3)
    Label(master, text='Yend').grid(row=9, column=1)
    Label(master, text=' ').grid(row=9, column=0)
    Label(master, text=' ').grid(row=9, column=3)
    Label(master, text=' ').grid(row=10)
    Label(master, text=' ').grid(row=11,column = 0)
    Label(master, text=' ').grid(row=11, column=2)
    Label(master, text=' ').grid(row=11, column=4)
    Label(master, text=' ').grid(row=12)
    Label(master, text=' ').grid(row=14)

    x1start = Entry(master)
    x1end = Entry(master)
    y1start = Entry(master)
    y1end = Entry(master)
    x2start = Entry(master)
    x2end = Entry(master)
    y2start = Entry(master)
    y2end = Entry(master)
    x1start.grid(row=1, column=2)
    x1end.grid(row=2, column=2)
    y1start.grid(row=3, column=2)
    y1end.grid(row=4, column=2)
    x2start.grid(row=6, column=2)
    x2end.grid(row=7, column=2)
    y2start.grid(row=8, column=2)
    y2end.grid(row=9, column=2)
    #x1start,x1end,y1start,y1end,x2start,x2end,y1start,y2end
    Button(master, text= "Update", command= update).grid(row=11, column=1)
    Button(master, text="Start Capture", command=start).grid(row=13, column=1)
    Button(master, text="Stop Capture", command=stop).grid(row=13, column=3)
    Button(master, text="Get Pointer", command=pointer).grid(row=11, column=3)
    t1 = threading.Thread(target=capture)
    t1.start()
    t2 = threading.Thread(target=gpsandsend)
    t2.start()
    t3 = threading.Thread(target=cleanup)
    t3.start()
    mainloop()

def cleanup():
    clean(10)
def capture():
    global ss
    global ls
    while(True):
        if (ss == 1):
            Capture_NEW_ALL(Directory_Location,GPS_Directory_PATH, 1, ls[0], ls[1], ls[2], ls[3],ls[4], ls[5], ls[6], ls[7])

def gpsandsend():
    global ss
    global ls
    while(True):
        if (ss == 1):
            [timestamp,[gpsNS, gpsEW]] = GPS_Extract_FullImage(GPS_Directory_PATH, 0)
            sendimg(f'{Directory_Location}{timestamp}.png', timestamp, gpsNS, gpsEW)
def start():
    global ss
    ss = 1

def stop():
    global ss
    ss = 0

def pointer():
    global pointerpath
    os.startfile(pointerpath)
def update():
    global ls
    global x1start
    global x1end
    global y1start
    global y1end
    global x2start
    global x2end
    global y2start
    global y2end
    x1s = x1start.get()
    nulltest = ''
    if(x1s == nulltest):
        x1s = 0
    x1e = x1end.get()
    if(x1e == nulltest):
        x1e = 0
    y1s = y1start.get()
    if (y1s == nulltest):
        y1s = 0
    y1e = y1end.get()
    if (y1e == nulltest):
        y1e = 0
    x2s = x2start.get()
    if (x2s == nulltest):
        x2s = 0
    x2e = x2end.get()
    if (x2e == nulltest):
        x2e = 0
    y2s = y2start.get()
    if (y2s == nulltest):
        y2s = 0
    y2e = y2end.get()
    if (y2e == nulltest):
        y2e = 0
    ls = [(int)(x1s),(int)(x1e),(int)(y1s),(int)(y1e),(int)(x2s),(int)(x2e),(int)(y2s),(int)(y2e)]
    start()


if __name__ == '__main__':
    draw(r"C:\Users\ishit\Downloads\MPos-v.0.5.0-Portable\MPos-v.0.5.0-Portable\MPos.exe")