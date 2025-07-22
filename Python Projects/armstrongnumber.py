# Get input from the user
num = int(input("Enter a number: "))

# Convert the number to a string to find the number of digits
num_str = str(num)
num_digits = len(num_str)

# Calculate the sum of each digit raised to the power of number of digits
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

# Check if the number is an Armstrong number
if sum_of_powers == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
