def test(lst):
    result= {}
    for item in lst:
        result[item[0]] = item [1:]
    return result

students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("\n Original list of lists:")
print(students)
print("\n Converted lists to a dictionary:")
print(test(students))