#!/usr/bin/python3

import rospy

from class_model_kobuki import KobukiModel
from class_communication import class_communication
 
#Init of program
if__name__== '__main__':

    
    rospy.init_node('Nodo_rycsv', anonymous=True)
 #   LIDAR_RYCSV()

    rospy.loginfo("Node init")

    rospy.spin()