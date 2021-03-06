#!/usr/bin/env python

import rospy, time
from centauri_sound.msg import *
from std_msgs.msg import *

def talker():
	pub = rospy.Publisher('/command_dc', Int64MultiArray, queue_size=10)

	rospy.init_node('talker', anonymous=True)
    
	rate = rospy.Rate(10) # 10hz
	
	data = Int64MultiArray()
	data.data.append(50)
	data.data.append(50)
	data.data.append(0)
	data.data.append(0)
	pub.publish(data)
	
	time.sleep(1)
	
	data = Int64MultiArray()
	data.data.append(255)
	data.data.append(255)
	data.data.append(0)
	data.data.append(0)
	pub.publish(data)
	
	time.sleep(1)
	
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