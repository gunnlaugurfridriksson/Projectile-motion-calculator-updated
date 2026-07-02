
# Assumptions
# - No air resistance during flight
# - Projectile lands at the same height it was launched from
# - Force is constant
# - All work done by the applied force becomes kinetic energy

import math
import matplotlib.pyplot as plt
import numpy as np

G = 9.81


# Calculations for projectile motion

def calculations_for_initial_velocity(force, distance, mass):
    """Calculates using the work-energy formula Fd = 1/2 * m * v**2"""
    initial_velocity = math.sqrt((2 * force * distance) / mass)
    return initial_velocity


def calculate_for_projectile_motion(mass, force, distance, angle_deg):
    initial_speed = calculations_for_initial_velocity(force, distance, mass)

    angle_rad = math.radians(angle_deg)

    vertical_velocity = initial_speed * math.sin(angle_rad)
    horizontal_velocity = initial_speed * math.cos(angle_rad)

    time_in_air = (vertical_velocity * 2) / G

    max_height = vertical_velocity ** 2 / (2 * G)

    length_traveled = horizontal_velocity * time_in_air

    return initial_speed, vertical_velocity, horizontal_velocity, time_in_air, max_height, length_traveled


def plot_trajectory(horizontal_velocity, vertical_velocity, time_in_air):
    t_values = np.linspace(0, time_in_air, 100)

    x_values = horizontal_velocity * t_values

    y_values = vertical_velocity * t_values - 0.5 * G * t_values**2

    plt.plot(x_values, y_values)
    plt.xlabel("Distance traveled (m)")
    plt.ylabel("Height (m)")
    plt.title("Projectile motion")
    plt.grid(True)
    plt.show()


def main():
    try:
        mass = float(input("Input mass of object (kg): "))
        force = float(input("Input force applied (N): "))
        distance = float(input("Input distance force was applied over (m): "))
        angle_deg = float(input("Input launch angle (degrees): "))
    except ValueError:
        print("Please enter numbers only. Example: 1.5")
        return

    if mass <= 0:
        print("Mass must be greater than 0.")
        return

    if force < 0 or distance < 0:
        print("Force and distance cannot be negative.")
        return
    
    if angle_deg < 0 or angle_deg > 90:
        print("Angle should be between 0 and 90 degrees.")
        return

    initial_speed, vertical_velocity, horizontal_velocity, time_in_air, max_height, range_distance = calculate_for_projectile_motion(
        mass, force, distance, angle_deg
    )

    print(f"Initial speed: {initial_speed:.3f} m/s")
    print(f"Horizontal velocity: {horizontal_velocity:.3f} m/s")
    print(f"Vertical velocity: {vertical_velocity:.3f} m/s")
    print(f"Range: {range_distance:.3f} m")
    print(f"Max height: {max_height:.3f} m")
    print(f"Time in air: {time_in_air:.3f} s")

    plot_trajectory(horizontal_velocity, vertical_velocity, time_in_air)

if __name__ == "__main__":
    main()