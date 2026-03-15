def is_power_of_4(n):
    # number must be positive
    if n <= 0:
        return False

    # check that only one bit is set (power of 2 check)
    if (n & (n - 1)) != 0:
        return False

    # count how many right shifts until the number becomes 1
    count = 0
    while n > 1:
        n = n >> 1
        count += 1

    # if count is even then it is a power of 4
    if count % 2 == 0:
        return True
    else:
        return False


# take input from user
num = int(input("Enter a number: "))

if is_power_of_4(num):
    print("It is a power of 4")
else:
    print("It is not a power of 4")