import numpy as np
import cv2

img=np.zeros((400,400,3),np.uint8)

img[:,:] =[255,0,0]
cv2.imwrite('D:\GitHub\opencv4\OpenCV4\blueImage.jpg',img)
cv2.imshow('img1',img)

cv2.waitKey(0)
cv2.destroyAllWindows()