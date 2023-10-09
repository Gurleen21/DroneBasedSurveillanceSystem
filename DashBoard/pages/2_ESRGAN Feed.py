import datetime
import streamlit as st
from PIL import Image
import time
from Config import *

col1, col2 = st.columns(2)
with col1:
    org = st.empty()
with col2:
    srg = st.empty()
while (True):
    with col1:
        with org:
            f = no_signal_path
            image = Image.open(f)
            distime = datetime.datetime.now()
            st.image(image, caption=distime)
    with col2:
        with srg:
            f = no_signal_path
            image = Image.open(f)
            distime = datetime.datetime.now()
            st.image(image, caption=distime)
    time.sleep(1)