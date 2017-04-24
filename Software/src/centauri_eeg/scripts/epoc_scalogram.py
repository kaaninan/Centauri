#!/usr/bin/env python
#
# epoc_scalogram.py
#
# Generates a scalogram from EEG signals read from the Emotiv EPOC headset.
# Currently this only can read data from a pre-recorded ROS '.bag' file. For
# more information see: http://www.ros.org/wiki/rosbag.
#
# Usage:
#   python epoc_scalogram.py /path/to/bag/file.bag

import argparse
import numpy
import rosbag
import scipy.misc
import subprocess
import yaml

from Wavelets import Morlet
from matplotlib import cm
from matplotlib import pylab
from matplotlib import pyplot
from mpl_toolkits.mplot3d import axes3d


def read_bag(bag_location):
    # Open a bag file.
    bag = rosbag.Bag(bag_location)
    print "Bag information:"
    print bag
    print
    print

    # Get information about the .bag file.
    bag_info_command = ['rosbag', 'info', '--yaml', bag_location]
    bag_info_process = subprocess.Popen(
        bag_info_command,
        stdout=subprocess.PIPE)
    bag_info = yaml.load(bag_info_process.communicate()[0])

    # Extract the topics recorded in the .bag file.
    bag_channels = {
        topic['topic']: topic['messages']
        for topic
        in bag_info['topics']
    }

    # Setup the buffers for holding data extracted from the bag file.
    buffers = {
        topic: numpy.zeros(bag_channels[topic])
        for topic
        in bag_channels.keys()
    }
    buffer_sizes = {
        topic: 0
        for topic
        in bag_channels.keys()
    }

    # Read data from the bag file.
    messages = bag.read_messages(topics=bag_channels.keys())
    for topic, msg, t in messages:
        buffers[topic][buffer_sizes[topic]] = msg.data
        buffer_sizes[topic] += 1

    # Cleanup.
    print "Done! Read: %d messages" % sum(buffer_sizes.values())
    bag.close()

    return buffers


def draw_specgram(signal, name):
    # Use specgram.
    pylab.specgram(signal, NFFT=1024, Fs=128)
    # pylab.title(name)


def draw_scalogram(signal, name):
    # Perform a wavelet transform on the input signal.
    print "Transforming '%s' using a Morlet wavelet..." % name
    transformed = Morlet(
        signal,
        largestscale=4,
        notes=16,
        scaling='log')
    power_matrix = transformed.getpower()

    # Display the power matrix generated during the wavelet transform.
    pylab.imshow(
        power_matrix,
        cmap=pylab.cm.jet,
        aspect='auto')


def draw_3D_scalogram(signal, name, draw_contours=False):
    # Perform a wavelet transform on the input signal.
    print "Transforming '%s' using a Morlet wavelet..." % name
    transformed = Morlet(
        signal,
        largestscale=4,
        notes=16,
        scaling='log')
    power_matrix = transformed.getpower()

    # Downsample the image.
    matrix_dimensions = numpy.shape(power_matrix)
    mat_size = (matrix_dimensions[0], 1000)
    power = scipy.misc.imresize(power_matrix, mat_size)

    # Display the power matrix generated during the wavelet transform.
    fig = pyplot.figure(name)
    pyplot.title(name)
    axis = fig.gca(projection='3d')

    # Setup each axis' data.
    f = numpy.arange(mat_size[0])
    t = numpy.arange(mat_size[1])
    f_major, t_major = numpy.meshgrid(f, t)

    # Plot everything.
    axis.plot_surface(t_major, f_major, power.transpose(), rstride=8, cstride=8, alpha=0.3)
    if draw_contours:
        axis.contour(t_major, f_major, power.transpose(), zdir='z', offset=0, cmap=cm.coolwarm)
        axis.contour(t_major, f_major, power.transpose(), zdir='x', offset=0, cmap=cm.coolwarm)
        axis.contour(t_major, f_major, power.transpose(), zdir='y', offset=0, cmap=cm.coolwarm)
    axis.set_xlabel('t')
    axis.set_ylabel('f')
    axis.set_zlabel('amplitude')


if __name__ == '__main__':
    # Setup command line arguments for epoc_scalogram.
    parser = argparse.ArgumentParser(
        description='Generate a scalogram from EEG signals read from the Emotiv EPOC headset.')
    parser.add_argument('target')
    parser.add_argument('--target-type', dest='target_type', choices=['ros_topic', 'bag'], default='ros_topic')
    parser.add_argument('--display-type', dest='display_type', choices=['3d', '3d_contour', 'heatmap'], default='heatmap')
    parser.add_argument('--transform-type', dest='transform_type', choices=['morlet', 'fft'], default='fft')
    args = parser.parse_args()

    if args.target_type == 'bag':
        # Read the bag file.
        buffers = read_bag(args.target)
        print "Read buffers."

        # Only display the signal channels.
        signals = [topic for topic in buffers if 'signal' in topic]
        print "Read signals."

        # Draw 3d plots.
        if args.display_type == '3d' or args.display_type == '3d_contour':
            print "Drawing 3D plot."
            for topic in signals:
                draw_3D_scalogram(buffers[topic], topic, args.display_type == '3d_contour')

        # Draw 2d plots.
        elif args.display_type == 'heatmap':
            print "Drawing heatmap."
            pylab.figure('EEG scalograms')
            pylab.title('EEG scalograms')

            if args.transform_type == 'fft':
                for i, topic in enumerate(signals):
                    pylab.subplot(1, len(signals), i)
                    draw_specgram(buffers[topic], topic)
            elif args.transform_type == 'morlet':
                for i, topic in enumerate(signals):
                    pylab.subplot(len(signals), 1, i)
                    draw_scalogram(buffers[topic], topic)
            else:
                print "Unsupported 'transform-type': %s" % args.transform_type

        # Display everything.
        pyplot.show()

    elif args.target_type == 'ros_topic':
        # Open up listeners
        print "Listening to ros topics."
        pass
    else:
        print "Unrecognized target-type: %s" % args.target_type
