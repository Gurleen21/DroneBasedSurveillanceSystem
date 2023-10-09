import streamlit as st
from Config import *
import Config
import pymongo
import time
from io import BytesIO
from PIL import Image
import datetime
import threading
channel_status = {}
channel_info = {}
zone_info = {}

def update_channel_status(diff=10):
    global channel_status
    cluster = pymongo.MongoClient(
        "mongodb+srv://admin:drone123@cluster0.ln0stfj.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["Image_Cluster"]
    collection = db["Settings"]
    channel_status = {}
    #while(True):
    try:
        for x in collection.find({}, {"channel": 1, "ts": 1}):
            ts = x['ts']
            now = datetime.datetime.now()
            now = now - datetime.timedelta(seconds=diff)
            dt_string = now.strftime("%m-%d  %H-%M-%S")
            #print(f'{ts}:{dt_string}')
            if ts<dt_string:
                channel_status[x['channel']] = 0
            else:
                channel_status[x['channel']] = 1
        print(channel_status)
        #     time.sleep(1)
    except Exception:
        pass

#
# def getOriginalImages(delay=3):
#     try:
#         cluster = pymongo.MongoClient(
#             "mongodb+srv://admin:drone123@cluster0.ln0stfj.mongodb.net/?retryWrites=true&w=majority")
#         db = cluster["Image_Cluster"]
#         collection = db["Original_Database"]
#         attribute = "ts"
#         now = datetime.datetime.now() - datetime.timedelta(seconds=delay)
#         dt_string = now.strftime("%m-%d  %H-%M-%S")
#         document = collection.find_one({attribute: dt_string})
#         i = 0
#         while(True):
#             if(document==None):
#                 i += 1
#                 document = collection.find_one({attribute: dt_string})
#             else:
#                 break
#             if i==50:
#                 break
#         imagedoc = document['image']
#         ts = dt_string
#         image = Image.open(BytesIO(imagedoc))
#         output_path = f'{Config.Original_Image_Dir}{ts}.png'
#         image.save(output_path)
#     except Exception:
#         print("Error")
#
# def getimages():
#     while(True):
#         getOriginalImages(3)
global channel_list
def getChannels():
    global channel_list
    channel_list = []
    cluster = pymongo.MongoClient(
        "mongodb+srv://admin:drone123@cluster0.ln0stfj.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["Image_Cluster"]
    collection = db["Settings"]
    try:
        for x in collection.find({}, {"channel": 1, "info":1,"zone":1}):
            channel_list.append(x['channel'])
            channel_info[x['channel']]=x['info']
            zone_info[x['channel']] = x['zone']
        print(channel_list)
        #     time.sleep(1)
    except Exception:
        channel_list = [1]

getChannels()
col1, col2 = st.columns(2)
with col1:
    option = st.selectbox('Select Channel',channel_list)
with col2:
    st.write(channel_info[option])
    st.write(f'Zone: {zone_info[option]}')

with st.empty():
    cluster = pymongo.MongoClient(
        "mongodb+srv://admin:drone123@cluster0.ln0stfj.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["Image_Cluster"]
    collection = db["Original_Database"]
    f = no_signal_path
    image_no_signal = Image.open(f)
    while(True):
        try:
            distime = datetime.datetime.now().strftime("%m-%d  %H-%M-%S")
            if option==1:
                update_channel_status(10)
                if channel_status[option]==1:
                    attribute1 = "ts"
                    now = datetime.datetime.now()
                    now = now - datetime.timedelta(seconds=3)
                    dt_string = now.strftime("%m-%d  %H-%M-%S")
                    value1 = dt_string
                    attribute2 = "channel"
                    value2 = option
                    document = collection.find_one({attribute1: value1, attribute2: value2})
                    imagedoc = document['image']
                    image = Image.open(BytesIO(imagedoc))
                    st.image(image, caption=f'{dt_string}')
                else:
                    #print('else part')
                    st.image(image_no_signal, caption=f'Channel Offline : {distime}')
        except Exception:
            pass



# with st.empty():
#     f = no_signal_path
#     image_no_signal = Image.open(f)
#     image_no_signal = image_no_signal.resize((600,400))
#     t1 = threading.Thread(target=getimages)
#     t1.start()
#     i = 0
#     while (True):
#         try:
#             i += 1
#             now = datetime.datetime.now() - datetime.timedelta(seconds=4)
#             ts = now.strftime("%m-%d  %H-%M-%S")
#             path = f'{Config.Original_Image_Dir}{ts}.png'
#             image = Image.open(path)
#             image = image.resize((600,400))
#             st.image(image,caption=ts)
#             i = 0
#         except Exception:
#             if i > 50000:
#                 distime = datetime.datetime.now().strftime("%m-%d  %H-%M-%S")
#                 st.image(image_no_signal, caption=distime)
#             else:
#                 pass