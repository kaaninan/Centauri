#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import *

def talker():
	pub = rospy.Publisher('/serial_send_dc', Int64MultiArray, queue_size=10)

	rospy.init_node('talker', anonymous=True)

	rate = rospy.Rate(50) # 10hz

	while not rospy.is_shutdown():
		for i in range(0,255, 5):
			rospy.loginfo("SeND")
			data = Int64MultiArray()
			data.data.append(1)
			data.data.append(i)
			data.data.append(1)
			data.data.append(i)
			pub.publish(data)
			rate.sleep()
			
		time.sleep(5)
			
		for i in range(255,-1,-5):
			rospy.loginfo("SeND")
			data = Int64MultiArray()
			data.data.append(1)
			data.data.append(i)
			data.data.append(1)
			data.data.append(i)
			pub.publish(data)
			rate.sleep()
			
		data = Int64MultiArray()
		data.data.append(0)
		data.data.append(0)
		data.data.append(0)
		data.data.append(0)
		pub.publish(data)

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass