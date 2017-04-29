#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import *


present_pos_servos = [0,0,0,0,0,0,0,0]



##  LIMIT  ##

# Position limits
def limit_pos(positions):
	limits = rospy.get_param('~Limit')
	for key, pos in enumerate(positions):
		first = limits[key][0]
		end = limits[key][1]
		if pos >= first and pos <= end:
			pass
		elif int(pos) == -1:
			# Eger pozisyon -1 ise eksi konumunu koru
			pos = present_pos_servos[key]
		else:
			new = -1
			t1 = abs(first-pos)
			t2 = abs(end-pos)
			if t1 > t2:
				new = end
			else:
				new = first
			positions[key] = new
			rospy.logwarn("Motion Manager: Warning servo limit! ID: "+str(key+1)+" old pos: "+str(pos)+ " new pos: "+ str(new))
	return positions
	

# Position limits (only head)
def limit_pos_only_head(positions):
	# [x, y]
	limits = rospy.get_param('~Limit')
	for key, pos in enumerate(positions):
		first = limits[key+6][0]
		end = limits[key+6][1]
		if pos >= first and pos <= end:
			pass
		elif int(pos) == -1:
			# Eger pozisyon -1 ise eksi konumunu koru
			pos = present_pos_servos[key+6]
		else:
			new = -1
			t1 = abs(first-pos)
			t2 = abs(end-pos)
			if t1 > t2:
				new = end
			else:
				new = first
			positions[key] = new
			rospy.logwarn("Motion Manager (Head): Warning servo limit! ID: "+str(key+1)+" old pos: "+str(pos)+ " new pos: "+ str(new))
	return positions




##  SEND POS TO HARDWARE  ##


# Directly go postions
def go_pos(positions, speed):
	positions = limit_pos(positions) # Control limits
	for key, pos in enumerate(positions):
		data = Int64MultiArray()
		data.data = []
		data.data.append(int(key+1)) # ID
		data.data.append(int(pos)) # POS
		data.data.append(speed) # SPEED
		pub_servo.publish(data)
		rate.sleep()
		present_pos_servos[key] = pos



# For the servo rotations to end at the same time
def speed_calculate(pre_pos, goal_pos, max_speed):
	steps = []
	
	# Control limits
	goal_pos = limit_pos(goal_pos)
	
	# Degress of servo turn, for find max step size
	for i in range(0, len(pre_pos)):
		turn = goal_pos[i] - pre_pos[i]
		steps.append(abs(float(turn)))

	# Speed of which the motor go at last pos
	for i in range(0, len(pre_pos)):	
		# Calculate speed
		vel = (steps[i] * max_speed) / max(steps)
		
		# LOG
		#print str(i+1) + " ID's servo speed is: " + str(round(vel, 2)) + " step size is: " + str(steps[i]) + " pre pos: "+ str(pre_pos[i]) + " goal pos: " + str(goal_pos[i])

		# update pos of servos
		present_pos_servos[i] = goal_pos[i]
		
		# Publish Data
		data = Int64MultiArray()
		data.data = []
		data.data.append(i+1) # ID
		data.data.append(goal_pos[i]) # POS
		data.data.append(int(round(vel, 0))) # SPEED
		pub_servo.publish(data)
		rate.sleep()


# Only head move
def head_move(positions, speed):
	positions = limit_pos_only_head(positions) # Control limits
	for key, pos in enumerate(positions):
		data = Int64MultiArray()
		data.data = []
		data.data.append(int(key+6)) # ID
		data.data.append(int(pos)) # POS
		data.data.append(speed) # SPEED
		pub_servo.publish(data)
		rate.sleep()
		present_pos_servos[key+6] = pos



def callback_command(data):
	print data



def main():
	
	global pub_servo, rate
	
	rospy.init_node('motion_servo', anonymous=True)

	pub_servo = rospy.Publisher('/serial_send_servo', Int64MultiArray, queue_size=10)
	
	rospy.Subscriber('/command_servo', Int64MultiArray, callback_command)
	
	rate = rospy.Rate(50)
	
	rospy.spin()




if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass