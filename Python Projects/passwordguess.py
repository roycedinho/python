import random
import string

def generate_password(length):
    # Define possible characters
    letters = string.ascii_letters  # a-z and A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # special characters

    # Combine all characters
    all_characters = letters + digits + symbols

    # Generate password
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

# Main program
print("Welcome to the Random Password Generator!")

# Ask user for length
password_length = int(input("Enter desired password length: "))

# Generate and display
password = generate_password(password_length)
print("\nYour random password is:", password)
