#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import *

pwm_right = 0
pwm_left = 0
dir_left = 0
dir_right = 0

running = 0
stop_cmd = 0



# Istenen pwm ve yone don
def go(goal_right, goal_left, goal_dir_right, goal_dir_left, step, sleep):
	global pwm_left, pwm_right, dir_left, dir_right, running
	
	# Yon degisikligini algila
	if running == 0:
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
	global pwm_left, pwm_right, dir_left, dir_right, stop_cmd, running, dis_back, dis_front
	
	# Komutlar ust uste binmesin
	running = 1
	
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
		time.sleep(sleep/10)
		
	running = 0
	


def callback_command(data):
 	if running == 0:
	 	rospy.loginfo("Callback DC")
 		go(data.data[0], data.data[1], data.data[2], data.data[3], data.data[4], data.data[5])
 	else:
 		rospy.logwarn("Callback DC - Already running!")



def distance_back(data):
	global dis_back, stop_cmd, pub_stop
	dis_back = data.data
	limit = rospy.get_param('~distance_limit')
	if dis_back < limit and stop_cmd == 0:
		stop_cmd = 1
		data = Int64()
		data.data = stop_cmd
		pub_stop.publish(data)
		rate.sleep()
	elif dis_back >= limit and stop_cmd == 1:
		stop_cmd = 0
		data = Int64()
		data.data = stop_cmd
		pub_stop.publish(data)
		rate.sleep()
	
	
def distance_front(data):
	global dis_front, stop_cmd, pub_stop
	dis_front = data.data
	limit = rospy.get_param('~distance_limit')
	if dis_front < limit and stop_cmd == 0:
		stop_cmd = 1
		rospy.logerr("dis")
		data = Int64()
		data.data = stop_cmd
		pub_stop.publish(data)
		rate.sleep()
	elif dis_front >= limit and stop_cmd == 1:
		rospy.logerr("dis5")
		stop_cmd = 0
		data = Int64()
		data.data = stop_cmd
		pub_stop.publish(data)
		rate.sleep()



def main():
	
	global pub_dc, pub_stop, rate	
	rospy.init_node('motion_dc', anonymous=True)
	
	pub_dc = rospy.Publisher('/serial_send_dc', Int64MultiArray, queue_size=10)
	pub_stop = rospy.Publisher('/serial_stop_dc', Int64, queue_size=10)
	
	rospy.Subscriber('/distance_back', Int64, distance_back)
	rospy.Subscriber('/distance_front', Int64, distance_front)
	
	rospy.Subscriber('/command_dc', Int64MultiArray, callback_command)
	
	rate = rospy.Rate(100) # Only use stop dc when low distance
	
	time.sleep(4)
	# Stop when starting
	go(0, 0, 0, 0, 10, 0.1)
	
	rospy.spin()
	




if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass