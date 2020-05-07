import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, pi, ceil, floor

#Starting conditions
length_1 = 1 #Length of top rod
length_2 = 1 #Length of bottom rod

mass_1 = 2 #mass of top ball
mass_2 = 2 #mass of bottom ball
theta_1 = pi/2 #angle between y-axis and top rod
theta_2 = pi/2 + 0.2 #angle between y-axis and bottom rod
omega_1 = 0 #angular velocity of top rod
omega_2 = 0 #angular velocity of bottom rod
omega_1p = 0 #angular acceleration of top rod
omega_2p = 0 #angular acceleration of bottom rod
g = 9.81

#Other parameters
iter_increment = 0.0001 #Increment time by 0.1 seconds each iteration
current_iter = 0
iter_period = 15 #time (seconds) for which we want to simulate the pendulum

#corresponding angular velocities for each iteration
vel_1 = [omega_1]
vel_2 = [omega_2]

#in x-y pairs --> [[x, y], [x, y], [x, y]]
pos_1 = [[length_1 * sin(theta_1), length_1 * cos(theta_1)]]
pos_2 = [[pos_1[0][0] + length_2 * sin(theta_2), pos_1[0][1] + length_2 * cos(theta_2)]]

#List of times for plotting
times = [0]


def angular_acc_1_eq (l_1, l_2, m_1, m_2, t_1, t_2, w_1, w_2):
    return ((-g)*(2*m_1+m_2)*sin(t_1) - m_2*g*sin(t_1-2*t_2) - 2*sin(t_1 - t_2)*m_2*((w_2**2)*l_2 + (w_1**2)*l_1*cos(t_1 - t_2)))   /   (l_1 * (2*m_1 + m_2 - m_2*cos(2*t_1 - 2*t_2)))

def angular_acc_2_eq (l_1, l_2, m_1, m_2, t_1, t_2, w_1, w_2):
    return (2*sin(t_1 - t_2)*((w_1**2)*l_1*(m_1 + m_2) + g*(m_1 + m_2)*cos(t_1) + (w_2**2)*l_2*m_2*cos(t_1 - t_2)))/(l_2 * (2*m_1 + m_2 - m_2 * cos(2*theta_1 - 2*theta_2)))


#Variables that are updated each loop to keep track of the current angular position of each mass
current_pos_1 = theta_1
current_pos_2 = theta_2
#Run the simulation and save x-y position of each mass at each increment
for i in range(ceil(iter_period / iter_increment)):
    a_1 = angular_acc_1_eq(length_1, length_2, mass_1, mass_2, current_pos_1, current_pos_2, vel_1[-1], vel_2[-1])
    a_2 = angular_acc_2_eq(length_1, length_2, mass_1, mass_2, current_pos_1, current_pos_2, vel_1[-1], vel_2[-1])

    v_1 = round(a_1 * iter_increment + vel_1[-1], 4)
    v_2 = round(a_2 * iter_increment + vel_2[-1], 4)

    vel_1.append(v_1)
    vel_2.append(v_2)

    p_1 = current_pos_1 + v_1 * iter_increment + (a_1 * iter_increment * iter_increment)/2
    p_2 = current_pos_2 + v_2 * iter_increment + (a_2 * iter_increment * iter_increment)/2

    current_pos_1 = p_1
    current_pos_2 = p_2

    pos_1.append([length_1 * sin(p_1), length_1 * cos(p_1)])
    pos_2.append([pos_1[i+1][0] + length_2 * sin(p_2), pos_1[i+1][1] + length_2 * cos(p_2)])
    current_iter += iter_increment
    times.append(current_iter)

counter = 0
for i in range (0, ceil(iter_period / iter_increment), floor((1 / iter_increment * 30))):
    fig, ax = plt.subplots(figsize=(10, 10))
    line_1 = plt.Line2D((0, round(pos_1[i][0])), (1, round(pos_1[i][1])), lw=3)
    circle_1 = plt.Circle((round(pos_1[i][0]), round(pos_1[i][1])), radius=0.1, fc='b')
    line_2 = plt.Line2D((round(pos_1[i][0]), round(pos_2[i][0])), (round(pos_1[i][1]), round(pos_2[i][0])), lw=3)
    circle_2 = plt.Circle((round(pos_2[i][0]), round(pos_2[i][1])), radius=0.1, fc='b')
    line_1.set_color('b')
    line_2.set_color('b')
    plt.gca().add_line(line_1)
    plt.gca().add_patch(circle_1)
    plt.gca().add_line(line_2)
    plt.gca().add_patch(circle_2)
    plt.axis('equal')
    ax.set(xlim=(-2, 2), ylim=(-2, 3))
    fig.savefig('./images/double_pendulum/f_'+str(counter)+'.png')
    counter+=1
    plt.close()


#Create gifs
import imageio

frames = []
for i in range(counter):
    frames.append('f_'+str(counter)+'.png')

gif = []
for filename in frames:
    gif.append(imageio.imread('./images/double_pendulum/'+filename))
imageio.mimsave('./images/double_pendulum/sim.gif', gif)

fig1, ax = plt.subplots()
fig1.savefig('./images/double_pendulum/f_'+str(counter)+'.png')
