#!/usr/bin/env python

import rospy
import cv2
import random
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

	def __init__(self):
		self.image_sub = rospy.Subscriber("camera/color/image_raw",Image,self.callback)
		self.image_pub = rospy.Publisher("image_modified",Image,queue_size=1)
		self.bridge = CvBridge()

	def callback(self,data):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
				
				# Option
				# mono8: CV_8UC1, grayscale image
				# mono16: CV_16UC1, 16-bit grayscale image
				# bgr8: CV_8UC3, color image with blue-green-red color order
				# rgb8: CV_8UC3, color image with red-green-blue color order
				# bgra8: CV_8UC4, BGR color image with an alpha channel
				# rgba8: CV_8UC4, RGB color image with an alpha channel 

		except CvBridgeError as e:
			print(e)

		(rows,cols,channels) = cv_image.shape
		if cols > 60 and rows > 60 :
			cv2.circle(cv_image, (50,50), 10, 255)
			cv2.circle(cv_image,(256,256),120+random.randint(3, 9),(0,69,255),5)
			cv2.rectangle(cv_image,(150+random.randint(3, 9),222+random.randint(3, 9)),(363+random.randint(3, 9),400+random.randint(3, 9)),(222,252,22),2) 
			cv2.line(cv_image,(150,222),(363,400),(222,252,22),2)      
			cv2.putText(cv_image,"Text",(139,256),cv2.FONT_HERSHEY_DUPLEX, 0.75,(0,25,251),3)

		cv2.imshow("Image window", cv_image)
		cv2.waitKey(3)

		try:
			self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
		except CvBridgeError as e:
			print(e)

def main():
	ic = image_converter()
	rospy.init_node('ros_image_converter')
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()

if __name__ == '__main__':
		main()