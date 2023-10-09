import pymongo
import datetime
import time
from pymongo.server_api import ServerApi

def sendimg(imgpath, timestamp,gpsNS,gpsEW):
    cluster = pymongo.MongoClient("",server_api=ServerApi('1'))
    db = cluster["Original_Cluster"]
    collection = db["Original_Database"]
    i = 0
    while(True):
        print(i)
        try:
            if i==100:
                break
            i += 1
            with open(imgpath, 'rb') as image_file:
                binary_data = image_file.read()
            ts = time.time()
            print(timestamp)
            image_document = {'timestamp':datetime.datetime.utcfromtimestamp(ts), 'ts':timestamp,'image': binary_data, 'gpsNS': gpsNS, 'gpsEW': gpsEW}
            result = collection.insert_one(image_document)
            break
        except Exception:
            print('SENDING ERROR')
