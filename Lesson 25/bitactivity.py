def count_bits(n):
    ones = 0
    zeros = 0
    
    temp = n
    while temp > 0:
        if temp & 1 == 1:
            ones += 1
        else:
            zeros += 1
        temp >>= 1
        
    return ones, zeros


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def analyse_number(n):
    print("\n======= RESULT =======")
    print("Number:", n)
    print("Binary:", bin(n))
    print("Bit Length:", n.bit_length())
    
    ones, zeros = count_bits(n)
    print("Number of 1's:", ones)
    print("Number of 0's:", zeros)
    
    if n % 2 == 0:
        print("Even or Odd: Even")
    else:
        print("Even or Odd: Odd")
    
    if is_prime(n):
        print("Prime Check: Prime")
    else:
        print("Prime Check: Not Prime")
    
    print("-----------------------------------------\n")


# Main loop
while True:
    user_input = input("Enter a positive number (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        print("Exiting the program. Goodbye!")
        break
    
    if not user_input.isdigit():
        print("Invalid input. Please enter a positive number.")
        continue
    
    number = int(user_input)
    analyse_number(number)