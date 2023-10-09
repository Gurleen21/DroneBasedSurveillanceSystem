import pymongo
from PIL import Image
from io import BytesIO

cluster = pymongo.MongoClient("")
db = cluster["Server"]
collection = db["Image"]

image_document = collection.find_one()
imagedoc = image_document['image']
image = Image.open(BytesIO(imagedoc))

output_folder = 'C:/Users/HP/Desktop/Main/Thapar/Capstone Project/Drone Based Surveillance System/App/ServerApp'

output_filename = 'image2.jpg'

output_path = f'{output_folder}/{output_filename}'

image.save(output_path, 'JPEG')
