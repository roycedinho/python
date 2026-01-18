# program to find hcf/gcd
#enter 2 numbers

numberlargest = int(input("Enter the largest number: "))
numbersmallest = int(input("Enter the smallest number: "))

#using euclidean algorithm to find gcd
while(numbersmallest):
    numberstore = numbersmallest
    numbersmallest = numberlargest % numbersmallest
    numberlargest = numberstore
    
    print("HCF is: ", numberlargest)