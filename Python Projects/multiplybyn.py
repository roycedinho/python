# Function 1: Using 1 iteration (direct multiplication)
def multiply_one_iteration(N, M):
    return N * M

# Function 2: Using N iterations (repeated addition)
def multiply_n_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

# Main program
N = int(input("Enter the value of N: "))
M = int(input("Enter the value of M: "))

print("Result using one iteration:", multiply_one_iteration(N, M))
print("Result using N iterations:", multiply_n_iterations(N, M))
