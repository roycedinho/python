#program to find the element not makign a pair
# function to calculate the number that is odd occuring

def odd_occurring(arr):
    
    #initialize result
    
    res = 0
    
    #traverse the array
    for element in arr:
        #xor with the result
        res ^= element
    return res

#initialize our array
arr= []

#take array size as input
n = int(input("Enter the size of the array: "))

#take array elements as input
while(n):
    num = int(input("Enter the number: "))
    arr.append(num)
    n -= 1
    
    print("\nThe number that is not making a pair is: ", odd_occurring(arr))