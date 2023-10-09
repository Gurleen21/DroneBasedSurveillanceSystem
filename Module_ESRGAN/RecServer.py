import pymongo
import datetime
import time
from io import BytesIO
from PIL import Image
from numpy import sort
from pymongo.server_api import ServerApi
from Config import *



def getimg(ts):
    try:
        cluster = pymongo.MongoClient(
            "")
        cb = cluster.Original_Cluster
        tt = cb.Original_Database.find()
        tt = list(tt)
        newlist = sorted(tt, key=lambda d: d['ts'])
        #print(newlist[-1])
        db = cluster["Original_Cluster"]
        collection = db["Original_Database"]
        attribute = "ts"
        value = newlist[-1]['ts']
        print(value)
        document = collection.find_one({attribute: value})
        #document = collection.find().sort({"timestamp": -1}).limit(1)
        # print('0')
        # cursor = tt.toArray()
        # print(cursor)
        # lst = collection.find_one()
        # document = collection.find({}).sort({"timstamp":-1}).limit(1)
        # print(document)
        imagedoc = document['image']
        ts = document['ts']
        image = Image.open(BytesIO(imagedoc))
        timestamp = document['timestamp']
        gpsNS = document['gpsNS']
        gpsEW = document['gpsEW']
        output_path = f'{Original_Data_Dir}{ts}.png'
        image.save(output_path)
        return (image,timestamp,ts,gpsNS,gpsEW)
    except Exception:
        print("Error")
        return(0,0,0,0,0)

if __name__ == '__main__':
    getimg("M07D17h15m02s53")
