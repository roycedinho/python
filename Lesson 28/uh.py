def swap1(a, b):
   
    a = a ^ b
    print("Swap1 (XOR) -> a:", a, "b:", b)

def swap2(a, b):

    a = (a & b) + (a | b) 
    b = a + (~b) + 1 # Equivalent to a - b
    a = a + (~b) + 1 # Equivalent to a - b
    print("Swap2 (Arithmetic) -> a:", a, "b:", b)

swap1(1, 2)
swap2(1, 2)