import cv2
import numpy as np
import os

pic_num = 0

while pic_num < 89:
	img = cv2.imread('/home/ziva/Desktop/sb/SB_homework/testPic/test-'+str(pic_num)+'.jpg', cv2.IMREAD_UNCHANGED)
	print("LALLALA", img)
	print('ORIG DIMENIONS: ', img.shape)
	width = 360
	height = 480
	dim = (width, height)
	resized= cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	cv2.imwrite('/home/ziva/Desktop/sb/SB_homework/usc/test-'+str(pic_num)+'.jpg', resized)
	pic_num += 1

	print('resize dim: ', resized.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()

