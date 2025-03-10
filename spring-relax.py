import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# constants
k = 10 
m = 0.5  
c = 2
x0 = [0, 0.1, 0.75, 0.8, 0.9, 1]  # initial position
dt = 0.01  # iota
t_max = 5

# time array
t = np.arange(0, t_max, dt)

n_nodes = len(x0)
x = np.array(x0) 
y = np.zeros(n_nodes)
v = np.zeros(n_nodes) 

# Create a plot
fig, ax = plt.subplots()
line, = ax.plot([], [], 'bo--', lw=1)
ax.set_xlabel('Position (m)')
ax.set_title('Relaxation of Spring Nodes')

for i in range(1,len(t)):

    x_new = np.copy(x)
    v_new = np.copy(v)

    # Loop over the internal nodes (not the first and last ones)
    for j in range(1, n_nodes - 1):
        F_left = k * (x[j - 1] - x[j])
        F_right = k * (x[j + 1] - x[j])
        F_damping = -c * v[j]
        F_net = F_left + F_right + F_damping  # Net force on the node

        a = F_net / m  # Acceleration
        v_new[j] = v[j] + a * dt  # Update velocity for node j
        x_new[j] = x[j] + v_new[j] * dt  # Update position for node j

    # Boundary conditions: assume the ends of the spring are fixed
    x_new[0] = x0[0] 
    x_new[-1] = x0[-1] 

    # Update the position and velocity arrays
    x = x_new
    v = v_new

    # Update the plot data for animation
    line.set_data(x,y) 
    ax.relim() 
    ax.autoscale_view()
    print(i,t[i])
    plt.pause(dt)

plt.show()



