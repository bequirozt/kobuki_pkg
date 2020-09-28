#!/usr/bin/python

import rospy

from kobuki_model import Kobuki
from communication_model import Communication
from std_msgs.msg import Float64
 
#Init of program
if __name__ == '__main__':
    
    rospy.init_node('kobuki_controller', anonymous=True)

    rospy.loginfo("Node init")

    kobuki = Kobuki()
    com = Communication()
    
    # Polling+Callback
    rate = rospy.Rate(50)
    while(not rospy.is_shutdown()):
        if(com.flagCmd == True):
            com.flagCmd = False
            vel2Send = kobuki.WheelVelocities(com.velX,com.velX,com.velAng)

            # Right Wheel
            msg = Float64()
            msg.data = vel2Send[0]
            com.publisherVelR.publish(msg)

            # Left Wheel
            msg = Float64()
            msg.data = vel2Send[1]
            com.publisherVelL.publish(msg)
            rospy.loginfo("Published")
            
        rate.sleep()