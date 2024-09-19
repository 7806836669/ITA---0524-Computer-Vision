import cv2 
import numpy as np 
img = cv2.imread("montage.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(gray) 
cv2.imshow('Original image', gray)
cv2.imshow('Equalized image',equ)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

