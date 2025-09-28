# File Handling Activity for Students

def write_file():
    with open("student_file.txt", "w") as f:
        f.write("This is the first line.\n")
        f.write("This is the second line.\n")
    print("File created and written successfully (mode: w).")

def read_file():
    try:
        with open("student_file.txt", "r") as f:
            content = f.read()
        print("\n--- File Content (mode: r) ---")
        print(content)
    except FileNotFoundError:
        print("File not found. Please create it first.")

def append_file():
    with open("student_file.txt", "a") as f:
        f.write("This line is appended at the end.\n")
    print("Text appended successfully (mode: a).")

def read_write_file():
    with open("student_file.txt", "r+") as f:
        print("\n--- Before writing (mode: r+) ---")
        print(f.read())
        f.seek(0)  # move cursor to start
        f.write("Updated first line!\n")
    print("First line updated using r+ mode.")

def write_read_file():
    with open("student_file.txt", "w+") as f:
        f.write("File is overwritten with new content.\n")
        f.seek(0)  # go back to start
        print("\n--- After writing (mode: w+) ---")
        print(f.read())

def append_read_file():
    with open("student_file.txt", "a+") as f:
        f.write("Extra line added with a+ mode.\n")
        f.seek(0)
        print("\n--- File Content after a+ ---")
        print(f.read())

# Main program menu
def main():
    while True:
        print("\n--- File Handling Activity ---")
        print("1. Write File (w)")
        print("2. Read File (r)")
        print("3. Append File (a)")
        print("4. Read & Write File (r+)")
        print("5. Write & Read File (w+)")
        print("6. Append & Read File (a+)")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            write_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            append_file()
        elif choice == "4":
            read_write_file()
        elif choice == "5":
            write_read_file()
        elif choice == "6":
            append_read_file()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
