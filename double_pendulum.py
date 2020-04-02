import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin

#Starting conditions
length_1 = 0 #Length of top rod
length_2 = 0 #Length of bottom rod
mass_1 = 0 #mass of top ball
mass_2 = 0 #mass of bottom ball
theta_1 = 0 #angle between y-axis and top rod
theta_2 = 0 #angle between y-axis and bottom rod
omega_1 = 0 #angular velocity of top rod
omega_2 = 0 #angular velocity of bottom rod
omega_1p = 0 #angular acceleration of top rod
omega_2p = 0 #angular acceleration of bottom rod
g = 9.81

#Other parameters
iter_t = 0.1 #Increment time by 0.1 seconds each iteration
iter_period = 10 #time (seconds) for which we want to simulate the pendulum

#corresponding angular velocities for each iteration
vel_1 = []
vel_2 = []

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 6.5, 7, 8, 20])
print(length_1)

def ang_acc_1_eq (l_1, l_2, m_1, m_2, t_1, t_2, w_1, w_2):
    return -( g(2*m_1+m_2)*sin(t_1) - m_2*sin(t_1-2*t_2) - 2*sin(t_1 - t_2)*m_2*((w_2**2)*l_2 + (w_1**2)*l_1*cos(t_1 - t_2)))/(l_1 * (2*m_1 + m_2 - m_2*cos(2*t_1 - 2*t_2)))

def ang_acc_1_eq (l_1, l_2, m_1, m_2, t_1, t_2, w_1, w_2):
    return (2*sin(t_1 - t_2)*((w_1**2)*l_1*(m_1 + m_2) + g*(m_1 + m_2)*cos(t_1) + (w_2**2)*l_2*m_2*cos(t_1 - t_2))/(l_2 * (2*m_1 + m_2 - m_2 * cos(2*theta_1 - 2*theta_2)))
