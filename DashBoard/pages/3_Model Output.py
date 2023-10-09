import pymongo
import datetime
import time
from PIL import Image
from Config import *
import streamlit as st
import threading
from io import BytesIO

global model
global model_options
global option
global option2
model_options = ['Smoking', 'Fighting', 'Fire']



machine_list_smoking = []
machine_list_fighting = []
machine_list_fire = []

machine_running_status_smoking = {}
machine_running_status_fighting = {}
machine_running_status_fire = {}

machine_list_full_smoking = {}
machine_list_full_fighting = {}
machine_list_full_fire = {}


cluster = pymongo.MongoClient(
        "mongodb+srv://admin:drone123@cluster0.u8iebia.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Settings_Cluster"]
collection = db["Model_1"]
for x in collection.find({}, {"machine_id": 1, "input_channel":1, "source_channel":1}):
    machine_list_full_smoking[x['machine_id']]=([x['input_channel'],x['source_channel']])
    machine_list_smoking.append(x['machine_id'])
    machine_running_status_smoking[x['machine_id']]=0


def update_machine_status_smoking(diff=10):
    cluster_smoking = pymongo.MongoClient(
        "mongodb+srv://admin:drone123@cluster0.u8iebia.mongodb.net/?retryWrites=true&w=majority")
    db_smoking_settings = cluster_smoking["Settings_Cluster"]
    collection_smoking_setting_Model_1 = db_smoking_settings["Model_1"]
    #while(True):
    try:
        for x in collection_smoking_setting_Model_1.find({}, {"machine_id": 1, "ts": 1}):
            ts = x['ts']
            now = datetime.datetime.now()
            now = now - datetime.timedelta(seconds=diff)
            dt_string = now.strftime("%m-%d  %H-%M-%S")
            if ts<dt_string:
                machine_running_status_smoking[x['machine_id']] = 0
            else:
                machine_running_status_smoking[x['machine_id']] = 1
            print(machine_running_status_smoking)
        #     time.sleep(1)
    except Exception:
        pass

def update_machine_status_fighting(diff=10):
    pass

def update_machine_status_fire(diff=10):
    pass

# t0 = threading.Thread(target=update_machine_status_smoking)
# t0.start()
# t1 = threading.Thread(target=update_machine_status_fighting)
# t1.start()
# t2 = threading.Thread(target=update_machine_status_fire)
# t2.start()
col1, col2 = st.columns(2)
with col1:
    option = st.selectbox('Select Model',model_options)
with col2:
    if option==model_options[0]:
        option2 = st.selectbox('Select Machine',machine_list_smoking)
        try:
            ccc1, ccc2 = st.columns(2)
            with ccc1:
                st.write(f'Source Channel: {machine_list_full_smoking[option2][1]}')
            with ccc2:
                st.write(f'Input Channel: {machine_list_full_smoking[option2][0]}')
        except Exception:
            pass
    elif option==model_options[1]:
        option2 = st.selectbox('Select Machine',machine_list_fighting)
        try:
            ccc1, ccc2 = st.columns(2)
            with ccc1:
                st.write(f'Source Channel: {machine_list_full_fighting[option2][1]}')
            with ccc2:
                st.write(f'Input Channel: {machine_list_full_fighting[option2][0]}')
        except Exception:
            pass
    elif option==model_options[2]:
        option2 = st.selectbox('Selcet Machine',machine_list_fire)
        try:
            ccc1, ccc2 = st.columns(2)
            with ccc1:
                st.write(f'Source Channel: {machine_list_full_fire[option2][1]}')
            with ccc2:
                st.write(f'Input Channel: {machine_list_full_fire[option2][0]}')
        except Exception:
            pass

with st.empty():
    f = no_signal_path
    image_no_signal = Image.open(f)

    cluster_smoking = pymongo.MongoClient(
        "mongodb+srv://admin:drone123@cluster0.u8iebia.mongodb.net/?retryWrites=true&w=majority")
    db_smoking = cluster_smoking["Smoking_Model_Cluster"]
    collection_smoking = db_smoking["Smoking_Output_1"]

    #image_no_signal = image_no_signal.resize((600, 400))
    while(True):
        try:
            distime = datetime.datetime.now().strftime("%m-%d  %H-%M-%S")
            if option==model_options[0]:
                update_machine_status_smoking(10)
                if machine_running_status_smoking[option2]==1:
                    attribute1 = "ts"
                    now = datetime.datetime.now()
                    now = now - datetime.timedelta(seconds=10)
                    dt_string = now.strftime("%m-%d  %H-%M-%S")
                    value1 = dt_string
                    attribute2 = "machine_id"
                    value2 = option2
                    document = collection_smoking.find_one({attribute1: value1, attribute2: value2})
                    imagedoc = document['image']
                    image = Image.open(BytesIO(imagedoc))
                    st.image(image, caption=f'{dt_string}')
                else:
                    st.image(image_no_signal, caption=f'Machine Offline : {distime}')
            elif option==model_options[1]:
                if machine_running_status_fighting[option2]==1:
                    pass
                else:
                    st.image(image_no_signal, caption=f'Machine Offline : {distime}')
            elif option==model_options[2]:
                if machine_running_status_fire[option2]==1:
                    pass
                else:
                    st.image(image_no_signal, caption=f'Machine Offline : {distime}')
        except Exception:
            pass


