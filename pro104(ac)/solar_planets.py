import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Mercury",(120,250),cv2.FONT_HERSHEY_COMPLEX,0.35,(255,255,255))

cv2.putText(img,"Venus",(194,260),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))

cv2.putText(img,"Earth",(290,270),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))

cv2.putText(img,"Mars",(385,270),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))

cv2.putText(img,"Jupiter",(530,380),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Saturn",(750,320),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Uranus",(970,310),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Neptune",(1110,310),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("output",img)

cv2.waitKey(0)