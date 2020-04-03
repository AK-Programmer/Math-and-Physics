import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, pi, ceil

#Starting conditions
length_1 = 5 #Length of top rod
length_2 = 5 #Length of bottom rod
mass_1 = 5 #mass of top ball
mass_2 = 5 #mass of bottom ball
theta_1 = - pi/2 #angle between y-axis and top rod
theta_2 = -pi/2 #angle between y-axis and bottom rod
omega_1 = 3 #angular velocity of top rod
omega_2 = -1 #angular velocity of bottom rod
omega_1p = 0 #angular acceleration of top rod
omega_2p = 0 #angular acceleration of bottom rod
g = 9.81

#Other parameters
iter_increment = 0.001 #Increment time by 0.1 seconds each iteration
current_iter = 0
iter_period = 10 #time (seconds) for which we want to simulate the pendulum

#corresponding angular velocities for each iteration
vel_1 = [omega_1]
vel_2 = [omega_2]

pos_1 = [theta_1]
pos_2 = [theta_2]
#List of times for plotting
times = [0]

def angular_acc_1_eq (l_1, l_2, m_1, m_2, t_1, t_2, w_1, w_2):
    return ( (-g)*(2*m_1+m_2)*sin(t_1) - m_2*g*sin(t_1-2*t_2) - 2*sin(t_1 - t_2)*m_2*((w_2**2)*l_2 + (w_1**2)*l_1*cos(t_1 - t_2)))   /   (l_1 * (2*m_1 + m_2 - m_2*cos(2*t_1 - 2*t_2)))

def angular_acc_2_eq (l_1, l_2, m_1, m_2, t_1, t_2, w_1, w_2):
    return (2*sin(t_1 - t_2)*((w_1**2)*l_1*(m_1 + m_2) + g*(m_1 + m_2)*cos(t_1) + (w_2**2)*l_2*m_2*cos(t_1 - t_2)))/(l_2 * (2*m_1 + m_2 - m_2 * cos(2*theta_1 - 2*theta_2)))


for i in range(ceil(iter_period / iter_increment)):
    a_1 = angular_acc_1_eq(length_1, length_2, mass_1, mass_2, pos_1[-1], pos_2[-1], vel_1[-1], vel_2[-1])
    a_2 = angular_acc_2_eq(length_1, length_2, mass_1, mass_2, pos_1[-1], pos_2[-1], vel_1[-1], vel_2[-1])

    v_1 = round(a_1 * iter_increment + vel_1[-1], 4)
    v_2 = round(a_2 * iter_increment + vel_2[-1], 4)

    vel_1.append(v_1)
    vel_2.append(v_2)

    p_1 = pos_1[-1] + v_1 * iter_increment + (a_1 * iter_increment * iter_increment)/2
    p_2 = pos_2[-1] + v_2 * iter_increment + (a_2 * iter_increment * iter_increment)/2
    pos_1.append(p_1)
    pos_2.append(p_2)

    current_iter += iter_increment
    times.append(current_iter)

fig, ax = plt.subplots()
ax.plot(times, pos_1)

fig, ax = plt.subplots()
ax.plot(times, pos_2)

print(vel_1)
"""def dual_euler (l_1, l_2, m_1, m_2, t_1, t_2, current_iter=current_iter):
    if (current_iter <= iter_period):
        vel_1.append(angular_acc_1_eq(l_1, l_2, m_1, m_2, t_1, t_2, vel_1[-1], vel_2[-1]) * iter_increment + vel_1[-1])
        vel_2.append(angular_acc_2_eq(l_1, l_2, m_1, m_2, t_1, t_2, vel_1[-1], vel_2[-1]) * iter_increment + vel_2[-1])
        current_iter += iter_increment
        times.append(current_iter)
        print(vel_1)

        dual_euler(length_1, length_2, mass_1, mass_2, theta_1, theta_2)
    else:"""



#dual_euler(length_1, length_2, mass_1, mass_2, theta_1, theta_2)
