#program to find two numbers that are odd occurring

def printtwoodd(arr,size):  

#xor of 2 will hold xor of the two odd occurring numbers
    xorof2 = arr[0]

#these will hold the two odd occurring numbers
x = 0
y = 0

#this will hold the rightmost set bit in xorof2
setbit = 0

for i in range(1,size):
    xorof2 = xorof2 ^ arr[i]
setbit = xorof2 & ~(xorof2 - 1)

# if number is having set bit at location we need then xor it with x else y
for i in range(size):
    if (arr[i] & setbit):
        x = x ^ arr[i]
    else:
        y = y ^ arr[i]
        
print("The two ODD occurring numbers are: ", x, " and ", y)

#create an empty array
arr = []
#take array size as input
arr_size = int(input("Enter the size of the array: "))
for i in range(arr_size):
    z = int(input("Enter the element: "))
    arr.append(z)
    
printtwoodd(arr, arr_size)