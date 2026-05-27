# Takes user input for the remaining fuel
fuel_level = float(input("Enter current fuel level (in liters): "))
low_fuel_threshold = 10.0

if fuel_level < low_fuel_threshold:
    print("WARNING: Low fuel! Please refuel soon.")