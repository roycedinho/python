# Simple Student Grade System

def calculate_average(scores):
    return sum(scores) / len(scores)

students = {}
num_students = int(input("How many students? "))

for i in range(num_students):
    name = input("Enter student name: ")
    scores = []
    for j in range(3):
        score = int(input(f"Enter score {j+1} for {name}: "))
        scores.append(score)
    students[name] = scores

# Calculate averages and find highest/lowest
highest_avg = -1
lowest_avg = 101
for name, scores in students.items():
    avg = calculate_average(scores)
    print(f"{name} average: {avg}")
    if avg > highest_avg:
        highest_avg = avg
        highest_student = name
    if avg < lowest_avg:
        lowest_avg = avg
        lowest_student = name

print(f"\nHighest average: {highest_avg} by {highest_student}")
print(f"Lowest average: {lowest_avg} by {lowest_student}")
