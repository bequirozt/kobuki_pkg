#!/usr/bin/python3

import rospy
from sensor_msgs.msg import LaserScan

from std_msgs.msg import Float64 #Flotante que reciben las ruedas
from geometry_msgs.msg import Twist #Definir cinematica ruedas

import numpy
from rospy.numpy_msg import numpy_msg

class communication:

    def __init__(self):

        #Atributos
        self.topicSubscriber = "/cmd_vel"

        self.topicPublisherL = "controller_left_wheel/command"
        self.topicPublisherR = "controller_right_wheel/command"

        self.velX   = 0.0
        self.velY   = 0.0
        self.velAng = 0.0

        #Publicador
        self.publisherVelL = rospy.Publisher(self.topicPublisherL, numpy_msg(Float64))
        self.publisherVelL = rospy.Publisher(self.topicPublisherR, numpy_msg(Float64))

        #Subscriptor
        rospy.Subscriber(self.topicSubscriber, numpy_msg(Twist), self.cmd_vel_callback)

        #Callback de velocidades 
        def cmd_vel_callback(self,cmd):

            self.velX   = Twist.linear.x
            self.velY   = Twist.linear.y
            self.velAng = Twist.angular.z