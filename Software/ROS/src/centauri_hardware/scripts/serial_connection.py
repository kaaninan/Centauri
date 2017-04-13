#!/usr/bin/env python

import rospy
import serial
import thread
import time
import os
from std_msgs.msg import *

# DEFAULT
port = "/dev/ttyS1"
baudrate = 19200

docname = os.path.basename(__file__)


# Serial

def connect(port, baudrate):
	global board
	board = serial.Serial(port, baudrate)
	board.flush()
	if(board is None):
		rospy.logfatal(docname+ " couldn't connect serial!")


def serial_incoming():
	gelen = ""
	while not rospy.is_shutdown():
		gelen = board.readline()
		parse_data(gelen)
		

def parse_data(data):
	arr = data.split("!")
	if(arr[0] == "1"):
		dis = arr[1].split("-")
		dis2 = dis[1].split("\/")
		
		data_back = Int64()
		data_back.data = int(dis[0])
		pub_dis_back.publish(data_back)
		
		data_front = Int64()
		data_front.data = int(dis[0])
		pub_dis_front.publish(data_front)
				
	elif(arr[0] == "2"):
		data_battery = Int64()
		data_battery.data = int(arr[1])
		pub_volt.publish(data_battery)



# Queries

def query_battery():
	while not rospy.is_shutdown():
		board.write("2&")
		time.sleep(1)
		
def query_distance():
	board.write("1&")
	
	
def send_dc(data):
	sag_yon = data.data[0]
	sag_hiz = data.data[1]
	sol_yon = data.data[2]
	sol_hiz = data.data[3]
	
	write = 0
	
	if(sag_yon == 1 and sol_yon == 1):
		write = 1
	elif(sag_yon == 1 and sol_yon == 0):
		write = 2
	elif(sag_yon == 0 and sol_yon == 1):
		write = 3
	elif(sag_yon == 0 and sol_yon == 0):
		write = 4
	
	# Send Board
	board.write("3 "+str(write)+"&")
	time.sleep(0.01)
	board.write("4 "+str(sol_hiz)+"&")
	time.sleep(0.01)
	board.write("5 "+str(sag_hiz)+"&")
	time.sleep(0.01)


def send_servo(data):
	rospy.loginfo(data)
	servo_id = data.data[0]
	servo_pos = data.data[1]
	servo_speed = data.data[2]
	
	# Send Board
	board.write("6 "+str(servo_id)+"&")
	time.sleep(0.01)
	board.write("7 "+str(servo_pos)+"&")
	time.sleep(0.01)
	board.write("8 "+str(servo_speed)+"&")
	time.sleep(0.01)




def main():
	global pub_dis_front, pub_dis_back, pub_volt

	rospy.init_node('serial_connection', anonymous=True)
	
	connect(port, baudrate)
		
	# Publish
	pub_dis_front = rospy.Publisher('/distance_front', Int64, queue_size=10)
	pub_dis_back = rospy.Publisher('/distance_back', Int64, queue_size=10)
	pub_volt = rospy.Publisher('/battery_voltage', Int64, queue_size=10)
	
	# Subscribe
	rospy.Subscriber("/serial_query_distance", Empty, query_distance)
	rospy.Subscriber("/serial_send_dc", Int64MultiArray, send_dc)
	rospy.Subscriber("/serial_send_servo", Int64MultiArray, send_servo)
	
	
	try:
		thread.start_new_thread( query_battery, () )
		thread.start_new_thread( serial_incoming, () )
	except:
		rospy.logerr(docname + " -> couldn't executed query_battery")
		
	
	rospy.loginfo("Started hardware -> serial_connection")
	
	rospy.spin()
	


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass