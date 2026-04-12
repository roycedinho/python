n = int(input())

binary = bin(n)[2:]
max_ones = max(binary.split('0'), key=len)

print(len(max_ones))