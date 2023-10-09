import pymongo
from pymongo import MongoClient
def sendimg(imgpath,imgname,gpsloc1,gpsloc2):
    cluster = pymongo.MongoClient("")
    db = cluster["Server"]
    collection = db["Image"]

    # post={"Name":'Gurleen'}
    # collection.insert_one(post)
    imgopenpath = f'{imgpath}{imgname}.png'
    with open(imgopenpath, 'rb') as image_file:
        binary_data = image_file.read()
    image_document = {"timestamp":imgname,'image': binary_data,'gpslocNorth':gpsloc1,'gpslocEast':gpsloc2}
    result = collection.insert_one(image_document)

#sendimg('m00d00h00m00s01','C:/Users/ishit/Desktop/DSS Server/Capture/1.png')
 
