print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

pi = 3.14159

radius = float(input("Enter radius: "))

area = pi * radius ** 2
circumference = 2 * pi * radius

print("Area =" , area)
print("Circumference =", circumference)