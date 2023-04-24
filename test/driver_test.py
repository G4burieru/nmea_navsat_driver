import select
import traceback
from scapy.all import *
from std_msgs.msg import String
import time
import os
import sys

if 'ROS_NAMESPACE' not in os.environ:
    # Default namespace if not set
    # Note, didn't need to check sys.argv for `__ns:=...`,
    # it seems __ns:= takes precidence over ROS_NAMESPACE

    os.environ['ROS_NAMESPACE'] = '/nmea'


import rospy

from libnmea_navsat_driver.driver import RosNMEADriver
import libnmea_navsat_driver.parser

import re

nmea_str = ''

class Test:
    def __init__(self) :
        rospy.init_node('driver_test', anonymous= False)

        self.driver = RosNMEADriver()
        self.timer_pub_msg = rospy.Timer(rospy.Duration(1), self.callback_timer_publish_msg)

    def callback_timer_publish_msg(self, event):
        while(True):
            with open('sensor_msgs.txt', 'r') as file:
                for line in file:
                    nmea_str = line.strip()
                    frame_id = RosNMEADriver.get_frame_id()
                    self.driver.add_sentence(nmea_str, frame_id)
                    time.sleep(1/10)

                    

test = Test()
rospy.spin() 