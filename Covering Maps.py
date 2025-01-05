import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters
theta = np.linspace(0, 2 * np.pi, 500)  # Angle for the circle
z = np.linspace(0, 4 * np.pi, 500)  # Z-coordinates for the helix
radius = 1

# Circle (base space)
x_circle = radius * np.cos(theta)
y_circle = radius * np.sin(theta)

# Helix (covering space)
x_helix = radius * np.cos(z)
y_helix = radius * np.sin(z)

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the helix
ax.plot(x_helix, y_helix, z, label='Helix (Covering Space)', color='blue')

# Plot the base circle
ax.plot(x_circle, y_circle, np.zeros_like(theta), label='Circle (Base Space)', color='orange', linestyle='--')

# Add projection lines from the helix to the circle
for i in range(0, len(z), 50):
    ax.plot([x_helix[i], x_circle[i % len(theta)]],
            [y_helix[i], y_circle[i % len(theta)]],
            [z[i], 0], color='gray', linestyle='dotted', alpha=0.5)

# Labels and legend
ax.set_title('Visualization of a Covering Map')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
