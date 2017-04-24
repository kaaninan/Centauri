#!/usr/bin/env python

from __future__ import print_function

# ROS imports.
import roslib
import rospy
from std_msgs.msg import Header
from std_msgs.msg import UInt32
from emotiv_epoc.msg import EEGFrame

# Other imports.
import argparse
import gevent
from emokit.emotiv import Emotiv

# Sensor channels.
channels = [
    'F3',
    'FC6',
    'P7',
    'T8',
    'F7',
    'F8',
    'T7',
    'P8',
    'AF4',
    'F4',
    'AF3',
    'O2',
    'O1',
    'FC5',
    'X',
    'Y'
]


def epoc_publish_frames():
    # Setup ROS publisher.
    publisher = rospy.Publisher('epoc/frames', EEGFrame)

    # Open a connection to the Emotiv EPOC.
    headset = Emotiv(display_output=False, is_research=True, write=False)
    gevent.sleep(1)

    # Initialize ROS node+publisher.
    rospy.init_node('epoc_publish')

    # Start the publishing loop.
    rospy.loginfo('Starting publishing loop...')
    published_count = 0
    try:
        while not rospy.is_shutdown():
            # Get the next packet from the EPOC.
            packet = headset.dequeue()
            
            if packet is not None:

	            frame_header = Header(published_count, rospy.Time.now(), '/epoc')
	            frame_accel_x = packet.sensors['X']['value']
	            frame_accel_y = packet.sensors['Y']['value']
	            frame_signals = [
	                packet.sensors[channel]['value']
	                for channel in channels]
	            frame_qualities = [
	                packet.sensors[channel]['quality']
	                for channel in channels]
	            frame = EEGFrame(
	                frame_header,
	                frame_accel_x,
	                frame_accel_y,
	                14,
	                channels,
	                frame_signals,
	                frame_qualities)
	
	            # Publish the the EEG channels and accelerometer values.
	            publisher.publish(frame)
	
	            # Update and print information count.
	            published_count += 1
	            print('\rPublished: %d' % published_count, end='')
	
	            gevent.sleep(0)
    except rospy.ROSInterruptException:
        headset.close()


if __name__ == '__main__':
    epoc_publish_frames()
