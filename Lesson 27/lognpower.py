# program to compute x^y without using math function

def computepower(x, y):
    # default total is 1
    result = 1
    
    while (y > 0):
        # if y is even
        if (y % 2 == 0):
            x = x * x
            y >>= 1
        else:
            result = result * x
            y = y - 1
    
    return result

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print("Total:", computepower(x, y))