#!/usr/bin/python3

import numpy as np

class KobukiModel:

    def __init__(self):

        #Ruedas.
        radius =  #*-*-*-*-* Pendiente *-*-*-*-*-*-*-*-*

        #Rueda izquierda (left)

        alpha_l = np.pi/2
        beta_l  = 0
        L_l     =   #*-*-*-*-* Pendiente *-*-*-*-*-*-*-*-*

        #Rueda derecha (Right)

        alpha_r = -np.pi/2
        beta_r  = np.pi
        L_r     =  #*-*-*-*-* Pendiente *-*-*-*-*-*-*-*-*

        #Definicion matrices J1 y J2


        J1 = np.array([(np.sin(alpha_r+beta_r), -np.cos(alpha_r + beta_r), -l*np.cos(beta_r)),
              (np.sin(alpha_l+beta_l), -np.cos(alpha_l + beta_l), -l*np.cos(beta_l)),
              (np.cos(alpha_r+beta_r), np.sin(alpha_r + beta_r), l*np.sin(beta_r))])

        J2 = radius*np.identity(3)

        #Jacob_inv

        self.Jacob_inv = np.matmul(np.linalg.pinv(J2),J1)

        #Calculo de velocidades de las ruedas

        def WheelVelocities(Vx,Vy,Wz):

            Vel = np.array([(Vx),(Vy),(Wz)]) # Velocidad respecto centro inercial

            VelWheels = np.matmul(self.Jacob_inv, Vel)

            return VelWheels