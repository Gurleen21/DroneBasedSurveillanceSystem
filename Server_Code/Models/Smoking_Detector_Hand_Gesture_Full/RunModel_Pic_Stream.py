from imutils.video import VideoStream
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import time
import cv2
import os


def startModel(filext='',interval=1,limit = 0):
	ap = argparse.ArgumentParser()
	ap.add_argument("-c", "--face_confidence", type=float, default=0.5,
		help="minimum probability to filter weak detections")
	args = vars(ap.parse_args())

	print("[INFO] loading face detector...")
	protoPath = os.path.sep.join(["face_detector", "deploy.prototxt"])
	protoPath2 = 'face_detector/deploy.prototxt.txt'
	modelPath = os.path.sep.join(["face_detector","res10_300x300_ssd_iter_140000.caffemodel"])
	#modelPath = 'C:/Users/ishit/Desktop/DSS Server/Models/Smoking_Detector_Hand_Gesture_Full/face_detector/res10_300x300_ssd_iter_140000.caffemodel'
	net = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

	# load the smoking detector model and label encoder
	print("[INFO] loading smoking detector...")
	model = load_model("smoking.model")
	#model = load_model(modelPath)
	le = pickle.loads(open("le.pickle", "rb").read())
	fname = 0

	count = 0
	# loop over the frames from the video stream
	while count<limit:
		count += 1
		file_path = f'{filext}{fname}.png'
		# grab the frame from the threaded video stream and resize it
		# to have a maximum width of 600 pixels
		frame = cv2.imread(file_path,1)
		frame = imutils.resize(frame, width=600)

		# grab the frame dimensions and convert it to a blob
		(h, w) = frame.shape[:2]
		blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
			(300, 300), (104.0, 177.0, 123.0))

		# pass the blob through the network and obtain the detections and
		# predictions
		net.setInput(blob)
		detections = net.forward()

		# loop over the detections
		for i in range(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated with the
			# prediction
			confidence = detections[0, 0, i, 2]

			# filter out weak detections
			if confidence > args["face_confidence"]:
				# compute the (x, y)-coordinates of the bounding box for
				# the face and extract the face ROI
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")

				# ensure the detected bounding box does fall outside the
				# dimensions of the frame
				startX = max(0, startX)
				startY = max(0, startY)
				endX = min(w, endX)
				endY = min(h, endY)

				# extract the face ROI and then preproces it in the exact
				# same manner as our training data

				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				img_gray = np.zeros_like(frame)
				img_gray[:, :, 0] = gray
				img_gray[:, :, 1] = gray
				img_gray[:, :, 2] = gray
				face = img_gray[startY:endY, startX:endX]
				face = cv2.resize(face, (32, 32))
				face = face.astype("float") / 255.0
				face = img_to_array(face)
				face = np.expand_dims(face, axis=0)

				# pass the face ROI through the trained smoking detector
				# model to determine if the face is "smoking" or "not smoking"
				predict = model.predict(face)[0]
				j = np.argmax(predict)
				label = le.classes_[j]

				# draw the label and bounding box on the frame
				label = "{}: {:.4f}".format(label, predict[j])
				cv2.putText(frame, label, (startX, startY - 10),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)



				cv2.rectangle(frame, (startX, startY), (endX, endY),
					(0, 0, 255), 2)

		cv2.putText(frame, "DONE", (100, 100),
					cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 255), 12)
		# show the output frame and wait for a key press
		cv2.imwrite(file_path, frame)
		fname += 1
		if fname==1000:
			fname = 0
		time.sleep(interval)


def startModel2(path,i1,i2):
	#startModel('C:/Users/ishit/Desktop/DSS Server/Capture/',1,10)
	startModel(path, i1, i2)
#startModel2('C:/Users/ishit/Desktop/DSS Server/Capture/',1,10)