#!/usr/bin/env python

from __future__ import print_function

# ROS imports.
import roslib
import rospy
import math
from std_msgs.msg import UInt32
from emotiv_epoc.srv import ChangeFrequency


class EpocMock(object):
    def __init__(self, initial_frequency=10):
        # Sensor channels.
        self.channels = [
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
        
        self.frequency = initial_frequency
        
        # Setup publishers.
        self.signal_publishers = {
            channel: rospy.Publisher('epoc/signal/%s' % channel, UInt32)
            for channel
            in self.channels}
        self.quality_publishers = {
            channel: rospy.Publisher('epoc/quality/%s' % channel, UInt32)
            for channel
            in self.channels}
            
        # Setup service.
        self.frequency_service = rospy.Service(
            'epoc/frequency',
            ChangeFrequency,
            self.change_frequency)
        
        # Start a ROS node.
        rospy.init_node('epoc_publish')
        
        # Start the publishing loop.
        rospy.loginfo('Starting publishing loop...')
        self.published_count = 0
        rate = rospy.Rate(128)
        init_time = rospy.get_time()
    
        while not rospy.is_shutdown():
            curr_time = rospy.get_time()
            y = math.sin(2 * math.pi * self.frequency * (curr_time - init_time))
            
            # Publish the the EEG channels and accelerometer values.
            for channel in self.channels:
                signal = UInt32(7000 + y * 1000)
                quality = UInt32(3)
                self.signal_publishers[channel].publish(signal)
                self.quality_publishers[channel].publish(quality)
    
            # Update and print information count.
            self.published_count += 1
            print('\rPublished: %d' % self.published_count, end='')
    
            rate.sleep()

    def change_frequency(self, req):
        self.frequency = req.frequency

    
if __name__ == '__main__':
    roslib.load_manifest('emotiv_epoc')
    mock = EpocMock()
