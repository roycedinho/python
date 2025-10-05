# Open file in read mode
file = open("example.txt", "r")

# 1. Read the whole content at once
print("Reading all content at once:")
print(file.read())

# Reset file pointer to beginning
file.seek(0)

# 2. Read line by line using readline()
print("\nReading line by line:")
print(file.readline())  # Reads first line
print(file.readline())  # Reads second line

# Reset file pointer to beginning
file.seek(0)

# 3. Read all lines into a list using readlines()
print("\nReading all lines into a list:")
lines = file.readlines()
print(lines)

file.close()

# 4. Using with-statement (best practice)
print("\nUsing 'with' for automatic file handling:")
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
