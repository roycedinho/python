def recurrence(n):
    if n == 1:
        return 1
    else:
        return recurrence(n - 1) + n

n = int(input("Enter value of n: "))
result = recurrence(n)

print("Result:", result)
