import select
import sys
import traceback
from scapy.all import *
import rospy
from std_msgs.msg import String

from libnmea_navsat_driver.driver import RosNMEADriver
import libnmea_navsat_driver.parser

import re

class Test:
    def __init__(self):
        rospy.init_node('driver_test', anonymous= False)

        self.driver = RosNMEADriver()
        self.timer_pub_msg = rospy.Timer(rospy.Duration(1), self.callback_timer_publish_msg)

    def callback_timer_publish_msg(self, event):
        nmea_str = "$GPGSA,A,3,02,10,16,18,23,26,29,32,66,81,67,68,1.30,1.10,1.10*04"
        frame_id = RosNMEADriver.get_frame_id()
        self.driver.add_sentence(nmea_str, frame_id)

test = Test()
rospy.spin() 