import numpy as np
import cv2

img=np.zeros((400,400,3),np.uint8)

img[:,:] =[255,0,0]
cv2.imwrite('D:\\GitHub\\opencv4\\OpenCV4\\blueImage.jpg',img)
cv2.imshow('img1',img)

img[:,:] =[0,255,0]
cv2.imwrite('D:\\GitHub\\opencv4\\OpenCV4\\greenImage.jpg',img)
cv2.imshow('img2',img)

img[:,:] =[0,0,255]
cv2.imwrite('D:\\GitHub\\opencv4\\OpenCV4\\redImage.jpg',img)
cv2.imshow('img3',img)

img[:,:] =[255,255,255]
cv2.imwrite('D:\\GitHub\\opencv4\\OpenCV4\\whiteImage.jpg',img)
cv2.imshow('img4',img)

#파일생성
cv2.waitKey(0)
cv2.destroyAllWindows()