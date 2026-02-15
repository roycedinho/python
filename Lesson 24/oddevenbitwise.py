# Program to check if the user entered number is odd or even using only bitwise operator

# Returns True if n is even, else False
def isEvenOdd(n):
    # XOR with 1 equals n + 1 only when n is even
    if (n ^ 1) == n + 1:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if isEvenOdd(number):
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")
