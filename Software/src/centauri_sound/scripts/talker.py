#!/usr/bin/env python

import rospy
from centauri_sound.msg import *
from std_msgs.msg import *

def talker():
	pub = rospy.Publisher('/command_dc', Int64MultiArray, queue_size=10)

	rospy.init_node('talker', anonymous=True)
    
	rate = rospy.Rate(1) # 10hz
	
	while not rospy.is_shutdown():
    
		data = Int64MultiArray()
		data.data.append(50)
		data.data.append(50)
		data.data.append(1)
		data.data.append(1)
		data.data.append(10)
		data.data.append(1)
		pub.publish(data)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass