import matplotlib.pyplot as plt
import numpy as np

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

#corresponding angular velocities for each iteration
vel_1 = []
vel_2 = []

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
print(length_1)
