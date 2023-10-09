
import os
import tensorflow as tf
from tensorflow import keras
import cv2
from Config import *



def singleImage(image_path,model):
    pass

def multipleImage(image_path_list,model):
    pass

def test(new_model):
    img=cv2.imread('C:/Users/ishit/Desktop/Smoking_Detection_1/TestImages/test4.jpeg')
    print(img.shape)
    img=cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
    print(img.shape)
    #img=img/255
    cv2.imwrite('C:/Users/ishit/Desktop/Smoking_Detection_1/TestImages/test4_reshaped.jpeg',img)
    img = img.reshape(1,224,224,3)
    predictions=new_model.predict(img)
    print(predictions)
    pre_class=predictions.argmax()

def video(new_model):
    vid = cv2.VideoCapture(0)
    while(True):
        ret, frame = vid.read()
        img=cv2.resize(frame, (224,224), interpolation = cv2.INTER_AREA)
        img = img.reshape(1, 224, 224, 3)
        predictions=new_model.predict(img)
        pre_class=predictions.argmax()
        #print(predictions[0][1])
        if(predictions[0][1]>0.8):
            borderoutput = cv2.copyMakeBorder(frame, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[1, 1, 255])
            cv2.imshow('frame', borderoutput)
            #print('RED')
        else:
            borderoutput = cv2.copyMakeBorder(frame, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[1, 255, 1])
            cv2.imshow('frame', borderoutput)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    new_model = tf.keras.models.load_model(Model_Path)
    video(new_model)
