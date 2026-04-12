def implement_circuit(a, b):
    # example circuit: (a AND b) OR (a XOR b)
    return (a & b) | (a ^ b)

a = int(input())
b = int(input())

print(implement_circuit(a, b))