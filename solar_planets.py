import cv2

planets = cv2.imread("solar-system.jpg")
#cv2.imshow("Solar-System",planets)
#cv2.waitKey(0)

mercury = "mercury"
cv2.putText(planets, mercury,(110,190),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))

venus = "venus"
cv2.putText(planets, venus,(190,260),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))

earth = "earth"
cv2.putText(planets, earth,(290,170),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))

mars = "mars"
cv2.putText(planets, mars,(380,255),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))

jupiter = "jupiter"
cv2.putText(planets, jupiter,(550,50),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))

saturn = "saturn"
cv2.putText(planets, saturn,(750,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))

uranus = "uranus"
cv2.putText(planets, uranus,(970,140),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))

neptune = "neptune"
cv2.putText(planets, neptune,(1110,280),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))

cv2.imshow("Solar-System", planets)
cv2.waitKey(0)