#!/usr/bin/env python
import rospy, os, sys, roslib
from centauri_sound.msg import SoundCommand
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient



soundAssets = '/home/robot/Music/'
# duration of yak throttle
throttle = 1 # seconds

def sound_translator(data):
	print data
	global allow_yak
	
	if rospy.Time.now() <= allow_yak: # Throttles yak to avoid
		print("Sound throttled")      # SoundClient segfault
		return
	
	allow_yak = rospy.Time.now() + rospy.Duration.from_sec(throttle)
	
	if data.cmd == "wav":
		soundhandle.playWave(soundAssets + data.param)
	if data.cmd == "say":
		soundhandle.say(data.param)
	if data.cmd == "builtin":
		soundhandle.play(int(data.param))
	if data.cmd == "stop":
		soundhandle.stopAll()


def init():
	rospy.init_node('sound_server', anonymous = True)
	global allow_yak
	allow_yak = rospy.Time.now()
	rospy.Subscriber('sound_cmd', SoundCommand, sound_translator)
	# Volume Up
	volume = rospy.get_param('~volume')
	os.system("pacmd set-sink-volume 0 "+ str(volume))
	rospy.spin()


if __name__ == '__main__':
	soundhandle = SoundClient()
	rospy.sleep(1)

	init()