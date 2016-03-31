#!/usr/bin/env python
import rospy
from geometry_msgs.msg import TwistStamped, Twist

def accel():
	rospy.init_node('accel_node')
	pub = rospy.Publisher('/g500/twist',TwistStamped,queue_size=10)
	
	subtwist = Twist()
	twist = TwistStamped()
	subtwist.linear.x = 1.0
	twist.twist = subtwist

	pub.publish(twist)   

	rospy.loginfo("About to be moving forward!")
       	for i in range(30):
           pub.publish(twist)
           rospy.sleep(0.1) # 30*0.1 = 3.0
	
if __name__ == '__main__':
	accel()
    
