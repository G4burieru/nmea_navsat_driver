# Software License Agreement (BSD License)
#
# Copyright (c) 2016, Rein Appeldoorn
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the names of the authors nor the names of their
#    affiliated organizations may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""Defines the main method for the nmea_socket_driver executable."""


import select
import sys
import traceback
from scapy.all import *
import rospy
from std_msgs.msg import String

from libnmea_navsat_driver.driver import RosNMEADriver
import libnmea_navsat_driver.parser

import re

nmea_str = "$GPGSA,A,3,02,10,16,18,23,26,29,32,66,81,67,68,1.30,1.10,1.10*04"

def packet_callback(packet):
    global nmea_str
    try:
        payload = packet[Raw].load
        nmea_raw = payload.decode('ascii')
        nmea_raw_splitted = nmea_raw.split("\\")
        for sentence in nmea_raw_splitted:
            try:
                if sentence[0] == '$' or sentence[0] == '!':
                    nmea_str = sentence
            except:
                pass
    except:
        pass

def main():
    """Create and run the nmea_socket_driver ROS node.

    Creates a ROS NMEA Driver and feeds it NMEA sentence strings from a UDP socket.

    :ROS Parameters:
        - ~ip (str)
            IPV4 address of the socket to open.
        - ~port (int)
            Local port of the socket to open.
        - ~timeout (float)
            The time out period for the socket, in seconds.
    """
    rospy.init_node('nmea_socket_driver_scapy')

    # pub = rospy.Publisher('nmea_sentences', String, queue_size=10)

    driver = RosNMEADriver()
    frame_id = RosNMEADriver.get_frame_id()

    # f = open("/home/vsnt/nmea_sentences_14_02_2023.txt", "w")

    # Handle incoming connections until ROS shuts down
    try:
        while not rospy.is_shutdown():
            conf.bufsize = 102400
            sniff(iface="vr-br", filter="port 10110", prn=packet_callback, count=1)
            # rospy.logerr(nmea_str)
            # pub.publish(nmea_str)
            # f.write(nmea_str)
            # print(nmea_str)
            driver.add_sentence(nmea_str, frame_id)
            # parsed_sentence = libnmea_navsat_driver.parser.parse_nmea_sentence(nmea_str)
            # print(parsed_sentence)
    except Exception:
        rospy.logerr(traceback.format_exc())
        # f.close()