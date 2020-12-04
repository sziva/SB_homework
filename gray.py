import cv2
import numpy as np
import os

pic_num = 0
folder = '/home/ziva/Desktop/pos'

while pic_num < 700:
	img = cv2.imread('/home/ziva/Desktop/pos/pos-'+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
	#cv2.imread("posCopy/pos-" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
	print('ORIG DIMENIONS: ', img.shape)
	scale = 60
	width = int(img.shape[1]*scale/100)
	height = int(img.shape[0]*scale/100)
	dim = (width, height)
	resized= cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	cv2.imwrite('/home/ziva/Desktop/posCopy/pos-'+str(pic_num)+'.jpg', resized)
	pic_num += 1

	print('resize dim: ', resized.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
