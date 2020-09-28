#!/usr/bin/python

import rospy

from class_model_kobuki import KobukiModel
from class_communication import Communication
from std_msgs.msg import Float64
 
#Init of program
if __name__ == '__main__':
    
    # Boton de Parada de movimiento.
    #  Botones de movimiento: Adelante, atras, giro a la izquierda,
    # giro a la derecha.
    #  Boton de Terminacion o Salida de nodo.
    #  Topic que contenga la informacion de los parametros de 
    #  velocidad angular y lineal.

    
    rospy.init_node('kobuki_controller', anonymous=True)

    rospy.loginfo("Node init")

    # rospy.spin()
    
    kobuki = KobukiModel()
    com = Communication()
    
    # Polling+Callback
    rate = rospy.Rate(50)
    
    while(not rospy.is_shutdown()):
        # if(com.flagCmd == True):
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
            rospy.loginfo("Stopped robot")
        rate.sleep()