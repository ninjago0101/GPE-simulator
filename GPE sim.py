import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11

def calculate_gpe(M, m, r):
    return -G * M * m / r

def plot_gpe(M, m, r_range):
    r_values = np.linspace(r_range[0], r_range[1], 500)
    gpe_values = [calculate_gpe(M, m, r) for r in r_values]

    plt.figure(figsize=(8, 6))
    plt.plot(r_values, gpe_values, label="Gravitational Potential Energy")
    plt.title("Gravitational Potential Energy vs Distance")
    plt.xlabel("Distance (m)")
    plt.ylabel("Gravitational Potential Energy (J)")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    print("Welcome to the Gravitational Potential Energy Simulator!")
    try:
        M = float(input("Enter the mass of the planet (kg): "))
        m = float(input("Enter the mass of the object (kg): "))
        r_min = float(input("Enter the minimum distance from the planet (m): "))
        r_max = float(input("Enter the maximum distance from the planet (m): "))

        print("\nSimulating gravitational potential energy... Please wait!")
        plot_gpe(M, m, (r_min, r_max))

    except ValueError:
        print("Invalid input! .")

if __name__ == "__main__":
    main()
