n = int(input())

binary = bin(n)[2:]
reversed_binary = binary[::-1]

print(int(reversed_binary, 2))