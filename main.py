import math

def read_number(prompt, allow_zero=False):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a number, using a dot for decimals.")
            continue

        if not math.isfinite(value):
            print("Please enter a finite number.")
        elif value > 0 or (allow_zero and value == 0):
            return value
        elif allow_zero:
            print("The value must be zero or greater.")
        else:
            print("The value must be greater than zero.")


print("Formula Student Vehicle Basics Calculator\n")

vehicle_mass = read_number("Vehicle mass [kg]: ")
speed_kmh = read_number("Speed [km/h]: ", allow_zero=True)
corner_radius = read_number("Corner radius [m]: ")
braking_deceleration = read_number("Braking deceleration [m/s²]: ")
cg_height = read_number("CG height [m]: ")
wheelbase = read_number("Wheelbase [m]: ")

# Convert speed from km/h to m/s.
speed_ms = speed_kmh / 3.6

# Lateral acceleration for a constant-radius corner.
lateral_acceleration = speed_ms ** 2 / corner_radius
lateral_acceleration_g = lateral_acceleration / 9.81

# Ideal stopping distance with constant braking deceleration.
braking_distance = speed_ms ** 2 / (2 * braking_deceleration)

# Braking shifts vertical load from the rear axle to the front axle.
load_transfer = vehicle_mass * braking_deceleration * cg_height / wheelbase

print("\n----------------------------------------")
print("VEHICLE DYNAMICS RESULTS")
print("----------------------------------------")
print(f"\nSpeed:\n{speed_ms:.2f} m/s")
print(f"\nLateral acceleration:\n{lateral_acceleration:.2f} m/s²")
print(f"{lateral_acceleration_g:.2f} g")
print(f"\nIdeal braking distance:\n{braking_distance:.2f} m")
print(f"\nLongitudinal load transfer:\n{load_transfer:.2f} N")
print("\n----------------------------------------")
