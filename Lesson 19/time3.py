def test(n):
    iteration = 0
    for i in range(0, n):
        for j in range(0, n):
            print("*", end="")
            iteration += 1
        print("")  # new line after each row
    print("\nWhen n is", n, "Iterations =", iteration)

test(5)
test(10)
test(300)

print("\nWith every 'n', the time taken = n^2")
print("(n^2)")
