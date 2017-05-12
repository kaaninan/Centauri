#!/usr/bin/env python

import rospy, serial, thread, time, os
from datetime import timedelta
from std_msgs.msg import *

# DEFAULT

docname = os.path.basename(__file__)

stop_cmd = 0 # Acil durumda serialden gondermeyi keser

# Serial

def connect():
	global board
	port = rospy.get_param('~port')
	baudrate = rospy.get_param('~baudrate')
	board = serial.Serial(port, baudrate)
	if(board is None):
		rospy.logfatal(docname+ " couldn't connect serial!")
	board.flush()
	time.sleep(0.1)
	board.write("99&")
	time.sleep(0.3)
	board.write("99&")
	time.sleep(0.5)


def serial_incoming():
	gelen = ""
	while not rospy.is_shutdown():
		gelen = board.readline()
		parse_data(gelen)
		

def parse_data(data):
	try:
		arr = data.split("!")
		if(arr[0] == "1"):
			dis = arr[1].split("-")
			dis2 = dis[1].split("\/")
			
			data_back = Int64()
			data_back.data = int(dis[0])
			pub_dis_back.publish(data_back)
			
			data_front = Int64()
			data_front.data = int(dis[1])
			pub_dis_front.publish(data_front)
					
		elif(arr[0] == "2"):
			data_battery = Int64()
			data_battery.data = int(arr[1])
			pub_volt.publish(data_battery)
	except:
		pass


# Queries

def query_battery():
	while not rospy.is_shutdown():
		board.write("2&")
		time.sleep(1)
		
def query_distance():
	while not rospy.is_shutdown():
		board.write("1&")
		time.sleep(0.2)
		
# def uptime():
# 	while not rospy.is_shutdown():
# 		with open('/proc/uptime', 'r') as f:
# 			uptime_seconds = float(f.readLine().split()[0])
# 			uptime_string = str(timedelta(seconds = uptime_seconds))
# 			
# 			data = String()
# 			data.data = uptime_string
# 			pub_uptime.publish(data)
# 		time.sleep(1)
	
	
def send_dc(data):
	global stop_cmd
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
	if stop_cmd == 0:
		board.write("3 "+str(write)+"&")
		time.sleep(0.01)
		board.write("4 "+str(sol_hiz)+"&")
		time.sleep(0.01)
		board.write("5 "+str(sag_hiz)+"&")
		time.sleep(0.01)


def send_servo(data):
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


def call_stop(data):
	global stop_cmd
	stop_cmd = data.data
	if stop_cmd == 1:
		rospy.logwarn("Hardware Warning! Don't send command to board. No distance")
		board.write("3 0&")
		time.sleep(0.01)
		board.write("4 0&")
		time.sleep(0.01)
		board.write("5 0&")
		time.sleep(0.01)
		

# SYSTTEM FUNC		

def call_reboot(data):
	time.sleep(1)
	rospy.loginfo("Reboot!")
	os.system("sudo reboot")
	
def call_shutdown(data):
	time.sleep(1)
	rospy.loginfo("Shutdown!")
	board.write("9&")


def main():
	global pub_dis_front, pub_dis_back, pub_volt, pub_uptime

	rospy.init_node('serial_connection', anonymous=True)
	
	connect()
		
	# Publish
	pub_dis_front = rospy.Publisher('/distance_front', Int64, queue_size=10)
	pub_dis_back = rospy.Publisher('/distance_back', Int64, queue_size=10)
	pub_volt = rospy.Publisher('/battery_voltage', Int64, queue_size=10)
	pub_uptime = rospy.Publisher('/uptime', Int64, queue_size=10)
	
	# Subscribe
	rospy.Subscriber("/serial_send_dc", Int64MultiArray, send_dc)
	rospy.Subscriber("/serial_send_servo", Int64MultiArray, send_servo)
	rospy.Subscriber("/serial_stop_dc", Int64, call_stop)
	rospy.Subscriber("/reboot", Empty, call_reboot)
	rospy.Subscriber("/shutdown", Empty, call_shutdown)
	
	
	try:
		thread.start_new_thread( query_battery, () )
		thread.start_new_thread( query_distance, () )
		thread.start_new_thread( serial_incoming, () )
# 		thread.start_new_thread( uptime, () )
	except:
		rospy.logerr(docname + " -> couldn't executed query_battery & serial_incoming")
		
	
	rospy.loginfo("Started hardware -> serial_connection")
	
	rospy.spin()
	


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass