# program to check if numbers are odd or even and count odd numbers

odd_count = 0

for i in range(3):
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
        odd_count += 1

print("Total odd numbers entered:", odd_count)
