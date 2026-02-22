#program to check if hte nth bit of a number is set or not

def setornot(number, n):
    
    #make a mask variable by left shifting 1 by k-1 times and check if (n AND mask) equals 1 or 0
    if number & (1 << (n-1)):
        print("\n SET")
    else:
        print("\n NOT SET")
        
number = int(input("Enter a number: "))
n = int(input("Enter the bit number: "))
setornot(number, n)