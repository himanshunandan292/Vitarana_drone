#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
def move_circle():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist , queue_size=10)
    rospy.init_node('move_circle' , anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        arg = Twist()
        pose = Pose()
        w = 1.0
        r = 2.0
        theta = w/r
        arg.linear.x = w
        arg.linear.y = 0
        arg.linear.z = 0
        arg.angular.x = 0
        arg.angular.y = 0
        arg.angular.z = theta
        pub.publish(arg)
        print(pose.orientation.w)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        move_circle()
    except rospy.ROSInterruptException:
        pass
 
