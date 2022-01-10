from typing import List
import numpy as np
import matplotlib.pyplot as plt
from math import pi

"""
    Adaptative PD controler for inverted pendulum
"""

"""
class Pendulum:
    def __init__(self,m,l,b) -> None:
        self.mass = m
        self.length = l
        self.friction = b
        self.gravity = 9.81

    def movePendulum(self) -> None:
        pass

"""

# desired position
th_d = pi/4

# neuron weights ( these will be the control gains kp, kd  respectively)
w_1 = 4.0
w_2 = 0.0

# Learning Factor
eta_1 = 0.001
eta_2 = 0.01

# error auxiliar
e_old = 0

# sampling time, seconds, number of iterations
t = 0.01
s = 50
n = s/t

# initial position and velocity
th_i = 0
thd_i = 0

# pendulum parameters (mass, length, gravity, friction coefficient  respectively)
m = 0.5
l = 0.85
g = 9.81
B = 0.2









# x = np.array([[1, 2, 3], [3, 2, 1]])

# r,c = np.shape(x)
# print(r,c)



