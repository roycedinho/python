def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm = abs(num1 * num2) // find_gcd(num1, num2)

print(f"The LCM is: {lcm}")