
import easyocr
import cv2
from collections.abc import MutableMapping
from datetime import datetime
def getGPS(path):
    reader = easyocr.Reader(['en'])
    try:
        img = cv2.imread(path,0)
        img = img[786:856,168:1286]
        #img = img[230:290,0:600]
        cv2.imwrite('C:/Users/ishit/Desktop/DSS Server/GPS/tempimg.jpg', img)

        cv2.imwrite('C:/Users/ishit/Desktop/DSS Server/GPS/tempimg.jpg',img)
        result = reader.readtext('C:/Users/ishit/Desktop/DSS Server/GPS/tempimg.jpg', detail = 0)
        print('11')
        print(result)
        result = str(result[0])
        print(result)
        # print('22')
        # print(result[1])
        print('33')
        index1 = result.find('C')
        print(index1)
        print('3.1')
        xx = result[index1:]
        print('3.2')
        index1 = xx.find(':')
        print('3.3')
        xx = xx[index1+1:]
        print('3.4')
        NC = xx[1:xx.find('N')]
        print('3.5')
        EC = xx[xx.find('N')+2:xx.find('E')]
        print('44')
        print(NC)
        print(EC)
        print('55')
        return([NC,EC])
    except:
        pass

    #return result

#print(getGPS('C:/Users/ishit/Desktop/DSS Server/Capture/5.png'))

def GPS(pathold, textpath, id):
    ret = getGPS(pathold)
    with open(textpath, 'a') as f:
        f.write(f'{id}\t{ret[0]}\t{ret[1]}')
    f.close()

def GPS_ALL(pathold, textpath):
    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
    while True:
        print(f'{pathold}{dt_string}.png')
        ret = getGPS(f'{pathold}{dt_string}.png')
        if len(ret)<15:
            pass
        else:
            try:
                with open(textpath, 'a') as f:
                    f.write(f'{dt_string}\t{ret[0]}\t{ret[1]}\n')
                f.close()
            except:
                pass


def GPS_ALL_NEW(pathold):
    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
    #print(f'{pathold}{dt_string}.png')
    ret = getGPS(f'{pathold}{dt_string}.png')
    #ret = getGPS(f'{pathold}M06D01h17m31s52.png')
    try:
        if len(ret)!=2:
            print("0 0")
            return [0,[0,0]]
            #print("0 0")
        else:
            print(f'{dt_string}\t{ret}')
            return [dt_string, ret]
            #print(f'{dt_string}\t{ret}')
    except:
        print("ERROR")
        return [dt_string,[0,0]]


#GPS('C:/Users/ishit/Desktop/DSS Server/Capture/5.png','C:/Users/ishit/Desktop/DSS Server/GPS/CC.txt',102003133)

#GPS_ALL(f'C:/Users/ishit/Desktop/DSS Server/Capture/','C:/Users/ishit/Desktop/DSS Server/GPS/CC.txt',100)
#GPS_ALL_NEW(f'C:/Users/ishit/Desktop/DSS Server/Capture/')



def GPS_TEST(pathold,dt_string):
    path = f'{pathold}{dt_string}.png'
    ret = getGPS(path)
    print('1')
    print(ret)
    print('2')
    print(len(ret))
    # ret = getGPS(f'{pathold}M06D01h17m31s52.png')
    try:
        if len(ret)!=2:
            print("0 0")
            return [0, [0,0]]
            # print("0 0")
        else:
            print(f'{dt_string}\t{ret}')
            return [dt_string, ret]
            # print(f'{dt_string}\t{ret}')
    except:
        print("ERROR")
        return [0, [0,0]]


#[tmp, gps] = GPS_TEST('C:/Users/ishit/Desktop/DSS Server/Capture/','M06D01h18m35s21')


