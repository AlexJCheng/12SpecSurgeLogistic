import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy.abc import j

# Define the parameter range
x = np.linspace(-10, 10, 200)
a = 1
k = 1
# Define the parametric equations

y = a * x * np.e ** (-1 * k * x)
#yj = a * j * np.e ** (-1 * k * j)
#print(sp.Derivative())

# Create the plot
plt.figure(figsize=(6,6))
plt.plot(x, y)  # x is real, y is imaginary

# Plotting the maximum
plt.plot(1/k, max(y), marker = 'o')

# Add thick lines at x=0 and y=0
plt.axhline(0, color='black', linewidth=1)  # Horizontal line (y=0)
plt.axvline(0, color='black', linewidth=1)  # Vertical line (x=0)

# Set labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'{a}xe^(-{k}x)')

# Set the limits of x and y axes

plt.xlim(-1, 10)
plt.ylim(-1, 2)

# Equal aspect ratio ensures that the scale on the x-axis is the same as the y-axis
plt.gca().set_aspect('equal', adjustable='box')

# Show grid
plt.grid(True, alpha = 1)

# Show the plot
plt.savefig(f'S{a}xe^(-{k}x).png', dpi=300, bbox_inches='tight')
plt.show()

print(max(y))
