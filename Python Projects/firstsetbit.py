n = int(input())

position = 1
while n > 0:
    if n & 1:
        print(position)
        break
    n >>= 1
    position += 1