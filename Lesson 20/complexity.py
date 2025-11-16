def arraysum(a):
    total = 0
    for i in a:
        total += i
    return total

def summ(n):
    if n <= 0:
        return 0
    return n + summ(n-1)

