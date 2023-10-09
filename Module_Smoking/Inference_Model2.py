from roboflow import Roboflow
import Config
from SendServer import sendImgModel2
from SendServer import sendImgModel2_Flagged
import cv2
import datetime
import time

def singleImage(image_path,ts,model):
    img = cv2.imread(image_path)
    predictions = model.predict(image_path, confidence=Config.MODEL2_THRESHOLD*10, overlap=Config.MODEL2_OVERLAP*10).json()
    full_path_1 = f'{Config.Model2_Output_Dir}{ts}.jpg'
    for bounding_box in predictions["predictions"]:
        x0 = bounding_box['x'] - bounding_box['width'] / 2
        x1 = bounding_box['x'] + bounding_box['width'] / 2
        y0 = bounding_box['y'] - bounding_box['height'] / 2
        y1 = bounding_box['y'] + bounding_box['height'] / 2
        start_point = (int(x0), int(y0))
        end_point = (int(x1), int(y1))
        cv2.rectangle(img, start_point, end_point, color=(1, 1, 255), thickness=1)
    cv2.imwrite(full_path_1, img)
    full_path = f'{Config.Model2_Flagged_Dir}{ts}.jpg'
    if len(predictions["predictions"])>=1:
        cv2.imwrite(full_path, img)
        return 1
    return 0

def multipleImage(image_path_list,ts,model):
    ans = []
    ans_path = []
    i = 0
    for image_path in image_path_list:
        img = cv2.imread(image_path)
        predictions = model.predict(image_path, confidence=Config.MODEL2_THRESHOLD * 10,overlap=Config.MODEL2_OVERLAP * 10).json()
        for bounding_box in predictions["predictions"]:
            x0 = bounding_box['x'] - bounding_box['width'] / 2
            x1 = bounding_box['x'] + bounding_box['width'] / 2
            y0 = bounding_box['y'] - bounding_box['height'] / 2
            y1 = bounding_box['y'] + bounding_box['height'] / 2
            start_point = (int(x0), int(y0))
            end_point = (int(x1), int(y1))
            cv2.rectangle(img, start_point, end_point, color=(1, 1, 255), thickness=1)

        full_path_1 = f'{Config.Model2_Output_Dir}{ts}_{i}.jpg'
        cv2.imwrite(full_path_1, img)
        ans_path.append(full_path_1)
        if len(predictions["predictions"])>=1:
            full_path = f'{Config.Model2_Flagged_Dir}{ts}_{i}.jpg'
            cv2.imwrite(full_path, img)
            ans.append(full_path)

    return (ans_path, ans)


def original_image_module2(img_path,model,timestamp,ts,gpsNS,gpsEW):
    full_path_1 = f'{Config.Model2_Output_Dir}{ts}.jpg'
    full_path = f'{Config.Model2_Flagged_Dir}{ts}.jpg'
    if(Config.MODULE_ON_OFF==1 and Config.MODEL2_ON_OFF==1 and Config.MODEL2_INPUT_ORIGINAL==1):
        if singleImage(img_path,ts,model)==1:
            sendImgModel2_Flagged([full_path], timestamp, ts, gpsNS, gpsEW, 1)
        sendImgModel2([full_path_1], timestamp, ts, gpsNS, gpsEW, 1)

def esrgan_image_module2(img_path_list,model,timestamp,ts,gpsNS,gpsEW):
    if(Config.MODULE_ON_OFF==1 and Config.MODEL2_ON_OFF==1 and Config.MODEL2_INPUT_ESRGAN==1):
        (alloutput, flaggedoutput) = multipleImage(img_path_list,ts,model)
        sendImgModel2(alloutput, timestamp, ts, gpsNS, gpsEW, 2)
        if(len(flaggedoutput)>0):
            sendImgModel2_Flagged(flaggedoutput, timestamp, ts, gpsNS, gpsEW, 2)


def test(model,input_path):
    # infer on a local image
    predictions = model.predict(input_path, confidence=40,overlap=30).json()
    print(predictions)
    print(predictions['predictions'])
    predictionslist = predictions['predictions']
    print(len(predictionslist))
    print(predictionslist[0])
    prediction_0_dic = predictionslist[0]
    print(prediction_0_dic['confidence'])

def test2(model,input_path,output_path):
    # visualize your prediction
    model.predict(input_path, confidence=40, overlap=30).save(output_path)


if __name__ == '__main__':
    rf = Roboflow(api_key="Qcd7g6qCpgyKp7jjPJmF")
    project = rf.workspace().project("dbss_smoking")
    model = project.version(1).model
    inp = r'C:\Users\ishit\Desktop\Smoking_Detection_1\TestImages\test2.jpeg'
    out = r'C:\Users\ishit\Desktop\test2.jpeg'
    #test(model,inp)
    #singleImage(inp,"None",model)
    original_image_module2(inp, model, datetime.datetime.utcfromtimestamp(time.time()), "None", 0, 0)
    #test2(model,inp,out)