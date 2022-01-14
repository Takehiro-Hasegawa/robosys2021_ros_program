#!/usr/bin/env python3 
## coding: UTF-8

import rospy
from std_msgs.msg import String

def cb(message):
	rospy.loginfo("句を表示 [%s]", message.data)

rospy.init_node('chrrev')
sub = rospy.Subscriber('chrter', String, cb)
rospy.spin()
