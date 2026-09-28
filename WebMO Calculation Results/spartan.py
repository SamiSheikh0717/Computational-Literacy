import math

# Molecular information obtained from the WebMO calculation

molecule = "H2O"                 # Store the molecule being studied
charge = 0                       # Store the molecular charge
multiplicity = 1                 # Store the spin multiplicity
energy_hartree = -76.421         # Store the calculated energy in Hartrees

# Dipole moment components obtained from the calculation

dx = 0.00                        # x-component of the dipole moment
dy = 1.85                        # y-component of the dipole moment
dz = 0.00                        # z-component of the dipole moment


def hartree_to_kj(energy):
    # Convert energy from Hartrees to kJ/mol
    return energy * 2625.50


def hartree_to_kcal(energy):
    # Convert energy from Hartrees to kcal/mol
    return energy * 627.509


def calculate_dipole(x, y, z):
    # Calculate the magnitude of the molecular dipole
    return math.sqrt(x**2 + y**2 + z**2)


energy_kj = hartree_to_kj(energy_hartree)
energy_kcal = hartree_to_kcal(energy_hartree)

dipole = calculate_dipole(dx, dy, dz)


print("====================================")
print("      WebMO Calculation Results")
print("====================================")

print("Molecule:", molecule)
print("Charge:", charge)
print("Multiplicity:", multiplicity)

print()
print("Energy:")
print("Hartrees:", energy_hartree)
print("kJ/mol:", energy_kj)
print("kcal/mol:", energy_kcal)

print()
print("Dipole Moment:")
print("X:", dx, "D")
print("Y:", dy, "D")
print("Z:", dz, "D")
print("Magnitude:", dipole, "D")

# A good practice assignment would be to run another molecule
# in WebMO and replace the example values with its calculated
# energy and dipole components.
