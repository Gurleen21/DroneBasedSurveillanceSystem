import datetime
import streamlit as st
from PIL import Image
import os
import time
import glob
from Config import *
import extra_streamlit_components as stx


def original_view():
    # ocol1 = st.columns(1)
    # with ocol1:
    #     org = st.empty()
    # while (True):
    #     with ocol1:
    #         with org:
    #             f = no_signal_path
    #             image = Image.open(f)
    #             distime = datetime.datetime.now()
    #             st.image(image, caption=distime)
    #     time.sleep(1)

    while(True):
        f = no_signal_path
        image = Image.open(f)
        distime = datetime.datetime.now()
        st.image(image, caption=distime)
        time.sleep(1)
            # for f in glob.iglob(f'{path}/*'):
            #     image = Image.open(f)
            #     distime = f"{f}"
            #
            #     st.image(image, caption=distime)
            #     time.sleep(1)


def original_split_view():
    col1, col2, col3 = st.columns(3)
    with col1:
        c1r1 = st.empty()
        c1r2 = st.empty()

    while (True):
        with col1:
            with c1r1:
                f = no_signal_path
                image = Image.open(f)
                distime = datetime.datetime.now()
                st.image(image, caption=distime)
            with c1r2:
                f = no_signal_path
                image = Image.open(f)
                distime = datetime.datetime.now()
                st.image(image, caption=distime)
        time.sleep(1)

def esrgan_view():
    col1, col2 = st.columns(2)
    with col1:
        org = st.empty()
    with col2:
        srg = st.empty()
    #
    # with col1:
    #     with org:
    #         f = no_signal_path
    #         image = Image.open(f)
    #         distime = datetime.datetime.now()
    #         st.image(image, caption=distime)
    # with col2:
    #     with srg:
    #         f = no_signal_path
    #         image = Image.open(f)
    #         distime = datetime.datetime.now()
    #         st.image(image, caption=distime)
    # time.sleep(1)
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

def model1_view():
    with st.empty():
        while(True):
            f = no_signal_path
            image = Image.open(f)
            distime = datetime.datetime.now()
            st.image(image, caption=distime)
            time.sleep(1)


def main():
    chosen_id = stx.tab_bar(
        data=[stx.TabBarItemData(id="tab1", title="\tOriginal\t", description=""),
              stx.TabBarItemData(id="tab2", title="\tESRGAN\t", description=""),
              stx.TabBarItemData(id="tab3", title="\tModel Outputs\t", description="")])
    display_area = st.empty()
    if chosen_id == "tab1":
        with display_area:
            original_view()
    elif chosen_id == "tab2":
        with display_area:
            esrgan_view()
    elif chosen_id == "tab3":
        with display_area:
            pass
    else:
        display_area = st.empty()

    #original_feed, srgan_feed, smoking_model_feed = st.tabs(['\tOriginal\t','\tESRGAN\t','\tSmoking Model\t'])
    #option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
    # display_area = st.empty()
    # with original_feed:
    #     with display_area:
    #         original_view()
    # with srgan_feed:
    #     with display_area:
    #         esrgan_view()


if __name__ == '__main__':
    main()

# 'C:/Users/ishit/Desktop/DSS Server/Capture'

