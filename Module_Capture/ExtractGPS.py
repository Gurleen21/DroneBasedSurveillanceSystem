import easyocr
import cv2
import datetime

def getGPS_Full_Image(path):
    reader = easyocr.Reader(['en'])
    try:
        result = reader.readtext(path, detail=0)
        result = str(result[0])
        index1 = result.find('C')
        xx = result[index1:]
        index1 = xx.find(':')
        xx = xx[index1 + 1:]
        NC = xx[1:xx.find('N')]
        EC = xx[xx.find('N') + 2:xx.find('E')]
        return ([NC, EC])
    except:
        return ([0,0])


def GPS_Extract_FullImage(pathold, delay=0):
    # dd/mm/YY H:M:S
    now = datetime.datetime.now()
    now = now - datetime.timedelta(seconds=delay)
    dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
    temp = 0
    if temp==0:
        return [dt_string, [0, 0]]
    ret = getGPS_Full_Image_Verbose(f'{pathold}{dt_string}.jpg')
    try:
        if ret[0] == 0 and ret[1] == 0:
            print("0 0")
            return [dt_string, [0, 0]]
        else:
            print(f'{dt_string}\t{ret}')
            return [dt_string, ret]
    except:
        print("ERROR")
        return [dt_string, [0, 0]]


def getGPS(path, temppath, xstart=168, xend=1286, ystart=786, yend=856):
    reader = easyocr.Reader(['en'])
    try:
        img = cv2.imread(path, 0)
        img = img[ystart:yend, xstart:xend]
        # img = img[786:856,168:1286]
        # img = img[230:290,0:600]
        filename = f"{temppath}tempimg.jpg"
        cv2.imwrite(filename, img)
        result = reader.readtext(filename, detail=0)
        result = str(result[0])
        print(result)
        index1 = result.find('C')
        xx = result[index1:]
        index1 = xx.find(':')
        xx = xx[index1 + 1:]
        NC = xx[1:xx.find('N')]
        EC = xx[xx.find('N') + 2:xx.find('E')]
        return ([NC, EC])
    except:
        return ([0,0])


def GPS_Extract(pathold, temppath, delay=0, xstart=168, xend=1286, ystart=786, yend=856):
    # dd/mm/YY H:M:S
    if(xstart==0 and xend ==0 and ystart==0 and yend==0):
        xstart = 168
        xend = 1286
        ystart = 786
        yend = 856
    now = datetime.datetime.now()
    now = now - datetime.timedelta(seconds=delay)
    dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
    ret = getGPS(f'{pathold}{dt_string}.jpg', temppath, xstart, xend, ystart, yend)
    try:
        if ret[0] == 0 and ret[1] == 0:
            print("0 0")
            return [dt_string, [0, 0]]
        else:
            print(f'{dt_string}\t{ret}')
            return [dt_string, ret]
    except:
        print("ERROR")
        return [dt_string, [0, 0]]


def GPS_Extract_TEST(imgpath, temppath, xstart=168, xend=1286, ystart=786, yend=856):
    ret = getGPS(imgpath, temppath, xstart, xend, ystart, yend)
    try:
        if ret[0] == 0 and ret[1] == 0:
            print("0 0")
        else:
            print(f'{ret}')
    except:
        print("ERROR")


def getGPS_Full_Image_Verbose(path):
    reader = easyocr.Reader(['en'])
    try:
        result = reader.readtext(path, detail=0)
        result = str(result[0])
        print(result)
        index1 = result.find('C')
        xx = result[index1:]
        index1 = xx.find(':')
        xx = xx[index1 + 1:]
        NC = xx[1:xx.find('N')]
        EC = xx[xx.find('N') + 2:xx.find('E')]
        return ([NC, EC])
    except:
        return ([0,0])

def GPS_Extract_Test_Full_Image(imgpath):
    ret = getGPS_Full_Image_Verbose(imgpath)
    try:
        if ret[0] == 0 and ret[1] == 0:
            print("0 0")
        else:
            print(f'{ret}')
    except:
        print("ERROR")

if __name__ == '__main__':
    GPS_Extract_Test_Full_Image(r"C:\Users\ishit\Desktop\DSS Server\GPS_Capture\M07D17h15m10s00.jpg")
