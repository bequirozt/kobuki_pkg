#!/usr/bin/python

import numpy

import rospy
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import Float64 
from geometry_msgs.msg import Twist
from kobuki_model import Kobuki

class Communication:

    def __init__(self):

        # Atributos
        self.topicSubscriber = "kobuki/cmd_vel"
        self.topicPublisherL = "left_wheel_controller/command"
        self.topicPublisherR = "right_wheel_controller/command"
        self.velX   = 0.0
        self.velY   = 0.0
        self.velAng = 0.0
        self.flagCmd = False

        # Atributos Publisher-Subscriber
        self.publisherVelL = rospy.Publisher(self.topicPublisherL, Float64)
        self.publisherVelR = rospy.Publisher(self.topicPublisherR, Float64)
        #Subscriptor
        rospy.Subscriber(self.topicSubscriber, numpy_msg(Twist), self.cmd_vel_callback)
        

    def cmd_vel_callback(self,cmd):
        '''
        Callback de velocidades    
        '''
        self.velX   = cmd.linear.x
        self.velY   = cmd.linear.y
        self.velAng = cmd.angular.z
        self.flagCmd = True

            