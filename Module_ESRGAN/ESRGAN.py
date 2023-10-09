import os

from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import cv2
from Config import *
from Split import splitImage
from Split import merge
from Split import splitImage_32
import datetime
from SendServer import sendImgLoop
from RecServer import getimg
import time
import matplotlib
import tensorflow as tf
from PIL import Image
def esrgan(image,generator):
    #image = cv2.imread(image_path)
    #image = cv2.cvtColour(image,cv2.COLOR_BGR2RGB)
    #image = cv2.resize(image,(32,32))
    #image = image/255
    image = np.expand_dims(image, axis=0)
    generated_hr = generator.predict(image)
    return generated_hr


def esrgan_loop(image_name,hsplit,vsplit,generator):
    original_image_path = f"{Original_Data_Dir}{image_name}.png"
    save_image_path = f"{ESRGAN_Data_Dir}"
    try:
        original_image = cv2.imread(original_image_path,3)
        #original_image = cv2.imread(r"C:\Users\ishit\Desktop\ishit_picture.jpg")
        (split_image_list,colnum,rownum) = splitImage_32(original_image)
        esrgan_image_list = []
        i =0
        for x in split_image_list:
            image = cv2.imread(x)
            save_path = f'{save_image_path}_{i}.png'
            generated_image = esrgan(image,generator)
            gen_new = tf.squeeze(generated_image)
            gen_new = gen_new.cpu().numpy()
            cv2.imwrite(save_path, gen_new)
            esrgan_image_list.append(save_path)
            i += 1
        print(colnum)
        tempimg = merge(esrgan_image_list,colnum,rownum)
        final_list = splitImage(tempimg,hsplit,vsplit)
        return final_list
    except Exception:
        return []


def esrgan_independant_runner(hsplit,vsplit,generator,delay=10):
    #generator = load_model(Model_Path, compile=False)
    try:
        # now = datetime.datetime.now()
        # now = now - datetime.timedelta(seconds=delay)
        # dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
        image,timestamp,ts,gpsNS,gpsEW = getimg("dt_string")
        if ts==0:
            print('ERROR')
            return
        # total_path = f'{Original_Data_Dir}{ts}.png'
        # os.remove(total_path)
        esrgan_image_list = esrgan_loop(ts,hsplit,vsplit,generator)
        if(len(esrgan_image_list)==0):
            pass
        else:
            sendImgLoop(esrgan_image_list,timestamp,ts,gpsNS,gpsEW)
    except Exception:
        pass


def esrgan_loop_test(image_path,hsplit,vsplit):
    generator = load_model(Model_Path, compile=False)
    save_image_path = f"{ESRGAN_Data_Dir}"
    original_image = cv2.imread(image_path)
    split_image_list = splitImage_32(original_image)
    esrgan_image_list = []
    i =0
    for x in split_image_list:
        save_path = f'{save_image_path}{i}.png'
        save_path2 = f'{save_image_path}{i}_gen.jpg'
        image = cv2.imread(x)
        image = np.expand_dims(image, axis=0)
        generated_hr = generator.predict(image)
        gen_new = tf.squeeze(generated_hr)
        gen_new = gen_new.cpu().numpy()
        cv2.imwrite(save_path2,gen_new)
        esrgan_image_list.append(save_path2)
        i += 1
    return esrgan_image_list

def esrgan_independant_runner_test(hsplit,vsplit,imgpath):

    print('Model Loaded')
    try:
        now = datetime.datetime.now()
        dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
        print(dt_string)
        ts = time.time()
        esrgan_image_list = esrgan_loop_test(imgpath,hsplit,vsplit)
        if(len(esrgan_image_list)==0):
            print('Pass')
        else:
            print(esrgan_image_list)
            sendImgLoop(esrgan_image_list,datetime.datetime.utcfromtimestamp(ts),dt_string,0,0)
    except Exception:
        pass




def test(img_path):
    generator = load_model(Model_Path, compile=False)
    sreeni_lr = cv2.imread(img_path)
    sreeni_hr = cv2.imread(img_path)
    #Change images from BGR to RGB for plotting.
    #Remember that we used cv2 to load images which loads as BGR.
    print(sreeni_lr.shape)
    sreeni_lr = cv2.cvtColor(sreeni_lr, cv2.COLOR_BGR2RGB)
    sreeni_hr = cv2.cvtColor(sreeni_hr, cv2.COLOR_BGR2RGB)
    sreeni_lr = cv2.resize(sreeni_lr,(32,32))
    sreeni_hr = cv2.resize(sreeni_hr,(128,128))

    sreeni_lr = sreeni_lr / 255.
    sreeni_hr = sreeni_hr / 255.

    sreeni_lr = np.expand_dims(sreeni_lr, axis=0)
    sreeni_hr = np.expand_dims(sreeni_hr, axis=0)

    generated_sreeni_hr = generator.predict(sreeni_lr)

    plt.figure(figsize=(16, 8))
    plt.subplot(231)
    plt.title('LR Image')
    plt.imshow(sreeni_lr[0,:,:,:])
    plt.subplot(232)
    plt.title('Superresolution')
    plt.imshow(generated_sreeni_hr[0,:,:,:])
    plt.subplot(233)
    plt.title('Orig. HR image')
    plt.imshow(sreeni_hr[0,:,:,:])
    plt.show()

if __name__ == "__main__":
    pass
    #test(r"C:\Users\ishit\Desktop\ishit_picture.jpg")
    #esrgan_independant_runner_test(3, 3, r"C:\Users\ishit\Desktop\ishit_picture.jpg")
    generator = load_model(Model_Path, compile=False)
    while(True):
        esrgan_independant_runner(3,3,generator,0)
    # esrgan_loop('image_name', 3, 3, generator)