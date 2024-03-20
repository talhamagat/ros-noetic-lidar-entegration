#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import MultiDOFJointTrajectory, MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Transform, Twist, TwistStamped

def main():
    rospy.init_node('move_uav_node')
    pub = rospy.Publisher('/firefly/command/trajectory', MultiDOFJointTrajectory, queue_size=10)
    rate = rospy.Rate(10)  # Hz

    # Hedef konumu ve hızı oluşturun
    desired_position = Transform()
    desired_position.translation.x = 3.0  # Sabit konum (sağa doğru)
    desired_position.translation.y = 0.0  # Sabit konum (ileri doğru)
    desired_position.translation.z = 1.0  # Yükseklik

    desired_velocity = Twist()
    desired_velocity.linear.x = 3.0  # Sabit hız (ileri doğru)
    desired_velocity.linear.y = 0.0  # Sabit hız (sağa doğru)
    desired_velocity.linear.z = 1.0  # Dikey hız

    # Mesaj oluşturun ve hedef konumu ve hızı ekleyin
    trajectory_msg = MultiDOFJointTrajectory()
    trajectory_msg.header.stamp = rospy.Time.now()
    trajectory_msg.points.append(MultiDOFJointTrajectoryPoint(transforms=[desired_position], velocities=[desired_velocity]))

    # Mesajı yayınlayın
    while not rospy.is_shutdown():
        pub.publish(trajectory_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

