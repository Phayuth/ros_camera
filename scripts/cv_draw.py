#!/usr/bin/env python

import rospy
import cv2
import random

Width = 640                                # Define Width
Height = 480                               # Define Height
cap = cv2.VideoCapture(4)                  # Read frame from Camera
while True:                                
	read, img = cap.read()                 # Read
	img = cv2.resize(img,(Width,Height))   # Resize into W and H

	cv2.circle(img,(256,256),120+random.randint(3, 9),(0,69,255),5)            
	cv2.rectangle(img,(150+random.randint(10, 100),222+random.randint(3, 9)),(363+random.randint(3, 9),400+random.randint(3, 9)),(222,252,22),2) 
	cv2.line(img,(150,222),(363,400),(222,252,22),2)      
	cv2.putText(img,"Text",(139,256),cv2.FONT_HERSHEY_DUPLEX, 0.75,(0,25,251),3)

	# Draw circle       CV2.circle(img,(xcenter,ycenter),radius,(B,G,R),thickness<--- or cv2.FILLED)
	# Draw rectangular  CV2.circle(img,(x1,x2),(y1,y2),(B,G,R),thickness<--- or cv2.FILLED)
	# Draw line         CV2.circle(img,(x1,x2),(y1,y2),(B,G,R),thickness<--- or cv2.FILLED)
	
	cv2.imshow("Video",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		