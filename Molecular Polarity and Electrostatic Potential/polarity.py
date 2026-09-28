import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# ATOMIC POSITIONS
# ==========================================================

# Example water molecule.
# Coordinates are in Angstroms.

oxygen = np.array([0.000, 0.000])

hydrogen1 = np.array([0.758, 0.504])

hydrogen2 = np.array([-0.758, 0.504])


# ==========================================================
# PARTIAL CHARGES
# ==========================================================

# Example partial charges.
# These would ideally be obtained from the chosen
# computational method.

q_oxygen = -0.84
q_hydrogen1 = 0.42
q_hydrogen2 = 0.42


# ==========================================================
# DIPOLE MOMENT
# ==========================================================

def dipole_component(position, charge):
    # Calculate the contribution of an atomic charge
    # to the molecular dipole.

    return position * charge


dipole_O = dipole_component(
    oxygen,
    q_oxygen
)

dipole_H1 = dipole_component(
    hydrogen1,
    q_hydrogen1
)

dipole_H2 = dipole_component(
    hydrogen2,
    q_hydrogen2
)


dipole = (
    dipole_O
    + dipole_H1
    + dipole_H2
)


dipole_magnitude = np.linalg.norm(dipole)


# ==========================================================
# ELECTROSTATIC POTENTIAL
# ==========================================================

def electrostatic_potential(
    x,
    y,
    positions,
    charges
):

    potential = np.zeros_like(x)

    # Calculate the contribution from every atomic charge.

    for position, charge in zip(
        positions,
        charges
    ):

        distance = np.sqrt(
            (x - position[0])**2
            +
            (y - position[1])**2
        )

        # Prevent division by zero directly on an atom.

        distance = np.maximum(
            distance,
            0.05
        )

        potential += charge / distance

    return potential


positions = np.array([
    oxygen,
    hydrogen1,
    hydrogen2
])


charges = np.array([
    q_oxygen,
    q_hydrogen1,
    q_hydrogen2
])


# ==========================================================
# CREATE A 2-D GRID
# ==========================================================

x = np.linspace(-3, 3, 300)

y = np.linspace(-3, 3, 300)

X, Y = np.meshgrid(
    x,
    y
)


# Calculate electrostatic potential everywhere
# on the grid.

potential = electrostatic_potential(
    X,
    Y,
    positions,
    charges
)


# ==========================================================
# RESULTS
# ==========================================================

print("====================================")
print("      Electrostatic Potential")
print("====================================")

print()
print("Dipole X component:",
      dipole[0])

print("Dipole Y component:",
      dipole[1])

print()
print("Dipole magnitude:",
      dipole_magnitude)


# ==========================================================
# ELECTROSTATIC POTENTIAL MAP
# ==========================================================

plt.figure(figsize=(8, 6))

contour = plt.contourf(
    X,
    Y,
    potential,
    levels=50
)

plt.colorbar(
    contour,
    label="Electrostatic Potential"
)

# Plot the atoms.

plt.scatter(
    oxygen[0],
    oxygen[1],
    s=200,
    label="O"
)

plt.scatter(
    hydrogen1[0],
    hydrogen1[1],
    s=100,
    label="H"
)

plt.scatter(
    hydrogen2[0],
    hydrogen2[1],
    s=100,
    label="H"
)

plt.xlabel("x position (Å)")
plt.ylabel("y position (Å)")

plt.title(
    "Electrostatic Potential Map"
)

plt.legend()

plt.axis("equal")

plt.show()


# A good practice assignment would be to obtain
# atomic partial charges and coordinates from a
# WebMO calculation and use them to generate a
# new electrostatic potential map.
