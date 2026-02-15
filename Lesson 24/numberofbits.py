# Program to find the number of bits present in a number

def numberofBits(n):
    
    count = 0
    
    # Right shift the number till it becomes 0
    while n:
        count += 1
        n >>= 1
    
    return count

number = int(input("Enter a number: "))
print("Number of bits in", number, "is", numberofBits(number))
