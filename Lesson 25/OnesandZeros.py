# program to find the number of 1's and 0's in the binary representation of a number

#functions taking our number as imput
def numberofbits(n):
    
    ones=0
    zeros=0
    
    #while our number is grater than 0 we will check the last bit of the number and right shift
    while n:
        
        #use AND operator to check if the last bit is 1 or 0
        if (n&1==1):
            ones+=1
        else:
            zeros+=1
            
            #right shigt the number remove the last bit that we just checked above
        n>>=1
        print("\n\nOnes =", ones,"\n Zeros =", zeros)
        
number = int(input("Enter a number: "))
numberofbits(number)
