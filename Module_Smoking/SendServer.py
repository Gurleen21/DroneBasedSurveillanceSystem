import pymongo
import datetime
import time
from pymongo.server_api import ServerApi

def sendImgModel1_Flagged(output_img_list,timestamp,ts,gpsNS,gpsEW,source):
    pass

def sendImgModel2_Flagged(output_img_list,timestamp,ts,gpsNS,gpsEW,source):
    pass

def sendImgModel1(output_img_list,timestamp,ts,gpsNS,gpsEW,source):
    print('Send1')
    cluster = pymongo.MongoClient("")
    print('Send2')
    db = cluster["Smoking_Cluster"]
    print('Send3')
    collection = db["Smoking_Model1_Output_Database"]
    try:
        attribute = "ts"
        value = ts
        document = collection.find_one({attribute: value})
        print(document)
        if document == None:
            try:
                print('Send4')
                binary_data_list = []
                for x in output_img_list:
                    print(x)
                    with open(x, 'rb') as image_file:
                        binary_data = image_file.read()
                        binary_data_list.append(binary_data)
                print(len(binary_data_list))
                details = {'timestamp': timestamp, 'ts': ts, 'gpsNS': gpsNS, 'gpsEW': gpsEW,
                           'number': len(binary_data_list),'source':source}

                i = 0
                for x in binary_data_list:
                    details[f'img{i}'] = x
                    i += 1
                print(details)
                # print(details)
                result = collection.insert_one(details, bypass_document_validation=True)
                print(result)
                print('Hello')
            except Exception:
                pass
    except Exception:
        print('Model 1 Sending Error')



def sendImgModel2(output_img_list,timestamp,ts,gpsNS,gpsEW,source):
    print('Send1')
    cluster = pymongo.MongoClient("")
    print('Send2')
    db = cluster["Smoking_Cluster"]
    print('Send3')
    collection = db["Smoking_Model2_Output_Database"]
    try:
        attribute = "ts"
        value = ts
        document = collection.find_one({attribute: value})
        print(document)
        if document == None:
            try:
                print('Send4')
                binary_data_list = []
                for x in output_img_list:
                    with open(x, 'rb') as image_file:
                        binary_data = image_file.read()
                        binary_data_list.append(binary_data)
                print(len(binary_data_list))
                details = {'timestamp': timestamp, 'ts': ts, 'gpsNS': gpsNS, 'gpsEW': gpsEW,
                           'number': len(binary_data_list),'source':source}
                i = 0
                for x in binary_data_list:
                    details[f'img{i}'] = x
                    i += 1
                # print(details)
                result = collection.insert_one(details, bypass_document_validation=True)
                # print(result)
                # print('Hello')
            except Exception:
                pass
    except Exception:
        pass


if __name__ == '__main__':
    uri = ""
    # Create a new client and connect to the server
    client = pymongo.MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    #datetime.datetime.utcfromtimestamp(time.time())
