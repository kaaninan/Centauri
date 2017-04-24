#!/usr/bin/python

from __future__ import print_function

# ROS imports.
import roslib
import rospy
from std_msgs.msg import UInt32

# TODO: Convert this to use opencv2 instead.
# Other imports.
import pygame
import pygame.font
import pygame.time

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

class EPOCSignalGapher(object):
    """
    Listens to a ROS channel and displays the data as a waveform using pygame.

    @param screen to draw to using pygame.
    @param name of the channel to listen to.
    @param vertical_position of the graph on the screen.
    @param signal_channel to listen to for waveform data.
        default: "/epoc/signal"
    @param quality_channel to listen to for channel quality data.
        default: "/epoc/quality"
    """
    def __init__(
        self,
        screen,
        name,
        position,
        size=(800, 64),
        signal_channel="/epoc/signal/",
        quality_channel="/epoc/quality/"):
        """
        Constructs an EPOCSignalGapher instance. Refer to the docstring for EPOCSignalGapher
        for more information.
        """

        # Store value parameters of this class.
        self.screen = screen
        self.name = name
        self.position = position
        self.size = size
        self.signal_channel = signal_channel
        self.quality_channel = quality_channel

        # Initialize the signal buffer.
        self.signal_range = float(1 << 13)
        self.signal_buffer = []
        self.signal_buffer_capacity = 800

        # Initialize pygame constants.
        self.vertical_display_ratio = self.size[1] / self.signal_range
        font = pygame.font.Font(None, 24)
        self.text = font.render(self.name, 1, (255, 0, 0))
        self.textpos = self.text.get_rect()
        self.textpos.centery = self.position[1] + self.size[1]

        # Setup the ROS Subscriber that provides data for this grapher.
        self.signal_subscriber = rospy.Subscriber(
            signal_channel + name,
            UInt32,
            self.update)


    def update(self, data):
        """
        Callback function that handles incoming data for the signal being graphed by this
        EPOCSignalGapher instance. Appends new data to `self.signal_buffer`.
        """

        # Drop the head of the list if the signal buffer is full.
        if len(self.signal_buffer) == self.signal_buffer_capacity:
            self.signal_buffer = self.signal_buffer[1:]

        # Add the new data to the end of the signal buffer.
        self.signal_buffer.append(data.data)


    def draw(self):
        """
        Draws the current `self.signal_buffer` to the screen.
        """

        # Do nothing is the signal buffer is empty.
        if len(self.signal_buffer) == 0:
            return

        # TODO: Why does this cause some channels to not get rendered?
        # # Draw a box around the signal.
        # pygame.draw.rect(
        #     self.screen,
        #     (0, 0, 0),
        #     (self.position[0], self.position[1], self.size[0], self.size[1]),
        #     2)

        # Draw a label for this signal.
        self.screen.blit(self.text, self.textpos)

        # Store the first point.
        first_y = self.position[1] + self.vertical_display_ratio * self.signal_buffer[0]
        previous_point = (self.position[0], first_y)
        for i, value in enumerate(self.signal_buffer):
            x = self.position[0] + i
            y = self.position[1] + self.vertical_display_ratio * value
            current_point = (x, y)

            # Draw the line segment.
            pygame.draw.line(
                self.screen,
                # TODO: Set this color based on the quality of the signal.
                (0, 255, 0),
                previous_point,
                current_point)

            previous_point = current_point


if __name__ == '__main__':
    # Initialize PyGame.
    pygame.init()
    screen = pygame.display.set_mode((40 + 800 + 40, 40 + 64 * 16 + 40))

    # Setup the signal graphers.
    graphers = {}
    for i, channel in enumerate(channels):
        graphers[channel] = EPOCSignalGapher(
            screen=screen,
            name=channel,
            position=(40, 40 + i * 64),
            size=(800, 64))

    # Start the ROS Node.
    rospy.init_node('epoc_signals')

    clock = pygame.time.Clock()
    while not rospy.is_shutdown():
        # Set the frame rate to 60 fps.
        clock.tick(30)

        # Perform the draw operation
        screen.fill((75, 75, 75))
        for channel in channels:
            graphers[channel].draw()
        pygame.display.flip()
