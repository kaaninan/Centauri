#!/usr/bin/env python

import rospy
from centauri_sound.msg import *

def talker():
	pub = rospy.Publisher('/sound_cmd', SoundCommand, queue_size=10)

	rospy.init_node('talker', anonymous=True)
    
	rate = rospy.Rate(20) # 10hz
    
	data = SoundCommand()
	data.cmd = "say"
	data.param = "Hello I'm Centauri Robot. My purpose is help paralyzed people"
	pub.publish(data)
	rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass