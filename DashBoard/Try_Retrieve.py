import datetime

import pymongo
from PIL import Image
from io import BytesIO

from pymongo.server_api import ServerApi

import streamlit as st
from PIL import Image
import os
import time
import glob

def dashView():
    with st.empty():
        while(True):
            ts = datetime.datetime.now() - datetime.timedelta(minutes=30)
            try:
                image, gpsa,gpsb = getdata(datetime.datetime.utcfromtimestamp(ts.timestamp()))
                st.image(image, caption=(str)(ts)+" "+(str)(gpsa)+" "+(str)(gpsb))
            except Exception:
                st.write("No data for "+(str)(ts))


def getdata(ts):
    cluster = pymongo.MongoClient(
        "mongodb+srv://admin:drone123@cluster0.ln0stfj.mongodb.net/?retryWrites=true&w=majority",
        server_api=ServerApi('1'))
    db = cluster["Original_Cluster"]
    collection = db["Test_Database"]
    attribute = "timestamp"
    value = ts
    document = collection.find_one({attribute:value})
    imagedoc = document['image']
    image = Image.open(BytesIO(imagedoc))
    gpsN = document['gpslocNorth']
    gpsE = document['gpslocEast']
    return [image,gpsN,gpsE]

dashView()
