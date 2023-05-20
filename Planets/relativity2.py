import numpy as np
import matplotlib.pyplot as plt

def calculate_orbit(semi_major_axis, eccentricity, num_points):
    # Constants
    G = 6.67430e-11  # Gravitational constant (m^3 kg^−1 s^−2)
    M = 1.989e30  # Mass of the Sun (kg)
    c = 299792458  # Speed of light (m/s)

    # Calculate time step
    period = 2 * np.pi * np.sqrt(semi_major_axis ** 3 / (G * M))
    dt = period / num_points

    # Initialize arrays
    times = np.linspace(0, period, num=num_points)
    r = np.zeros((num_points, 2))
    v = np.zeros((num_points, 2))

    # Initial conditions
    r[0] = [semi_major_axis * (1 + eccentricity), 0]
    v[0] = [0, np.sqrt((G * M * (1 - eccentricity)) / (semi_major_axis * (1 + eccentricity)))]

    # Calculate the orbit
    precession = 0.0
    for i in range(1, num_points):
        # Distance from the Sun
        distance = np.linalg.norm(r[i - 1])

        # Newtonian acceleration due to gravity
        acceleration_newton = (-G * M / distance ** 3) * r[i - 1]

        # General relativistic correction to acceleration
        acceleration_gr = ((3 * G * M) / (c**2 * distance**5)) * np.dot(r[i - 1], r[i - 1]) * r[i - 1]

        # Total acceleration
        acceleration = acceleration_newton + acceleration_gr

        # Update velocity and position using the Verlet method
        v[i] = v[i - 1] + acceleration * dt
        r[i] = r[i - 1] + v[i] * dt

        # Update the precession
        precession += (6 * np.pi * G * M) / (distance * c**2)

    return times, r, precession

# Orbital parameters for Mercury
semi_major_axis = 5.791e10  # meters
eccentricity = 0.2056

# Number of points to calculate
num_points = 10000

# Calculate the orbit and precession
times, r, precession = calculate_orbit(semi_major_axis, eccentricity, num_points)

# Print the precession angle in arcseconds
print("Precession of the perihelion: {:.2f} arcseconds".format(precession * 180 * 3600 / np.pi))

# Plot the orbit
plt.plot(r[:, 0], r[:, 1])
plt.xlabel('X (meters)')
plt.ylabel('Y (meters)')
plt.title('Orbit of Mercury around the Sun (with General Relativity correction)')
plt.gca().set_aspect('equal')
plt.show()
