# Dimensional Analysis Practice
# This program converts a measurement from one unit to another.

def km_to_m(km):
    # 1 kilometer = 1000 meters
    return km * 1000


def m_to_cm(m):
    # 1 meter = 100 centimeters
    return m * 100


def cm_to_mm(cm):
    # 1 centimeter = 10 millimeters
    return cm * 10


# Ask the user for a distance in kilometers
distance_km = float(input("Enter a distance in kilometers: "))

# Convert kilometers → meters
distance_m = km_to_m(distance_km)

# Convert meters → centimeters
distance_cm = m_to_cm(distance_m)

# Convert centimeters → millimeters
distance_mm = cm_to_mm(distance_cm)

# Display the results
print("Distance in meters:", distance_m, "m")
print("Distance in centimeters:", distance_cm, "cm")
print("Distance in millimeters:", distance_mm, "mm")

# Challenge:
# Modify the program so that the user enters a distance in kilometers
# and the program converts it directly to millimeters.
