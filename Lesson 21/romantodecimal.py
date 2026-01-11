# program to convert roman numerals to integers
def roman_to_integer(roman_input):

    # all roman units with integer values
    roman_values = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

    # result
    resultinteger = 0

    # go from 0 to len-1
    for i in range(0, len(roman_input) - 1):
        if roman_values[roman_input[i]] < roman_values[roman_input[i + 1]]:
            resultinteger -= roman_values[roman_input[i]]
        else:
            resultinteger += roman_values[roman_input[i]]

    return resultinteger + roman_values[roman_input[-1]]


# Take roman as input from user
roman = input("Input roman numeral : ")

# Print the integer
print("Integer equivalent : ", roman_to_integer(roman))
