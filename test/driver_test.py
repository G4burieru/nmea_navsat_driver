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
        nmea_str = "!AIVDO,1,1,,,B:UOH3P00?>VsvLf>c6SkwqUoP06,0*6D"
        frame_id = RosNMEADriver.get_frame_id()
        self.driver.add_sentence(nmea_str, frame_id)

test = Test()
rospy.spin() 