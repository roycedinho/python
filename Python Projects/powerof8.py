n = int(input())

def is_power_of_8(n):
    if n <= 0:
        return False
    while n % 8 == 0:
        n //= 8
    return n == 1

print(is_power_of_8(n))