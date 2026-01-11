#program to find inf a number is an armstrong number

#take input from the user
number=int(input("INpur your number: "))

#calculate number of digits
digits = len

#initialize result variable
resultnumber=0

#find the sum of the a^digits of each digit
temp=number
while temp>0:
    digit=temp%10
    resultnumber+=digit**digits
    temp//=10

#display the result
if resultnumber==number:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")