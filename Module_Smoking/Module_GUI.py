import tkinter as tk
import os
import Config
import threading
#from keras.models import load_model
from roboflow import Roboflow
import datetime
import time

from RecServer import getOriginalImages
from RecServer import getESRGANImages
# from Inference import original_image_module1
# from Inference import esrgan_image_module1
from Inference_Model2 import original_image_module2
from Inference_Model2 import esrgan_image_module2
from Settings import statusAndSettings
from Settings import statusAndSettingsInitial

global main_switch
global model1_switch
global original1_switch
global esrgan1_switch
global model2_switch
global original2_switch
global esrgan2_switch

currentOriginalImage = {}
currentESRGANImage = {}

def draw():
    global main_switch
    global model1_switch
    global original1_switch
    global esrgan1_switch
    global model2_switch
    global original2_switch
    global esrgan2_switch
    master = tk.Tk()
    master.title('Smoking Detection Module')
    tk.Label(master, text='\t').grid(row=0)
    tk.Label(master, text='\t').grid(row=1, column=1)
    # tk.Label(master, text='Main Switch').grid(row=1,column=2)
    # tk.Label(master, text='\t').grid(row=1, column=3)
    # tk.Label(master, text='\t').grid(row=1, column=5)
    # tk.Label(master, text='\t').grid(row=2)
    # tk.Label(master, text='Model_1').grid(row=3,column=2)
    # tk.Label(master, text='\t').grid(row=3, column=1)
    # tk.Label(master, text='\t').grid(row=3, column=3)
    # tk.Label(master, text='\t').grid(row=3, column=5)
    # tk.Label(master, text='Original_Input').grid(row=4,column=2)
    # tk.Label(master, text='\t').grid(row=4, column=1)
    # tk.Label(master, text='\t').grid(row=4, column=3)
    # tk.Label(master, text='\t').grid(row=4, column=5)
    # tk.Label(master, text='ESRGAN_Input').grid(row=5, column=2)
    # tk.Label(master, text='\t').grid(row=5, column=1)
    # tk.Label(master, text='\t').grid(row=5, column=3)
    # tk.Label(master, text='\t').grid(row=5, column=5)
    # tk.Label(master, text='\t').grid(row=6)
    tk.Label(master, text='Smoking Model').grid(row=7, column=2)
    tk.Label(master, text='\t').grid(row=7, column=1)
    tk.Label(master, text='\t').grid(row=7, column=3)
    tk.Label(master, text='\t').grid(row=7, column=5)
    tk.Label(master, text='Original_Input').grid(row=9, column=2)
    tk.Label(master, text='\t').grid(row=9, column=1)
    tk.Label(master, text='\t').grid(row=9, column=3)
    tk.Label(master, text='\t').grid(row=9, column=5)
    tk.Label(master, text='ESRGAN_Input').grid(row=10, column=2)
    tk.Label(master, text='\t').grid(row=10, column=1)
    tk.Label(master, text='\t').grid(row=10, column=3)
    tk.Label(master, text='\t').grid(row=10, column=5)
    tk.Label(master, text='\t').grid(row=11)
    print("")
    print(Config.MODEL1_ON_OFF, Config.MODEL1_INPUT_ORIGINAL, Config.MODEL1_INPUT_ESRGAN)
    print(Config.MODEL2_ON_OFF, Config.MODEL2_INPUT_ORIGINAL, Config.MODEL2_INPUT_ESRGAN)
    print()
    statusAndSettingsInitial()
    print("")
    print(Config.MODEL1_ON_OFF, Config.MODEL1_INPUT_ORIGINAL, Config.MODEL1_INPUT_ESRGAN)
    print(Config.MODEL2_ON_OFF, Config.MODEL2_INPUT_ORIGINAL, Config.MODEL2_INPUT_ESRGAN)
    print()
    statusAndSettingsInitial()

    # main_switch = tk.Button(master, text="ON", command=update_main, background='Green', padx=10, pady = 5)
    # main_switch.grid(row=1, column=4)

    # if Config.MODEL1_ON_OFF==1:
    #     model1_switch = tk.Button(master, text="ON", command=update_model1, background='Green', padx=10, pady = 5)
    #     if Config.MODEL1_INPUT_ORIGINAL==1:
    #         original1_switch = tk.Button(master, text="ON", command=update_original1, background='Green', padx=10,
    #                                      pady=5)
    #     else:
    #         original1_switch = tk.Button(master, text="OFF", command=update_original1, background='Red', padx=10,
    #                                      pady=5)
    #     if Config.MODEL1_INPUT_ESRGAN==1:
    #         esrgan1_switch = tk.Button(master, text="ON", command=update_esrgan1, background='Green', padx=10, pady=5)
    #     else:
    #         esrgan1_switch = tk.Button(master, text="OFF", command=update_esrgan1, background='Red', padx=10, pady=5)
    # else:
    #     model1_switch = tk.Button(master, text="OFF", command=update_model1, background='Red', padx=10, pady=5)
    #     original1_switch = tk.Button(master, text="---", command=update_original1, background='Gray', padx=10, pady=5)
    #     esrgan1_switch = tk.Button(master, text="---", command=update_esrgan1, background='Gray', padx=10, pady=5)
    #
    #
    # original1_switch.grid(row=4, column=4)
    # model1_switch.grid(row=3, column=4)
    # esrgan1_switch.grid(row=5, column=4)

    if Config.MODEL2_ON_OFF==1:
        model2_switch = tk.Button(master, text="ON", command=update_model2, background='Green', padx=10, pady = 5)
        if Config.MODEL2_INPUT_ORIGINAL:
            original2_switch = tk.Button(master, text="ON", command=update_original2, background='Green', padx=10,
                                         pady=5)
        else:
            original2_switch = tk.Button(master, text="OFF", command=update_original2, background='Red', padx=10,
                                         pady=5)
        if Config.MODEL2_INPUT_ESRGAN:
            esrgan2_switch = tk.Button(master, text="ON", command=update_esrgan2, background='Green', padx=10, pady=5)
        else:
            esrgan2_switch = tk.Button(master, text="OFF", command=update_esrgan2, background='Red', padx=10, pady=5)
    else:
        model2_switch = tk.Button(master, text="OFF", command=update_model2, background='Red', padx=10, pady=5)
        original2_switch = tk.Button(master, text="---", command=update_original2, background='Gray', padx=10, pady = 5)
        esrgan2_switch = tk.Button(master, text="---", command=update_esrgan2, background='Gray', padx=10, pady=5)


    original2_switch.grid(row=9, column=4)
    model2_switch.grid(row=7, column=4)
    esrgan2_switch.grid(row=10, column=4)

    t000 = threading.Thread(target=statusAndSettingslooop)
    t000.start()
    t0 = threading.Thread(target=getOriginal)
    t0.start()
    t00 = threading.Thread(target=getESRGAN)
    t00.start()
    # t1 = threading.Thread(target=runmodel1_Original)
    # t1.start()
    # t2 = threading.Thread(target=runmodel1_ESRGAN)
    # t2.start()
    t3 = threading.Thread(target=runmodel2_Original)
    t3.start()
    t4 = threading.Thread(target=runmodel2_ESRGAN)
    t4.start()
    tk.mainloop()

def statusAndSettingslooop():
    while(True):
        statusAndSettings()
def getOriginal():
    global currentOriginalImage
    while(True):
        while(Config.MODEL2_INPUT_ORIGINAL==1 or Config.MODEL1_INPUT_ORIGINAL==1):
            currentOriginalImage = getOriginalImages()

def getESRGAN():
    global currentESRGANImage
    while(True):
        while(Config.MODEL2_INPUT_ESRGAN==1 or Config.MODEL1_INPUT_ESRGAN==1):
            currentESRGANImage = getESRGANImages()

# def runmodel1_Original():
#     localmodel = load_model(Config.Model_Path)
#     print('Model Loaded')
#     global currentOriginalImage
#     # currentOriginalImage['img_path'] = r'C:\Users\ishit\Desktop\Smoking_Detection_1\TestImages\test2.jpeg'
#     # currentOriginalImage['timestamp'] = datetime.datetime.utcfromtimestamp(time.time())
#     # now = datetime.datetime.now()
#     # dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
#     # currentOriginalImage['ts'] = dt_string
#     # currentOriginalImage['gpsNS'] = '01'
#     # currentOriginalImage['gpsEW'] = '01'
#
#     while(True):
#         try:
#             while(Config.MODULE_ON_OFF==1 and Config.MODEL1_ON_OFF==1 and Config.MODEL1_INPUT_ORIGINAL==1):
#                 currentOriginalImage['img_path'] = r'C:\Users\ishit\Desktop\Smoking_Detection_1\TestImages\test2.jpeg'
#                 currentOriginalImage['timestamp'] = datetime.datetime.utcfromtimestamp(time.time())
#                 now = datetime.datetime.now()
#                 dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
#                 currentOriginalImage['ts'] = dt_string
#                 currentOriginalImage['gpsNS'] = '01'
#                 currentOriginalImage['gpsEW'] = '01'
#                 print('1-In while')
#                 original_image_module1(currentOriginalImage['img_path'],localmodel,currentOriginalImage['timestamp'],currentOriginalImage['ts'],currentOriginalImage['gpsNS'],currentOriginalImage['gpsEW'])
#         except Exception:
#             print('Model 1 Exception')
#
# def runmodel1_ESRGAN():
#     localmodel = load_model(Config.Model_Path)
#     global currentESRGANImage
#     while(True):
#         try:
#             while(Config.MODULE_ON_OFF==1 and Config.MODEL1_ON_OFF and Config.MODEL1_INPUT_ESRGAN):
#                 esrgan_image_module1(currentESRGANImage['img_path_list'],localmodel,currentESRGANImage['timestamp'],currentESRGANImage['ts'],currentESRGANImage['GPSNS'],currentESRGANImage['gpsEW'])
#         except Exception:
#             pass



def runmodel2_Original():
    rf = Roboflow(api_key="Qcd7g6qCpgyKp7jjPJmF")
    project = rf.workspace().project("dbss_smoking")
    roboflowmodel = project.version(1).model
    global currentOriginalImage
    while (True):
        try:
            while (Config.MODULE_ON_OFF == 1 and Config.MODEL2_ON_OFF==1 and Config.MODEL2_INPUT_ORIGINAL==1):
                original_image_module2(currentOriginalImage['img_path'], roboflowmodel, currentOriginalImage['timestamp'],currentOriginalImage['ts'], currentOriginalImage['gpsNS'],currentOriginalImage['gpsEW'])
        except Exception:
            pass


def runmodel2_ESRGAN():
    rf = Roboflow(api_key="Qcd7g6qCpgyKp7jjPJmF")
    project = rf.workspace().project("dbss_smoking")
    roboflowmodel = project.version(1).model
    global currentESRGANImage
    while (True):
        try:
            while (Config.MODULE_ON_OFF == 1 and Config.MODEL2_ON_OFF and Config.MODEL2_INPUT_ESRGAN):
                esrgan_image_module2(currentESRGANImage['img_path_list'], roboflowmodel, currentESRGANImage['timestamp'],currentESRGANImage['ts'], currentESRGANImage['GPSNS'], currentESRGANImage['gpsEW'])
        except Exception:
            pass

def update_main():
    global main_switch
    global model1_switch
    global original1_switch
    global esrgan1_switch
    global model2_switch
    global original2_switch
    global esrgan2_switch

    if(Config.MODULE_ON_OFF==0):
        Config.MODULE_ON_OFF = 1
        Config.MODEL1_ON_OFF = 1
        Config.MODEL2_ON_OFF = 1
        Config.MODEL1_INPUT_ORIGINAL = 1
        Config.MODEL2_INPUT_ORIGINAL = 1
        Config.MODEL1_INPUT_ESRGAN = 1
        Config.MODEL2_INPUT_ESRGAN = 1
        main_switch['text']='ON'
        main_switch['background']='Green'
        model1_switch['background'] = 'Green'
        original1_switch['background'] = 'Green'
        esrgan1_switch['background'] = 'Green'
        model2_switch['background'] = 'Green'
        original2_switch['background'] = 'Green'
        esrgan2_switch['background'] = 'Green'
        model1_switch['text'] = 'ON'
        original1_switch['text'] = 'ON'
        esrgan1_switch['text'] = 'ON'
        model2_switch['text'] = 'ON'
        original2_switch['text'] = 'ON'
        esrgan2_switch['text'] = 'ON'
    else:
        Config.MODULE_ON_OFF = 0
        main_switch['text'] = 'OFF'
        main_switch['background'] = 'Red'
        model1_switch['background'] = 'Gray'
        original1_switch['background'] = 'Gray'
        esrgan1_switch['background'] = 'Gray'
        model2_switch['background'] = 'Gray'
        original2_switch['background'] = 'Gray'
        esrgan2_switch['background'] = 'Gray'
        model1_switch['text'] = '---'
        original1_switch['text'] = '---'
        esrgan1_switch['text'] = '---'
        model2_switch['text'] = '---'
        original2_switch['text'] = '---'
        esrgan2_switch['text'] = '---'

def update_model1():
    global model1_switch
    global original1_switch
    global esrgan1_switch
    if(Config.MODULE_ON_OFF==1):
        if (Config.MODEL1_ON_OFF == 0):
            Config.MODEL1_ON_OFF = 1
            Config.MODEL1_INPUT_ORIGINAL = 1
            Config.MODEL1_INPUT_ESRGAN = 1
            model1_switch['text'] = 'ON'
            model1_switch['background'] = 'Green'
            original1_switch['text'] = 'ON'
            original1_switch['background'] = 'Green'
            esrgan1_switch['text'] = 'ON'
            esrgan1_switch['background'] = 'Green'
        else:
            Config.MODEL1_ON_OFF = 0
            Config.MODEL1_INPUT_ORIGINAL = 0
            Config.MODEL1_INPUT_ESRGAN = 0
            model1_switch['text'] = 'OFF'
            model1_switch['background'] = 'Red'
            original1_switch['text'] = '---'
            original1_switch['background'] = 'Gray'
            esrgan1_switch['text'] = '---'
            esrgan1_switch['background'] = 'Gray'

def update_original1():
    global original1_switch
    if (Config.MODULE_ON_OFF == 1 and Config.MODEL1_ON_OFF == 1):
        if (Config.MODEL1_INPUT_ORIGINAL == 0):
            Config.MODEL1_INPUT_ORIGINAL = 1
            original1_switch['text'] = 'ON'
            original1_switch['background'] = 'Green'
        else:
            Config.MODEL1_INPUT_ORIGINAL = 0
            original1_switch['text'] = 'OFF'
            original1_switch['background'] = 'Red'

def update_esrgan1():
    global esrgan1_switch
    if (Config.MODULE_ON_OFF == 1 and Config.MODEL1_ON_OFF == 1):
        if (Config.MODEL1_INPUT_ESRGAN == 0):
            Config.MODEL1_INPUT_ESRGAN = 1
            esrgan1_switch['text'] = 'ON'
            esrgan1_switch['background'] = 'Green'
        else:
            Config.MODEL1_INPUT_ESRGAN = 0
            esrgan1_switch['text'] = 'OFF'
            esrgan1_switch['background'] = 'Red'

def update_model2():
    global model2_switch
    global original2_switch
    global esrgan2_switch
    if (Config.MODULE_ON_OFF == 1):
        if (Config.MODEL2_ON_OFF == 0):
            Config.MODEL2_ON_OFF = 1
            Config.MODEL2_INPUT_ORIGINAL = 1
            Config.MODEL2_INPUT_ESRGAN = 1
            model2_switch['text'] = 'ON'
            model2_switch['background'] = 'Green'
            original2_switch['text'] = 'ON'
            original2_switch['background'] = 'Green'
            esrgan2_switch['text'] = 'ON'
            esrgan2_switch['background'] = 'Green'
        else:
            Config.MODEL2_ON_OFF = 0
            Config.MODEL2_INPUT_ORIGINAL = 0
            Config.MODEL2_INPUT_ESRGAN = 0
            model2_switch['text'] = 'OFF'
            model2_switch['background'] = 'Red'
            original2_switch['text'] = '---'
            original2_switch['background'] = 'Gray'
            esrgan2_switch['text'] = '---'
            esrgan2_switch['background'] = 'Gray'

def update_original2():
    global original2_switch
    if (Config.MODULE_ON_OFF == 1 and Config.MODEL2_ON_OFF==1):
        if (Config.MODEL2_INPUT_ORIGINAL == 0):
            Config.MODEL2_INPUT_ORIGINAL = 1
            original2_switch['text'] = 'ON'
            original2_switch['background'] = 'Green'
        else:
            Config.MODEL2_INPUT_ORIGINAL = 0
            original2_switch['text'] = 'OFF'
            original2_switch['background'] = 'Red'

def update_esrgan2():
    global esrgan2_switch
    if (Config.MODULE_ON_OFF == 1 and Config.MODEL2_ON_OFF == 1):
        if (Config.MODEL2_INPUT_ESRGAN == 0):
            Config.MODEL2_INPUT_ESRGAN = 1
            esrgan2_switch['text'] = 'ON'
            esrgan2_switch['background'] = 'Green'
        else:
            Config.MODEL2_INPUT_ESRGAN = 0
            esrgan2_switch['text'] = 'OFF'
            esrgan2_switch['background'] = 'Red'

if __name__ == "__main__":


    draw()
