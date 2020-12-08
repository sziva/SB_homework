import numpy as np
import cv2
import sys
import os
from array import *

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
