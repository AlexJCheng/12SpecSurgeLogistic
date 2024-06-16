import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Plot size
ymin = 0
ymax = 2
ystep = 0.5
xmin = 0
xmax = 10
xstep = 1

# Define the parameter range
x = np.linspace(xmin, xmax, (xmax-xmin)*10)
l = 1
a = 1
k = 1

# Define the parametric equations
y = l / (1 + a * np.e ** (-1 * k * x))

# Create the plot
fig, ax = plt.subplots(figsize=(6,6))
line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], 'ro')  # This is the point that will follow the plot

# Plotting the maximum
#plt.plot(1/k, max(y), marker = 'o')

# Set labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'{l} / (1 + {a}e^(-{k}x))')

# Add thick lines at x=0 and y=0
plt.axhline(0, color='black', linewidth=1)  # Horizontal line (y=0)
plt.axvline(0, color='black', linewidth=1)  # Vertical line (x=0)

# Set the limits of x and y axes
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

# Equal aspect ratio ensures that the scale on the x-axis is the same as the y-axis
#ax.set_aspect('equal', adjustable='box')

# Show grid
plt.grid(which = 'major', linewidth = 0.5)
plt.xticks(np.arange(xmin,xmax+xstep,xstep))
plt.yticks(np.arange(ymin,ymax+ystep,ystep))

# Initialization function for the animation
def init():
    line.set_data([], [])
    return line,

# Animation function which updates figure data
def animate(i):
    line.set_data(x[:i], y[:i])
    point.set_data(x[i], y[i])  # Update the point's position here
    return line, point,

# Call the animator
ani = FuncAnimation(fig, animate, init_func=init, frames=len(x), interval=20, blit=True)

# Save the animation as a gif
ani.save(f'L{l}(1 + {a}e^(-{k}x)).gif', writer="ffmpeg")

# Show the plot
plt.show()
