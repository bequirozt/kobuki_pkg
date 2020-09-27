#!/usr/bin/python

import rospy

from class_model_kobuki import KobukiModel
from class_communication import class_communication
 
#Init of program
if __name__ == '__main__':
    
    rospy.init_node('Nodo_Kobuki', anonymous=True)

    rospy.loginfo("Node init")

    rospy.spin()