import pymongo
import datetime
import time
import Config

def statusAndSettingsInitial():
    cluster = pymongo.MongoClient(
        "mongodb+srv://admin:drone123@cluster0.y4q7p88.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["Settings_Cluster"]
    collection2 = db["Settings_Database"]
    try:
        attribute = "target"
        value = "Smoking_Module_Initial"
        document = collection2.find_one({attribute: value})
        if document!=None:
            Config.MODEL1_ON_OFF = (int)(document['ON_OFF_1'])
            Config.MODEL2_ON_OFF = (int)(document['ON_OFF_2'])
            Config.MODEL1_INPUT_ORIGINAL = (int)(document['ORIGINAL_IMAGE_1'])
            Config.MODEL2_INPUT_ORIGINAL = (int)(document['ORIGINAL_IMAGE_2'])
            Config.MODEL1_INPUT_ESRGAN = (int)(document['ESRGAN_IMAGE_1'])
            Config.MODEL2_INPUT_ESRGAN = (int)(document['ESRGAN_IMAGE_2'])
            print("")
            print(Config.MODEL1_ON_OFF, Config.MODEL1_INPUT_ORIGINAL, Config.MODEL1_INPUT_ESRGAN)
            print(Config.MODEL2_ON_OFF, Config.MODEL2_INPUT_ORIGINAL, Config.MODEL2_INPUT_ESRGAN)
            print()
    except Exception:
        pass
def statusAndSettings():
    # MODEL1_ON_OFF
    # MODEL2_ON_OFF
    # MODEL1_INPUT_ORIGINAL
    # MODEL2_INPUT_ORIGINAL
    # MODEL1_INPUT_ESRGAN
    # MODEL2_INPUT_ESRGAN

    cluster = pymongo.MongoClient(
        "mongodb+srv://admin:drone123@cluster0.y4q7p88.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["Settings_Cluster"]
    collection2 = db["Settings_Database"]
    collection1 = db["Smoking_Module_Database"]

    ##################### Status Send #########################
    now = datetime.datetime.now()
    ts = now.strftime("M%mD%dh%Hm%Ms%S")
    try:
        details = {'timestamp': datetime.datetime.utcfromtimestamp(time.time()), 'ts': ts, 'Model1': Config.MODEL1_ON_OFF, 'Model2': Config.MODEL2_ON_OFF}
        result = collection1.insert_one(details, bypass_document_validation=True)
    except Exception:
        pass

    ################## Settings Recieve #######################
    try:
        attribute = "target"
        value = "Smoking_Module"
        myquery = {attribute: value}
        newvalues = {"$set": {'ON_OFF_1': Config.MODEL1_ON_OFF, 'ON_OFF_2': Config.MODEL2_ON_OFF, 'ORIGINAL_IMAGE_1': Config.MODEL1_INPUT_ORIGINAL, 'ORIGINAL_IMAGE_2': Config.MODEL2_INPUT_ORIGINAL, 'ESRGAN_IMAGE_1': Config.MODEL1_INPUT_ESRGAN, 'ESRGAN_IMAGE_2': Config.MODEL2_INPUT_ESRGAN}}
        collection2.update_one(myquery, newvalues)
    except Exception:
        pass


if __name__ == '__main__':
    statusAndSettingsInitial()