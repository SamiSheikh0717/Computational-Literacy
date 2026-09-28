import numpy as np


# ==========================================================
# MOLECULAR COORDINATES
# ==========================================================

# Coordinates are given in Angstroms.
# These coordinates represent an example H2O molecule.

atoms = ["O", "H", "H"]

coordinates = np.array([
    [0.0000,  0.0000,  0.0000],   # Oxygen
    [0.7586,  0.0000,  0.5043],   # Hydrogen 1
    [-0.7586, 0.0000,  0.5043]    # Hydrogen 2
])


# ==========================================================
# BOND LENGTH
# ==========================================================

def bond_length(atom1, atom2):
    # Subtract the coordinates to create a vector
    # between the two atoms.

    vector = atom2 - atom1

    # Calculate the magnitude of the vector.

    return np.linalg.norm(vector)


OH1 = bond_length(
    coordinates[0],
    coordinates[1]
)

OH2 = bond_length(
    coordinates[0],
    coordinates[2]
)


# ==========================================================
# BOND ANGLE
# ==========================================================

def bond_angle(atom1, center, atom2):
    # Create vectors pointing from the central atom
    # toward the two outer atoms.

    vector1 = atom1 - center
    vector2 = atom2 - center

    # Calculate the dot product of the vectors.

    dot_product = np.dot(vector1, vector2)

    # Calculate the magnitude of each vector.

    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)

    # Use the dot-product relationship:
    #
    # cos(theta) = A dot B / |A||B|

    cosine = dot_product / (
        magnitude1 * magnitude2
    )

    # Prevent small numerical errors from producing
    # an invalid value slightly outside [-1, 1].

    cosine = np.clip(cosine, -1.0, 1.0)

    # Convert the angle from radians to degrees.

    return np.degrees(np.arccos(cosine))


HOH = bond_angle(
    coordinates[1],
    coordinates[0],
    coordinates[2]
)


# ==========================================================
# RESULTS
# ==========================================================

print("====================================")
print("      Molecular Geometry")
print("====================================")

print("Molecule: H2O")

print()
print("Bond Lengths:")
print("O-H 1:", round(OH1, 4), "Å")
print("O-H 2:", round(OH2, 4), "Å")

print()
print("Bond Angle:")
print("H-O-H:", round(HOH, 2), "degrees")


# ==========================================================
# LEWIS STRUCTURE INFORMATION
# ==========================================================

valence_electrons = {
    "H": 1,
    "O": 6
}

total_electrons = (
    valence_electrons["O"]
    + valence_electrons["H"]
    + valence_electrons["H"]
)

print()
print("Lewis Structure Information:")
print("Total valence electrons:", total_electrons)

print()
print("The Lewis structure can be used to predict")
print("the molecular geometry before comparing it")
print("with the calculated geometry.")

# A good practice assignment would be to replace the
# coordinates with coordinates exported from WebMO
# for another molecule and calculate its bond lengths
# and bond angles.
