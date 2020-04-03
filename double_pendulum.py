import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, pi, ceil

#Starting conditions
length_1 = 1 #Length of top rod
length_2 = 1 #Length of bottom rod
mass_1 = 2 #mass of top ball
mass_2 = 2 #mass of bottom ball
theta_1 = pi/2 #angle between y-axis and top rod
theta_2 = pi/2 #angle between y-axis and bottom rod
omega_1 = 0 #angular velocity of top rod
omega_2 = 0 #angular velocity of bottom rod
omega_1p = 0 #angular acceleration of top rod
omega_2p = 0 #angular acceleration of bottom rod
g = 9.81

#Other parameters
iter_increment = 0.0001 #Increment time by 0.1 seconds each iteration
current_iter = 0
iter_period = 30 #time (seconds) for which we want to simulate the pendulum

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

for t_iter in range(100):
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

    fig1, ax1 = plt.subplots()
    plt.title("Angle between the vertical axis and the first mass")
    ax1.plot(times, pos_1)
    fig1.savefig('./images/double_pendulum/t_1-'+str(t_iter)+'.png')
    plt.close()

    fig2, ax2 = plt.subplots()
    plt.title("Angle between the vertical axis and the second mass")
    ax2.plot(times, pos_2)
    fig2.savefig('./images/double_pendulum/t_2-'+str(t_iter)+'.png')
    plt.close()

    theta_2 += 0.01
    current_iter=0
    pos_1 = [theta_1]
    pos_2 = [theta_2]
    vel_1 = [omega_1]
    vel_2 = [omega_2]
    times=[0]


#Create gifs
import imageio

t_1_filenames = []
for i in range(100):
    t_1_filenames.append("t_1-"+str(i)+".png")
    t_1_filenames.append("t_1-"+str(i)+".png")
    t_1_filenames.append("t_1-"+str(i)+".png")
    t_1_filenames.append("t_1-"+str(i)+".png")
    t_1_filenames.append("t_1-"+str(i)+".png")

t_1images = []

for filename in t_1_filenames:
    t_1images.append(imageio.imread('./images/double_pendulum/'+filename))
imageio.mimsave('./images/double_pendulum/t_1.gif', t_1images)

t_2_filenames = []
for i in range(100):
    t_2_filenames.append("t_2-"+str(i)+".png")
    t_2_filenames.append("t_2-"+str(i)+".png")
    t_2_filenames.append("t_2-"+str(i)+".png")
    t_2_filenames.append("t_2-"+str(i)+".png")
    t_2_filenames.append("t_2-"+str(i)+".png")

t_2images = []

for filename in t_2_filenames:
    t_2images.append(imageio.imread('./images/double_pendulum/'+filename))
imageio.mimsave('./images/double_pendulum/t_2_v2.gif', t_2images)
