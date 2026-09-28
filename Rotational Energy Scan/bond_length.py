import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# ROTATIONAL ANGLES
# ==========================================================

# Angles used for the rotational scan.
# These would correspond to calculations performed
# in Spartan/WebMO.

angles = np.array([
    0, 15, 30, 45, 60, 75,
    90, 105, 120, 135, 150,
    165, 180
])


# ==========================================================
# QUANTUM-CHEMICAL ENERGY DATA
# ==========================================================

# Example energies from a hypothetical rotational scan.
# Replace these with energies from WebMO/Spartan.

energies = np.array([
    -100.12340,
    -100.13420,
    -100.14850,
    -100.15780,
    -100.16320,
    -100.16010,
    -100.15120,
    -100.14150,
    -100.13240,
    -100.12710,
    -100.13020,
    -100.13750,
    -100.14530
])


# ==========================================================
# RELATIVE ENERGY
# ==========================================================

# Absolute quantum energies can be very large negative
# numbers, so subtract the lowest energy to obtain
# a relative energy landscape.

minimum_energy = np.min(energies)

relative_energy = (
    energies - minimum_energy
)


# Convert Hartrees to kcal/mol.

relative_energy_kcal = (
    relative_energy * 627.509
)


# ==========================================================
# FIND MOST STABLE CONFORMATION
# ==========================================================

minimum_index = np.argmin(energies)

minimum_angle = angles[minimum_index]

print("====================================")
print("      Rotational Energy Scan")
print("====================================")

print()
print("Most stable rotational angle:",
      minimum_angle,
      "degrees")

print(
    "Minimum energy:",
    minimum_energy,
    "Hartrees"
)


# ==========================================================
# PRINT COMPLETE DATA TABLE
# ==========================================================

print()
print("Angle       Energy (Hartree)       Relative Energy (kcal/mol)")
print("-------------------------------------------------------------")

for i in range(len(angles)):

    print(
        f"{angles[i]:5.0f}       "
        f"{energies[i]:12.6f}             "
        f"{relative_energy_kcal[i]:8.3f}"
    )


# ==========================================================
# PLOT ENERGY LANDSCAPE
# ==========================================================

plt.plot(
    angles,
    relative_energy_kcal,
    marker="o"
)

plt.xlabel("Rotational Angle (degrees)")
plt.ylabel("Relative Energy (kcal/mol)")
plt.title("Energy vs. Rotational Angle")

plt.grid()

plt.show()


# A good practice assignment would be to perform a
# rotational scan in WebMO at additional angles,
# replace the example energies, and determine the
# lowest-energy conformation.
