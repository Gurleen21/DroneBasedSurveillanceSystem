import pymongo
from PIL import Image
from io import BytesIO

def getdata(outputname,imgname):
    cluster = pymongo.MongoClient("")
    db = cluster["Server"]
    collection = db["Image"]
    attribute = "timestamp"
    value = imgname
    document = collection.find_one({attribute:value})
    imagedoc = document['image']
    image = Image.open(BytesIO(imagedoc))
    gpsN = document['gpslocNorth']
    gpsE = document['gpslocEast']
    print(gpsN)
    print(gpsE)
    output_path = f'{outputname}/{imgname}.png'
    image.save(output_path)
    return [gpsN,gpsE]
