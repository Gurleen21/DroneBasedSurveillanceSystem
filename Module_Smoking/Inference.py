import cv2
import Config
from SendServer import sendImgModel1
from SendServer import sendImgModel1_Flagged
from keras.models import load_model
import tensorflow as tf
import datetime
import time
import pymongo

def singleImage(image_path,ts,model):
    img = cv2.imread(image_path)
    print(img.shape)
    img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
    print('1-Resize')
    img = img.reshape(1, 224, 224, 3)
    print('1-Reshape')
    predictions = model.predict(img)
    print('1-Predict')
    img = tf.squeeze(img)
    print('1-squeeze')
    img = img.cpu().numpy()
    print('1-convert')
    full_path_1 = f'{Config.Model1_Output_Dir}{ts}.jpg'
    print(predictions)
    print(img.shape)
    cv2.imwrite(full_path_1, img)
    if (predictions[0][1] > Config.MODEL1_THRESHOLD):
        full_path = f'{Config.Model1_Flagged_Dir}{ts}.jpg'
        borderoutput = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[1, 1, 255])
        cv2.imwrite(full_path, borderoutput)
        cv2.imwrite(full_path_1, borderoutput)
        print('1-Final')
        return 1
    return 0


def multipleImage(image_path_list,ts,model):
    ans = []
    ans_path = []
    i = 0
    for image_path in image_path_list:
        img = cv2.imread(image_path)
        img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
        img = img.reshape(1, 224, 224, 3)
        predictions = model.predict(img)
        full_path_1 = f'{Config.Model1_Output_Dir}{ts}_{i}.jpg'
        ans_path.append(full_path_1)
        if predictions[0][1] > Config.MODEL1_THRESHOLD:
            full_path = f'{Config.Model1_Flagged_Dir}{ts}_{i}.jpg'
            borderoutput = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[1, 1, 255])
            cv2.imwrite(full_path, borderoutput)
            cv2.imwrite(full_path_1, borderoutput)
            ans.append(full_path)
        else:
            cv2.imwrite(full_path_1, img)
    return (ans_path,ans)

def original_image_module1(img_path,model,timestamp,ts,gpsNS,gpsEW):
    full_path_1 = f'{Config.Model1_Output_Dir}{ts}.jpg'
    full_path = f'{Config.Model1_Flagged_Dir}{ts}.jpg'
    if(Config.MODULE_ON_OFF==1 and Config.MODEL1_ON_OFF==1 and Config.MODEL1_INPUT_ORIGINAL==1):
        if singleImage(img_path,ts,model)==1:
            sendImgModel1_Flagged([full_path], timestamp, ts, gpsNS, gpsEW, 1)
        sendImgModel1([full_path_1], timestamp, ts, gpsNS, gpsEW, 1)

def esrgan_image_module1(img_path_list,model,timestamp,ts,gpsNS,gpsEW):
    if(Config.MODULE_ON_OFF==1 and Config.MODEL1_ON_OFF==1 and Config.MODEL1_INPUT_ESRGAN==1):
        (alloutput, flaggedoutput) = multipleImage(img_path_list,ts,model)
        sendImgModel1(alloutput, timestamp, ts, gpsNS, gpsEW, 2)
        if(len(flaggedoutput)>0):
            sendImgModel1_Flagged(flaggedoutput, timestamp, ts, gpsNS, gpsEW, 2)


if __name__ == '__main__':
    model = load_model(Config.Model_Path)
    original_image_module1(r'C:\Users\ishit\Desktop\Smoking_Detection_1\TestImages\test2.jpeg',model,datetime.datetime.utcfromtimestamp(time.time()),"None2",0,0)
    #video(new_model)
