import numpy as np
import plot

"""
Follows Armando Signorini's nice Excel spreadsheet "differentials 2."
We use a set recursive equations to plot the path of a projectile moving 
under the influenced by gravity and drag.
"""

# Set up constants
n = 200 # Number of iterations
gravity = 6.67 * (10**(-11))
mass = 5.97 * (10**24)
drag_c = 0.01
dt = 1
vel = 4000
angle = np.pi/18
time = range(0,n)

# Set up starting conditions
init_x_vel= vel*np.cos(angle)
init_y_vel = vel*np.sin(angle)
init_x = 0
init_y = 6371000

# Create temporary variables and initalize them
x_vel_tmp = init_x_vel
y_vel_tmp = init_y_vel
x_tmp = init_x
y_tmp = init_y

# Initialize lists for the coordinates of the projectile
xlist = [init_x]
ylist = [init_y]
flist = [init_y]

# Two helper functions grav() and drag() used to make calculuation more readable.
def grav(coord, x_val, y_val):
    return (gravity * mass * coord)/(x_val**2 + y_val**2)**(3/2)

def drag(coord):
    return (-1) * drag_c * coord
 
# We iterate through the equations n times
for t in time:
    # Increment all variables
    x_vel = x_vel_tmp + (drag(x_vel_tmp) - grav(x_tmp, x_tmp, y_tmp))*dt
    y_vel = y_vel_tmp + (drag(y_vel_tmp) - grav(y_tmp, x_tmp, y_tmp))*dt
    x = x_tmp + x_vel_tmp*dt
    y = y_tmp + y_vel_tmp*dt
    f = (init_y ** 2 - x ** 2) ** (1/2)
    
    # Append new values to the list of coordinates
    xlist.append(x)
    ylist.append(y)
    flist.append(f)
    
    #Store new values into temp variables before the next iteration
    x_vel_tmp = x_vel
    y_vel_tmp = y_vel
    x_tmp = x
    y_tmp = y
    f_temp = f
    
# We use my_plot from my plot.py module to graph curves
plot.my_plot(xlist,ylist, "Plot x vs y")
plot.my_plot(xlist,flist, "Plot x vs f")
