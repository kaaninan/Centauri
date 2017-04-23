#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import *

pwm_right = 0
pwm_left = 0
dir_left = 0
dir_right = 0

# Istenen pwm ve yone don
def go(goal_right, goal_left, goal_dir_right, goal_dir_left, step, sleep):
	global pwm_left, pwm_right, dir_left, dir_right
	
	# Yon degisikligini algila
		
	if dir_left == goal_dir_left and dir_right == goal_dir_right:
		# Hic yon degismiyor
		accel(goal_right, goal_left, step, sleep)

	elif dir_left != goal_dir_left and dir_right == goal_dir_right:
		# Sadece sol
		accel(pwm_right, 0, step, sleep) # Dur
		dir_left = goal_dir_left
		accel(goal_right, goal_left, step, sleep) # Hizlan
		
	elif dir_left == goal_dir_left and dir_right != goal_dir_right:
		# Sadece sag
		accel(0, pwm_left, step, sleep) # Dur
		dir_right = goal_dir_right
		accel(goal_right, goal_left, step, sleep) # Hizlan
		
	else:
		# Her ikisi degisiyor
		accel(0, 0, step, sleep) # Dur
		dir_right = goal_dir_right
		dir_left = goal_dir_left
		accel(goal_right, goal_left, step, sleep) # Hizlan


# Ivmelendir
def accel(goal_right, goal_left, step, sleep):
	global pwm_left, pwm_right, dir_left, dir_right
	# Hiz ne kadar degisecek
	step_right = goal_right - pwm_right
	step_left = goal_left - pwm_left
	
	# Adim basina degisecek hiz
	single_step_right = step_right/float(step)
	single_step_left = step_left/float(step)
	
	# Her adimda hizi arttir ve bekle
	for i in range(0, step):
		pwm_right += single_step_right
		pwm_left += single_step_left
		data = Int64MultiArray()
		data.data.append(dir_right) # 1 DIR
		data.data.append(round(pwm_right, 0)) # 1 SPEED
		data.data.append(dir_left) # 2 DIR
		data.data.append(round(pwm_left, 0)) # 2 SPEED
		pub_dc.publish(data)
		time.sleep(sleep)
	



def main():
	
	global pub_dc, rate	
	rospy.init_node('motion_dc', anonymous=True)
	
	pub_dc = rospy.Publisher('/serial_send_dc', Int64MultiArray, queue_size=10)
	
	rate = rospy.Rate(50)
	
	go(150, 50, 0, 0, 10, 0.2)
	time.sleep(1.5)
	go(100, 150, 1, 1, 10, 0.2)
	time.sleep(1.5)
	go(0, 0, 0, 1, 10, 0.2)
	
	rospy.spin()
	




if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass