#!/usr/bin/env python3

import rospy
from gazebo_msgs.msg import Wind
from geometry_msgs.msg import Vector3

def wind_publisher():
    rospy.init_node('wind_publisher', anonymous=True)
    pub = rospy.Publisher('/gazebo/wind', Wind, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        wind_msg = Wind()
        wind_msg.header.stamp = rospy.Time.now()
        wind_msg.wind.linear = Vector3(x=1.0, y=0.0, z=0.0)  
        pub.publish(wind_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        wind_publisher()
    except rospy.ROSInterruptException:
        pass

