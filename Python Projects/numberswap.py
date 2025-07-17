# Input three numbers from the user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

# Show original values
print("Before swapping:")
print("a =", a, "b =", b, "c =", c)

# Swap the numbers
a, b, c = c, a, b

# Show swapped values
print("After swapping:")
print("a =", a, "b =", b, "c =", c)
