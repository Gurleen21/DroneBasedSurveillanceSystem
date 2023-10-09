import Config
import pymongo
import time
from io import BytesIO
from PIL import Image
import datetime


def getOriginalImages():
    try:
        cluster = pymongo.MongoClient(
            "")
        # cb = cluster.Original_Cluster
        # tt = cb.Original_Database.find()
        # tt = list(tt)
        #
        # newlist = sorted(tt, key=lambda d: d['ts'])
        #print(newlist)
        db = cluster["Original_Cluster"]
        collection = db["Original_Database"]
        attribute = "ts"
        #
        # value = newlist[-1]['ts']
        now = datetime.datetime.now() - datetime.timedelta(seconds=5)
        dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
        document = collection.find_one({attribute: dt_string})
        while(True):
            if(document==None):
                now = datetime.datetime.now() - datetime.timedelta(seconds=5)
                dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
                document = collection.find_one({attribute: dt_string})
            else:
                break
        imagedoc = document['image']
        ts = document['ts']
        image = Image.open(BytesIO(imagedoc))
        timestamp = document['timestamp']
        gpsNS = document['gpsNS']
        gpsEW = document['gpsEW']
        output_path = f'{Config.Original_Image_Dir}{ts}.png'
        print(output_path)
        image.save(output_path)
        dic = {}
        # currentESRGANImage['img_path'],
        # currentESRGANImage['timestamp'],
        # currentESRGANImage['ts'],
        # currentESRGANImage['GPSNS'],
        # currentESRGANImage['gpsEW']
        dic['img_path'] = output_path
        dic['timestamp'] = timestamp
        dic['ts'] = ts
        dic['gpsNS'] = gpsNS
        dic['gpsEW'] = gpsEW

        # dic['img_path'] = r'C:\Users\ishit\Desktop\Smoking_Detection_1\TestImages\test2.jpeg'
        # dic['timestamp']=datetime.datetime.utcfromtimestamp(time.time())
        # now = datetime.datetime.now()
        # dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
        # dic['ts']=dt_string
        # dic['gpsNS']='01'
        # dic['gpsEW']='01'
        return dic
    except Exception:
        print("Error")
        dic = {}
        return dic

def getESRGANImages():
    # currentESRGANImage['img_path_list'],
    # currentESRGANImage['timestamp'],
    # currentESRGANImage['ts'],
    # currentESRGANImage['GPSNS'],
    # currentESRGANImage['gpsEW']
    pass

if __name__ == '__main__':
    while(True):
        getOriginalImages()
