
# import the necessary packages
import numpy as np
import cv2
import sys
from os.path import isfile,join
import os


if len(sys.argv) <= 1 or sys.argv[1] !='--image':
	print("Command",argv[0],"--image path")

paths = [x for x in os.listdir(sys.argv[2]) if 'png' in str(x) ]




# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())




# loop over the image paths
for imagePath in paths:
	# load the image and resize it to (1) reduce detection time
	# and (2) improve detection accuracy
	image = cv2.imread(imagePath)
	(h,w) = image.shape[:2]
	if w>400:
		ratio = h/w
		h = int(400*ratio)
		w = 400

	image = cv2.resize(image, (w,h), interpolation = cv2.INTER_AREA)
	orig = image.copy()

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
		padding=(8, 8), scale=1.05)

	# draw the original bounding boxes
	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	#rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	#pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	# draw the final bounding boxes
	#for (xA, yA, xB, yB) in pick:
	#	cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

	# show some information on the number of bounding boxes
	filename = imagePath[imagePath.rfind("/") + 1:]
	print("[INFO] {}: {} original boxes".format(filename, len(rects)) )	#, len(pick)))

	# show the output images
	cv2.imshow("Before NMS", orig)
	#cv2.imshow("After NMS", image)
	cv2.waitKey(0)
