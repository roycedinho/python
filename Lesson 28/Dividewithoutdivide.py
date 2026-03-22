# program to divide two numbers without using division operator

def divide(ourdividend, ourdivisor):
    
    # check if divisor is positive or negative
    sign = (-1 if((ourdividend < 0) ^
                     (ourdivisor < 0)) else 1);
    
    # make both positve
    ourdividend = abs(ourdividend)
    ourdivisor = abs(ourdivisor)
    quotient = 0
    tempnumber= 0
    
    # go from 31 to 0 and accimilate all valid bits
    for i in range(31, -1, -1):
        if (tempnumber + (ourdivisor << i) <= ourdividend):
            tempnumber += ourdivisor << i
            quotient |= 1 << i
            
    #assuming the sign value ompued earlier is -1, negate the quotient
    if sign ==-1:
        quotient = -quotient
    return quotient

a= int(input("Enter the a for a/b: "))
b= int(input("Enter the b for a/b: "))
print("result of", a, "/", b, "is", divide(a, b))