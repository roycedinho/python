# Get the number of terms from the user
n = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
a, b = 0, 1

# Print the Fibonacci series
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
