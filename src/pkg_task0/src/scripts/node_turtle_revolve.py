#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pi
def move_circle():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist , queue_size=10)
    rospy.init_node('move_circle' , anonymous=True)
    rate = rospy.Rate(10)
    theta = 0
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
    def pose_callback(msg):
        print(msg.theta)
    sub = rospy.Subscriber('turtle1/pose' , Pose , pose_callback)
    pub.publish(arg)
    rospy.loginfo(pose)
    time = rospy.Time.now()
    rate = rospy.Rate(20)
    while rospy.Time.now() < time + rospy.Duration.from_sec(12):
        pub.publish(arg)
        rospy.loginfo(pose_callback)
        rate.sleep()
if __name__ == '__main__':
    try:
        move_circle()
    except rospy.ROSInterruptException:
        pass
 
