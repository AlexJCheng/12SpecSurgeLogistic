import matplotlib.pyplot as plt
import numpy as np

# Define the parameter range
x = np.linspace(-10, 10, 100)
l = 1
a = 0.1
k = 1
# Define the parametric equations

y = 1 / (1 + a * np.e ** (-1 * k * x))




# Create the plot
plt.figure(figsize=(6,6))
plt.plot(x, y)  # x is real, y is imaginary

# Add thick lines at x=0 and y=0
plt.axhline(0, color='black', linewidth=1)  # Horizontal line (y=0)
plt.axvline(0, color='black', linewidth=1)  # Vertical line (x=0)

# Set labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'{l}/(1+{a}e^(-{k}x))')

# Set the limits of x and y axes

plt.xlim(-10, 10)
plt.ylim(-1, 2)

# Equal aspect ratio ensures that the scale on the x-axis is the same as the y-axis
plt.gca().set_aspect('equal', adjustable='box')

# Show grid
plt.grid(True)

# Show the plot
plt.savefig(f'{l} (1+{a}e^(-{k}x)).png', dpi=300, bbox_inches='tight')
plt.show()
