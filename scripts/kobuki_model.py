#!/usr/bin/python

import numpy as np

class Kobuki:

    def __init__(self):

        # Parametros ruedas
        radius = 0.035
        alpha_l = np.pi/2 # left
        beta_l  = 0
        alpha_r = -np.pi/2 # right
        beta_r  = np.pi
        l = 0.23/2 # 2l = distancia entre ruedas

        #Definicion matrices J1 y J2
        J1 = np.array([(np.sin(alpha_r+beta_r), -np.cos(alpha_r + beta_r), -l*np.cos(beta_r)),
                       (np.sin(alpha_l+beta_l), -np.cos(alpha_l + beta_l), -l*np.cos(beta_l)),
                       (np.cos(alpha_r+beta_r), np.sin(alpha_r + beta_r), l*np.sin(beta_r))])

        J2 = radius*np.identity(3)

        #Jacob_inv
        self.jacob_inv = np.matmul(np.linalg.pinv(J2),J1)


    def WheelVelocities(self,Vx,Vy,Wz):
        '''
        Funcion para calcular velocidad angular [rad/s] de las ruedas
        '''
        vel = np.array([(Vx),(Vy),(Wz)]) # Velocidad respecto centro inercial "El phi"
        vel_wheels = np.matmul(self.jacob_inv, vel)

        return vel_wheels