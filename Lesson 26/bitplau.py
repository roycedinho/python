# program to check if user input numbers are equal without usning any comparison operator

def checkifsame(number1, number2):
    # using xor operator as a^a is always 0
    if number1 ^ number2 == 0:
        print("numbers are not equal")
    else:
        print("both numbers are equal")


# taking user input
number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))

checkifsame(number1, number2)