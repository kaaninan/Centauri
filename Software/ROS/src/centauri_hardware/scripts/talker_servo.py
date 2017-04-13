#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import *

def talker():
	pub = rospy.Publisher('/serial_send_servo', Int64MultiArray, queue_size=10)

	rospy.init_node('talker', anonymous=True)

	rate = rospy.Rate(50) # 10hz
	
	present_pos_servos = [0,0,0,0,0,0,0,0]
# 	present_pos_servos = []


		
	motion_first = [420, 630, 880, 600, 370, 140, 512, 520]
	
	motion_two = [703, 430, 500, 400, 630, 512, 490, 489]
	
	walk_one = [400, 512, 880, 400, 450, 450, 400, 520]
	walk_two = [700, 480, 600, 400, 450, 450, 600, 520]
	
	def go_pos(motion):
		for key, pos in enumerate(motion):
			data = Int64MultiArray()
			data.data = []
			data.data.append(int(key+1)) # ID
			data.data.append(int(pos)) # POS
			data.data.append(100) # SPEED
# 			rospy.loginfo(data)
			pub.publish(data)
			rate.sleep()
			present_pos_servos[key] = pos
		
	go_pos(walk_one)
# 	time.sleep(2)
# 	go_pos(walk_one)
# 	time.sleep(1)
# 	go_pos(walk_two)
# 	time.sleep(1)
# 	go_pos(walk_one)	
	
	## ZAMANA GORE MOTOR POS HESAPLAMA VE GONDERME
	def pos_calculate(present_motor_data, new_motor_data, adim_sayisi):
		
		tek_adim = [] # Her motorun bir dongude donecegi derece
	
		for i in range(0, len(present_motor_data)):
			# Her adimda kac derece hareket edecek
			degisecek_derece = new_motor_data[i] - present_motor_data[i]
			tek_adim.append(float(degisecek_derece) / adim_sayisi)
	
	
		for i in range(0, adim_sayisi):
			# Her bir adimda motorlarin gitmesi gereken pozisyon
	
			for a in range(0, len(present_motor_data)):
			
				new_pos = present_motor_data[a] + round(tek_adim[a], 0)
				present_motor_data[a] = new_pos

				data = Int64MultiArray()
				data.data = []
				data.data.append(a+1) # ID
				data.data.append(new_pos) # POS
				data.data.append(100) # SPEED
				pub.publish(data)
				rate.sleep()


# 	pos_calculate(present_pos_servos, motion_two, 20)
# 	time.sleep(2)
# 	pos_calculate(present_pos_servos, motion_first, 5)
	
	
# 	for single in motion:
# 		for key, pos in enumerate(single):
# 			data = Int64MultiArray()
# 			data.data = []
# 			data.data.append(key+1) # ID
# 			data.data.append(pos) # POS
# 			data.data.append(100) # SPEED
# 			rospy.loginfo(data)
# 			pub.publish(data)
# 			rate.sleep()
# 	
# 	
# 	speed = 512
# 	
# 	for d in range(1,4):
# 		for a in range(1,2):
# 			for pos in range(400, 700, 20):
# 				data = Int64MultiArray()
# 				data.data = []
# 				data.data.append(3) # ID
# 				data.data.append(pos) # POS
# 				data.data.append(speed) # SPEED
# 				pub.publish(data)
# 				rate.sleep()
# 				
# # 				data = Int64MultiArray()
# # 				data.data = []
# # 				data.data.append(2) # ID
# # 				data.data.append(pos) # POS
# # 				data.data.append(speed) # SPEED
# # 				pub.publish(data)
# # 				rate.sleep()
# 				
# 				data = Int64MultiArray()
# 				data.data = []
# 				data.data.append(1) # ID
# 				data.data.append(pos) # POS
# 				data.data.append(speed) # SPEED
# 				pub.publish(data)
# 				rate.sleep()
# 				
# 			for pos in range(700, 400, -20):
# 				data = Int64MultiArray()
# 				data.data = []
# 				data.data.append(3) # ID
# 				data.data.append(pos) # POS
# 				data.data.append(speed) # SPEED
# 				pub.publish(data)
# 				rate.sleep()
# 				
# 				data = Int64MultiArray()
# 				data.data = []
# 				data.data.append(1) # ID
# 				data.data.append(pos) # POS
# 				data.data.append(speed) # SPEED
# 				pub.publish(data)
# 				rate.sleep()
	

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass