#!/usr/bin/env python

import rospy, time, thread
from std_msgs.msg import *

## PROCESS
# 1. Komut /command_dc uzerinden (hiz_sag, hiz_sol, yon_sag, yon_sol) olarak gelir / go()
# 2. Yon degisimine gore durdurma ve yeniden hizlandirma / go() -> accel()
# 2. Degismiyorsa direk belirlenen hiza gitme / go() -> accel()
# 3. Step sayisina gore her adimda degisecek hiz hesaplanir ve thread acilir / accel() -> send_hw()
# 4. Thread bitene kadar running=1 yapilir ve o sirada gelen komutlar islenmez / send_hw()

## COMMAND FLOW
# callback_command() -> go() -> accel() -> send_hw()
# Externally -> distance_back() & distance_front() || If the obstacle is visible, stop


# SUBSCRIBER #
def callback_command(data):
	rospy.loginfo("callback dc")
	go(data.data[0], data.data[1], data.data[2], data.data[3])
	
	
	
# Yon degisiyorsa durdur ve tekrar hizlandir
def go(goal_right, goal_left, goal_dir_right, goal_dir_left):
	global dir_left, dir_right
	
	# Yon degisikligini algila
	if running == 0:
	
		if dir_left != goal_dir_left and dir_right == goal_dir_right:
			# Sadece sol
			accel(pwm_right, 0) # Dur
			dir_left = goal_dir_left
			
		elif dir_left == goal_dir_left and dir_right != goal_dir_right:
			# Sadece sag
			accel(0, pwm_left) # Dur
			dir_right = goal_dir_right
			
		elif dir_left != goal_dir_left and dir_right != goal_dir_right:
			# Her ikisi degisiyor
			accel(0, 0) # Dur
			dir_right = goal_dir_right
			dir_left = goal_dir_left
			
		# Her ihtimalde istenen yere git
		accel(goal_right, goal_left) # Hizlan
		
	else:
		rospy.loginfo("Callback DC - Already running!")



# Adim basina dusen pwmi hesapla ve thread a gonder
def accel(goal_right, goal_left):
	global running, pwm_right
	
	# For calibration
	if dir_left == 0 and dir_right == 0 and pwm_right > 49:
		pwm_right = pwm_right - 50
	
	# Komutlar ust uste binmesin
	running = 1
	
	# Hiz ne kadar degisecek
	step_right = goal_right - pwm_right
	step_left = goal_left - pwm_left
	
	# Adim basina degisecek hiz
	single_step_right = step_right/float(step)
	single_step_left = step_left/float(step)
	
	try:
		thread.start_new_thread( send_hw, (single_step_left, single_step_right) )
	except:
		rospy.logerr(docname + " -> couldn't executed")
		
	

# Her adim icin motorlara komut gonder
def send_hw(single_step_left, single_step_right):
	global pwm_right, pwm_left, running
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
		time.sleep(sleep/float(10))
	running = 0





# Onune engel cikarsa serial iletisimini kesme komutu yolla

def distance_back(data):
	global dis_back, stop_cmd_back
	dis_back = data.data
	limit = rospy.get_param('~distance_limit')
	if dis_back <= limit and stop_cmd_back == 0:
		stop_cmd_back = 1
		data = Int64()
		data.data = stop_cmd_back
		pub_stop.publish(data)
		rate.sleep()
	elif dis_back > limit and stop_cmd_back == 1:
		stop_cmd_back = 0
		data = Int64()
		data.data = stop_cmd_back
		pub_stop.publish(data)
		rate.sleep()
	
	
def distance_front(data):
	global dis_front, stop_cmd_front
	dis_front = data.data
	limit = rospy.get_param('~distance_limit')
	if dis_front <= limit and stop_cmd_front == 0:
		stop_cmd_front = 1
		data = Int64()
		data.data = stop_cmd_front
		pub_stop.publish(data)
		rate.sleep()
	elif dis_front > limit and stop_cmd_front == 1:
		stop_cmd_front = 0
		data = Int64()
		data.data = stop_cmd_front
		pub_stop.publish(data)
		rate.sleep()


def default():
	global pwm_right, pwm_left, dir_left, dir_right, running, stop_cmd_back, stop_cmd_front, sleep, step
	
	pwm_right = 0
	pwm_left = 0
	dir_left = 0
	dir_right = 0
	
	running = 0
	stop_cmd_back = 0
	stop_cmd_front = 0
	
	step = rospy.get_param('~step')
	sleep = rospy.get_param('~sleep')


def main():
	
	global pub_dc, pub_stop, rate
	
	rospy.init_node('motion_dc', anonymous=True)
	
	pub_dc = rospy.Publisher('/serial_send_dc', Int64MultiArray, queue_size=10)
	pub_stop = rospy.Publisher('/serial_stop_dc', Int64, queue_size=10)
	
	rospy.Subscriber('/distance_back', Int64, distance_back)
	rospy.Subscriber('/distance_front', Int64, distance_front)
	
	rospy.Subscriber('/command_dc', Int64MultiArray, callback_command)
	
	rate = rospy.Rate(100) # Only use stop dc when low distance
	
	default()
	
	time.sleep(4)
	# Stop when starting
	go(0, 0, 0, 0)
	
	rospy.spin()
	




if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass