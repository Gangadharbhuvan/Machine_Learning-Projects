import cv2
import numpy as np
from pyzbar.pyzbar import decode
 
img = cv2.imread('./data/bar_code/bar-code_1.png')     #input image

#WebCam
'''
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
'''

myColor = (0, 0, 255)


while True:
 
    #success, img = cap.read()    #Webcamp
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
 
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,myColor,2)
 
    cv2.imshow('Result',img)
    cv2.waitKey(1)