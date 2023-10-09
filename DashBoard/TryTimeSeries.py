import cv2
import numpy as np
import pyautogui
import pymongo
from bson import Timestamp
import calendar
from pymongo import MongoClient
#from datetime import datetime
import datetime
import time
from pymongo.server_api import ServerApi


def sendimg(imgpath, timestamp):


    cluster = pymongo.MongoClient("mongodb+srv://admin:drone123@cluster0.ln0stfj.mongodb.net/?retryWrites=true&w=majority",server_api=ServerApi('1'))
    db = cluster["Original_Cluster"]
    collection = db["Test_Database"]

    # post={"Name":'Gurleen'}
    # collection.insert_one(post)
    #imgopenpath = f'{imgpath}{imgname}.png'
    # try:
    #     cluster.admin.command('ping')
    #     print("Pinged your deployment. You successfully connected to MongoDB!")
    # except Exception as e:
    #     print(e)
    with open(imgpath, 'rb') as image_file:
        binary_data = image_file.read()
    ts = time.time()
    image_document = {'timestamp':datetime.datetime.utcfromtimestamp(ts), 'image': binary_data, 'gpslocNorth': 'TESTLOC', 'gpslocEast': 'TESTLOC'}
    result = collection.insert_one(image_document)

# sendimg('m00d00h00m00s01','C:/Users/ishit/Desktop/DSS Server/Capture/1.png')

def test():
    i = 0
    while(True):
        # now = datetime.now()
        # dt_string = now.strftime("%m%d%H%M%S")
        screen = pyautogui.screenshot()
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
        cv2.imwrite('C:/Users/ishit/Desktop/Temp/'+(str)(i)+'.jpg',screen)

        sendimg((str)('C:/Users/ishit/Desktop/Temp/'+(str)(i)+'.jpg'),"dt_string")
        i = i + 1

test()
#sendimg("","")