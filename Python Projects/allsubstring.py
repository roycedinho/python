def get_all_substrings(string):
    n = len(string)
    substrings = []

    # The outer loop determines the starting position
    for i in range(n):
        # The inner loop determines the ending position
        # We use i + 1 because the second index in slicing is exclusive
        for j in range(i + 1, n + 1):
            substrings.append(string[i:j])
            
    return substrings
