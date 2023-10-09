import sys
import datetime
#from datetime import datetime
import multiprocessing
import threading
import time
import os
sys.path.insert(0, 'C:/Users/ishit/Desktop/DSS Server/Models/Smoking_Detector_Hand_Gesture_Full')
sys.path.insert(0,'C:/Users/ishit/Desktop/DSS Server/Screen Capture')
sys.path.insert(0,'C:/Users/ishit/Desktop/DSS Server/GPS')
sys.path.insert(0,'C:/Users/ishit/Desktop/DSS Server/Server')
sys.path.insert(0,'C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.2/bin')
sys.path.insert(0,'C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.2/lib')
sys.path.insert(0,'C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.2/lib/x64')
sys.path.insert(0,'C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.2/libnvvp')
from RunModel_Pic_Stream import startModel2
from ScreenGrab import startCapture_NEW
from Extract_GPS import GPS_ALL_NEW
from sendserver import sendimg
from revieveserver import getdata
num = 0
#time.sleep(10)
def task1():
    while True:
        try:
            startCapture_NEW('C:/Users/ishit/Desktop/DSS Server/Capture/', 1, 0, 120, 0, 700)
        except:
            pass
def task2():
    while True:
        try:
            [tmp, gps] = GPS_ALL_NEW('C:/Users/ishit/Desktop/DSS Server/Capture/')
            if tmp == 0:
                pass
            else:
                sendimg('C:/Users/ishit/Desktop/DSS Server/Capture/',tmp,gps[0],gps[1])
            #total_path = 'C:/Users/ishit/Desktop/DSS Server/Capture/'+str(tmp)+'.png'
            #print(total_path)
            total_path = f'C:/Users/ishit/Desktop/DSS Server/Capture/{tmp}.png'
            os.remove(total_path)

        except:
            pass

def task4():
    while True:
        try:
            now = datetime.datetime.now()
            now = now - datetime.timedelta(seconds=60)
            dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
            tmp = str(dt_string)
            total_path = f'C:/Users/ishit/Desktop/DSS Server/Capture/{tmp}.png'
            os.remove(total_path)
        except:
            pass


def task3():
    while True:
        try:
            now = datetime.datetime.now()
            now = now - datetime.timedelta(seconds=30)
            dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
            name = str(dt_string)
            try:
                [gpsN, gpsE] = getdata('C:/Users/ishit/Desktop/DSS Server/Capture2/',name)
                print(f'{name}\t{gpsE}\t{gpsN}')
            except:
                pass
        except:
            pass



t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)
t4 = threading.Thread(target=task4)
t1.start()
time.sleep(2)
t2.start()
time.sleep(40)
t3.start()
time.sleep(10)
t4.start()


#startModel2('C:/Users/ishit/Desktop/DSS Server/Capture/', 1, 100)




# adding Folder_2 to the system path

