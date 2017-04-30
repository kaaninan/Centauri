#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import *

# callback() -> go_pos() & go_pos_accel() & go_head() -> limit() -> send_hw

# CALLBACK
# [0, ..] -> go_pos
# [1, ..] -> go_pos_accel
# [2, ..] -> go_head


present_pos_servos = [0,0,0,0,0,0,0,0]

##  SEND POSITIONS  ##


# Directly go postions
def go_pos(positions, speed):
	global present_pos_servos
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
def go_pos_accel(goal_pos, max_speed):
	global present_pos_servos
	steps = []
	
	# Limitleri kontrol et
	goal_pos = limit_pos(goal_pos)
	
	# Maximum donus acisini bulmak icin liste yap
	for i in range(0, len(present_pos_servos)):
		turn = goal_pos[i] - present_pos_servos[i]
		steps.append(abs(float(turn)))

	# Motorlarin ne kadar hizla hareket edeceklerini hesapla
	for i in range(0, len(present_pos_servos)):	
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
def go_head(positions, speed):
	global present_pos_servos
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
			new = 0
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
			new = 0
			t1 = abs(first-pos)
			t2 = abs(end-pos)
			if t1 > t2:
				new = end
			else:
				new = first
			positions[key] = new
			rospy.logwarn("Motion Manager (Head): Warning servo limit! ID: "+str(key+1)+" old pos: "+str(pos)+ " new pos: "+ str(new))
	return positions





## SUBSCRIBER


def callback_command(data):
	if data.data[0] == 0:
		# go_pos()
		pos_in = []
		for i in range(1,9):
			pos_in.append(data.data[i])
		go_pos(pos_in, data.data[9])
		
	elif data.data[0] == 1:
		# go_pos_accel()
		pos_in = []
		for i in range(1,9):
			pos_in.append(data.data[i])
		go_pos_accel(pos_in, data.data[9])
		
		
		
def callback_command_head(data):
	# go_head()
	pos_in = []
	for i in range(0, 1):
		pos_in.append(data.data[i])
	go_head(pos_in, data.data[2])



def main():
	global pub_servo, rate
	
	rospy.init_node('motion_servo', anonymous=True)

	pub_servo = rospy.Publisher('/serial_send_servo', Int64MultiArray, queue_size=10)
	rospy.Subscriber('/command_servo', Int64MultiArray, callback_command)
	rospy.Subscriber('/command_servo_head', Int64MultiArray, callback_command_head)
	
	rate = rospy.Rate(50)
	rospy.spin()




if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass