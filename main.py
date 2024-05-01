import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup initial inputs and parameters
v0 = 0
theta = 0
try:
    v0 = float(input("Input initial velocity: "))
    theta = np.deg2rad(float(input("Input initial angle : ")))
except TypeError:
    print("Please input correct data types.")

dt = 0.01
g = 9.81

x_max = (2 * v0 ** 2 * np.cos(theta) * np.sin(theta)) / g
y_max = (v0**2*(np.sin(theta)**2)) / (2 * g)
t_max = (2 * v0**2 * np.sin(theta)) / g

fig, ax = plt.subplots()
line, = ax.plot([], [], 'o', ls='dashed', markevery=[0,-1], ms=5)

def init():
    line.set_data([], [])

# Animation function to calculate as t increases.
def animate(i):
    t = np.linspace(0, i*dt, 50)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    line.set_data(x, y)
    return line

ani = animation.FuncAnimation(fig, animate, interval=25, init_func=init, frames=400)

ax.set_xlim(0, x_max)
ax.set_ylim(0, y_max)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.title('Simple Projectile Motion')

plt.text(0, y_max, 'Max Height: ' + str(y_max))
plt.text(0, y_max - (y_max/16), 'Max Distance: ' + str(x_max))
plt.text(0, y_max - (y_max/32), 'Trajectory Time' + str(t_max))
plt.show()