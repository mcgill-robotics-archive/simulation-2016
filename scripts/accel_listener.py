#!/usr/bin/env python
import rospy
from geometry_msgs.msg import *
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def accel_listener():
	rospy.init_node('accel_listener',anonymous=True)
	sub = rospy.Subscriber('/dataNavigator', String, callback)
	rospy.spin()
if __name__ == '__main__':
	accel_listener()
   	
