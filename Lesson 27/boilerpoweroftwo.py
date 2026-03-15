# program to check if a number is a power of two

def power2(number):
    
    #as the power of two will have only one bit set, we can use the property that n & (n-1) will be 0 for powers of two
    if (number== 0):
        return 0
    if ((number & (~(number - 1))) == number):
        return 1
    return 0

#take input from user
number = int(input("Enter a number: "))

if (power2(number)):
    print(number, "is a power of two.")
else:
    print(number, "is not a power of two.")