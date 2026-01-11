# to find factors of user input

#goes from 1 to number and hecks if i divide the number. if es, it is a factor

def print_factors(number):
    print(f"Factors of {number} are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
            
#taking input from the user
number=int(input("Enter a number to find its factors: "))

#calling our function
print_factors(number)