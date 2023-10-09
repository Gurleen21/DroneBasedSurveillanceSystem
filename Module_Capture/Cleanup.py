import datetime
from Config import *
import os
def clean(delay=100):
    while True:
        try:
            now = datetime.datetime.now()
            now = now - datetime.timedelta(seconds=delay)
            dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
            tmp = str(dt_string)
            total_path = f'{Directory_Location}{tmp}.png'
            os.remove(total_path)
            total_path = f'{GPS_Directory_PATH}{tmp}.png'
            os.remove(total_path)
        except:
            pass