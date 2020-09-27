#!/usr/bin/python3

import rospy
from sensor_msgs.msg import LaserScan

from std_msgs.msg import Float64 #Flotante que reciben las ruedas
from geometry_msgs.msg import Twist #Definir cinematica ruedas

import numpy
from rospy.numpy_msg import numpy_msg

from class_model_kobuki import KobukiModel

class communication:

    def __init__(self):

        #Atributos
        self.topicSubscriber = "/cmd_vel"

        self.topicPublisherL = "controller_left_wheel/command"
        self.topicPublisherR = "controller_right_wheel/command"

        self.velX   = 0.0
        self.velY   = 0.0
        self.velAng = 0.0

        self.modelKobuki = KobukiModel()

        self.flagCmd = False

        #Publicador
        self.publisherVelL = rospy.Publisher(self.topicPublisherL, numpy_msg(Float64))
        self.publisherVelR = rospy.Publisher(self.topicPublisherR, numpy_msg(Float64))

        #Subscriptor
        rospy.Subscriber(self.topicSubscriber, numpy_msg(Twist), self.cmd_vel_callback)

        #Polling+Callback
        rate = rospy.Rate(60)
        while(not rospy.is_shutdown()):
            if(self.flagCmd == True):
                self.flagCmd = False
                vel2Send = self.modelKobuki.WheelVelocities(self.velX,self.velX,self.velAng)


                #Rueda derecha (right)
                msg = Float64()
                msg.data = vel2Send[0]
                self.publisherVelR.publish(msg)

                #Rueda derecha (right)
                msg = Float64()
                msg.data = vel2Send[1]
                self.publisherVelL.publish(msg)
            rate.sleep()


        #Callback de velocidades 
        def cmd_vel_callback(self,cmd):

            self.velX   = cmd.linear.x
            self.velY   = cmd.linear.y
            self.velAng = cmd.angular.z

            self.flagCmd = True;

            