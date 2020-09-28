#!/usr/bin/python

import numpy

import rospy
from rospy.numpy_msg import numpy_msg

from std_msgs.msg import Float64 #Flotante que reciben las ruedas
from geometry_msgs.msg import Twist #Definir cinematica ruedas

from class_model_kobuki import KobukiModel

class Communication:

    def __init__(self):

        # Atributos
        self.topicSubscriber = "/cmd_vel"
        self.topicPublisherL = "left_wheel_controller/command"
        self.topicPublisherR = "right_wheel_controller/command"
        self.velX   = 0.0
        self.velY   = 0.0
        self.velAng = 0.0
        self.flagCmd = False

        # Atributos Publisher-Subscriber
        self.publisherVelL = rospy.Publisher(self.topicPublisherL, numpy_msg(Float64))
        self.publisherVelR = rospy.Publisher(self.topicPublisherR, numpy_msg(Float64))
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

            