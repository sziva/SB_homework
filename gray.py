import cv2
import numpy as np
import os

pic_num = 0


while pic_num < 17:
	print(pic_num)
	img = cv2.imread('/home/ziva/Desktop/SB_homework/obraz/neg-'+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
	#cv2.imread("posCopy/pos-" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
	cv2.imwrite('/home/ziva/Desktop/SB_homework/ob/neg-'+str(pic_num)+'.jpg', img)
	pic_num += 1

cv2.waitKey(0)
cv2.destroyAllWindows()
