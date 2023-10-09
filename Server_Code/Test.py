import os
import datetime
now = datetime.datetime.now()
now = now - datetime.timedelta(seconds=30)
dt_string = now.strftime("M%mD%dh%Hm%Ms%S")
name = str(dt_string)
print(name)
