import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import ImageEnhance,Image

def clean(filename):
	image = Image.open("test/test/"+filename)
	enhancer = ImageEnhance.Sharpness(image)

	#for i in range(8):
	factor = 50 / 4.0
	enhancer.enhance(factor).save("check.png")



	#load original image
	img = cv2.imread('check.png')

	fgbg = cv2.createBackgroundSubtractorMOG2()
	fgmask = fgbg.apply(img)
	img = fgmask

	# global thresholding
	ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

	cv2.imwrite("test_cleaned/"+filename,th1)
