import numpy as np
import cv2
import sys
import os
from array import *

cascadeFace = cv2.CascadeClassifier("myhaar.xml")


def intersectionOverUnion(positiveRec, detectedRec):

	#coordinates of the intersecion reactangle
	xP = max(positiveRec[0], detectedRec[0])
	yP = max(positiveRec[1], detectedRec[1])
	xD = min(positiveRec[2], detectedRec[2])
	yD = min(positiveRec[3], detectedRec[3])

	#area of the intersection of the rectangels
	intersection = float((xD-xP+1) * (yD-yP+1))

	#area of rectangles
	posRec = (positiveRec[2]-positiveRec[0]+1) * (positiveRec[3]-positiveRec[1]+1)
	detRec = (detectedRec[2]-detectedRec[0]+1) * (detectedRec[3]-detectedRec[1]+1)

	#area of union, we have to substract intersection so that we don have double areas
	union = float(posRec-intersection+detRec)

	#intersection over union
	iou = float(intersection/union)
	#print("IOU: " + str(iou))
	return iou

def detectEars(img):
	detectionList = cascadeFace.detectMultiScale(img, 1.05, 5)

	#print(detectionList)
	
	return detectionList
	
def vizualization(img, detectionList, positiveList):
	
	for x, y, w, h in detectionList:
		cv2.rectangle(img, (x,y), (x+w, y+h), (128, 255, 0), 2)

	if len(positiveList) == 4:
		positiveRec = positiveList
		cv2.rectangle(img, (positiveRec[0], positiveRec[1]), (positiveRec[0]+positiveRec[2], positiveRec[1]+positiveRec[3]), (0, 0, 255,), 2)
	else:
		for x, y, w, h in positiveList:
			cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)

	cv2.imwrite(filename + '.detected.jpg', img)

#iterates trough all pictures in folder		
folder = sys.argv[1] #sys.argv[1] takes folder name as an "input"
with os.scandir(folder) as entries:
	for entry in entries:
		filename = entry.name
		print(filename)
		img = cv2.imread(filename)	
		f = open('info.txt', 'r') #info.txt cointains annotations of test data
		lines = f.readlines()
		for data in lines:
			positiveList = []
			if data.startswith(str(folder+'/'+filename+ " ")):
				posList = data.split()
				startList = 2
				endList = 6
				print("POS: ", posList)
				listPosition = 0
				for x in range(int(posList[1])): 
					positiveList.insert(listPosition, [int(i) for i in posList[startList:endList]])	
					startList = endList
					endList = endList + 6
					listPosition += 1
			else:
				positiveList.insert(0,[10, 14, 36, 21])

		detectionList = detectEars(img)
		vizualization(img, detectionList, positiveList) 	
		
		iou = 0	
		for detectedRec in detectionList:
			for positiveRec in positiveList:
				print("POSITIVE REC: ", positiveRec)
				iou += intersectionOverUnion(positiveRec ,detectedRec)
			#print(positiveRec)
		iou = float(iou/len(detectionList))
		print("IOU: " + str(iou))



		#print iou for every picture on the pictue
		cv2.putText(img, "IoU: {:.4f}".format(iou), (10, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

		cv2.imshow("Image", img)
		cv2.waitKey(0)
cv2.waitKey(0)

#if you want to run it only for one picture -> uncomment this
#filename = sys.argv[1]
#img = cv2.imread(filename)	
#detectionList = detectFace(img)
#vizualization(img, detectionList) 	
