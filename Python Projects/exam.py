# Exam eligibility criteria:
# - Minimum age: 16
# - Minimum attendance: 75%

# Get user input
age = int(input("Enter your age: "))
attendance = float(input("Enter your attendance percentage: "))

# Check eligibility
if age >= 16:
    if attendance >= 75:
        print("You are eligible to take the exam.")
    else:
        print("You are not eligible due to low attendance.")
else:
    print("You are not eligible due to age restrictions.")
