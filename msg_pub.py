#!/usr/bin/env python
from my_robot_controller.msg import position
import rospy

def talker():
    pub = rospy.Publisher('movement_topic', position, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        movement = position()
        movement.linear_speed = (1.0) # set linear speed
        movement.direction = (90.0) # set direction in degrees
        rospy.loginfo("publishing has begun")
        rospy.loginfo(movement)
        pub.publish(movement)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker() 
    except rospy.ROSInterruptException:
        pass
