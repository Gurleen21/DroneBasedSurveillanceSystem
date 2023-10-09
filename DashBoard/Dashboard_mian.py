import threading

import streamlit as st
from PIL import Image
import keyboard
import os
import psutil
import time
import glob
# def exit():
#     time.sleep(2)
#     keyboard.press_and_release('ctrl+w')
#     # Terminate streamlit python process
#     time.sleep(5)
#     pid = os.getpid()
#     p = psutil.Process(pid)
#     p.terminate()
# def login():
#     os.system(r'streamlit run C:\Users\ishit\Desktop\DashBoard\Login_Folder\Login.py')
# with st.sidebar:
#         logout = st.button("Logout")
# if logout:
#     t0 = threading.Thread(target=exit)
#     t0.start()
#     t1 = threading.Thread(target=login)
#     t1.start()


def dashView(option,path):
    with st.empty():
        while(True):
            for f in glob.iglob(f'{path}/*'):
                image = Image.open(f)
                distime = f"{f}"

                st.image(image, caption=distime)
                time.sleep(1)

def main():
    option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
dashView(0,'C:/Users/ishit/Desktop/DSS Server/Capture')
