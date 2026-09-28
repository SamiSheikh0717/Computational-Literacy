# CHEM 150 Module: WebMO Energy and Dipole Moment Analysis

## Goals

By completing this activity, students will:

- Read numerical results from a WebMO calculation.
- Convert energy from Hartrees to kJ/mol and kcal/mol.
- Calculate the magnitude of a molecular dipole moment.
- Use Python functions to organize repeated calculations.
- Connect computational output to chemically meaningful quantities.

## Activity Explanation

WebMO can report molecular energies in Hartrees and dipole moments as separate x, y, and z components.

This activity uses Python to process those values.

The energy is converted using:

**1 Hartree = 2625.50 kJ/mol**

and

**1 Hartree = 627.509 kcal/mol**

The magnitude of the dipole moment is calculated from its Cartesian components:

**|μ| = √(μₓ² + μᵧ² + μ_z²)**

The program therefore demonstrates how raw computational output can be converted into quantities that are easier to interpret and compare.

Students should replace the example values with the results from their own WebMO calculation.

## Learning Check

1. What unit is the original energy reported in?
2. Why are energy conversion factors necessary?
3. What do the x, y, and z dipole components represent?
4. Why is the square-root expression used to calculate dipole magnitude?
5. What changes when a different molecule's WebMO results are entered?

## Extension

Run a WebMO calculation for another molecule and enter its energy and dipole components into the program. Compare the calculated properties of the two molecules.
