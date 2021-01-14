import numpy as np
import cv2
import sys
import os
from array import *
import matplotlib.pyplot as plt

cascadeFace = cv2.CascadeClassifier("casEar.xml")
allIOU = []

def intersectionOverUnion(positiveRec, detectedRec):

	aP = positiveRec[0]
	aD = detectedRec[0]
	bP = positiveRec[1]
	bD = detectedRec[1]
	cP = positiveRec[0] + positiveRec[2]
	cD = detectedRec[0] + detectedRec[2]
	dP = positiveRec[1] + positiveRec[3]
	dD = detectedRec[1] + detectedRec[3]

	xP = max(aP, aD)
	yP = max(bP, bD)
	xD = min(cP, cD)
	yD = min(dP, dD)

	intersection = max(0, xD-xP+1) * max(0, yD-yP+1)

	posRec = (cP-aP+1) * (dP-bP+1)
	detRec = (cD-aD+1) * (dD-bD+1)

	union = float(posRec + detRec - intersection)

	iou = float(intersection/union)
	return iou

def detectEars(img):
	detectionList = cascadeFace.detectMultiScale(img, 1.05, 6)
	return detectionList

def vizualization(img, detectionList, positiveList, filename):

	for x, y, w, h in detectionList:
		cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2) #zelena

	for x, y, w, h in positiveList:
		cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2) #rdeca

	cv2.imwrite(filename + '.detected.jpg', img)

f = open('info.txt', 'r') #info.txt cointains annotations of test data
lines = f.readlines()

for data in lines:
	positiveList = []
	file = data.split(" ")
	file = file[0]
	file = str(file)
	filname = file.split("/")
	filname = filname[1]
	print("NAME: ", filname)
	img = cv2.imread(file)
	posList = data.split()
	startList = 2
	endList = 6
	listPosition = 0

	for x in range(int(posList[1])):
		positiveList.insert(listPosition, [int(i) for i in posList[startList:endList]])
		startList = endList
		endList = endList + 6
		listPosition += 1

	detectionList = detectEars(img)
	vizualization(img, detectionList, positiveList, filname)

	iou = 0
	for detectedRec in detectionList:
		for positiveRec in positiveList:
			iou += intersectionOverUnion(positiveRec, detectedRec)

	if len(detectionList) > 0:
		iou = float(iou/len(detectionList))

	allIOU.append(iou)

	cv2.putText(img, "IoU: {:.4f}".format(iou), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

	cv2.imshow("Image", img)
	cv2.waitKey(0)

avg = [np.mean(allIOU)]*len(allIOU)
plt.plot(allIOU)
plt.plot(avg)
plt.ylabel('Accuracy')
plt.show()

