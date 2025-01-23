import numpy as np
import matplotlib.pyplot as plt

# Given values of n
n_values = [0, 1, 2, 3, 7, 10, 17, 20, 33, 50, 99]

# Compute the phase angles
theta_values = [0.08 * np.pi * n - 0.25 * np.pi for n in n_values]

# Compute the phasor locations (points on the unit circle)
phasor_locations = [np.exp(1j * theta) for theta in theta_values]

# Extract real and imaginary parts for plotting
x = [np.real(z) for z in phasor_locations]
y = [np.imag(z) for z in phasor_locations]

# Plot the unit circle
circle = plt.Circle((0, 0), 1, color='blue', fill=False, linestyle='--')
fig, ax = plt.subplots()
ax.add_patch(circle)

# Plot the phasor locations
ax.scatter(x, y, color='red', label='Phasor Locations')

# Annotate the points with their corresponding n values
for i, n in enumerate(n_values):
    ax.text(x[i], y[i], f'n={n}', fontsize=8, ha='right')

# Set plot limits and labels
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title('Phasor Locations on the Unit Circle')
ax.legend()

plt.grid()
plt.show()