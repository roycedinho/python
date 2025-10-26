# Set creation
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Set A:", set_a)
print("Set B:", set_b)

# add an element to set a
set_a.add(10)
print("After adding 10 to Set A:", set_a)

# update set b with multiple elements
set_b.update([7, 8])
print("After updating Set B with 7 and 8:", set_b)

# remove an element from set a
set_a.remove(2)
print("After removing 2 from Set A:", set_a)

# discard an element
set_b.discard(100)  # no error if element not found
print("After discarding 100 from Set B:", set_b)

# pop an element (randomly removes one)
popped = set_a.pop()
print(f"\nPopped element from Set A: {popped}")
print("Set A after pop:", set_a)

# copy of set_a
copy_a = set_a.copy()
print("\nCopy of Set A:", copy_a)

print("\n--- SET OPERATIONS ---")
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A-B):", set_a - set_b)
print("Difference (B-A):", set_b - set_a)
print("Symmetric Difference:", set_a ^ set_b)

print("\n--- SET RELATIONS ---")
print("Is A subset of B?", set_a.issubset(set_b))
print("Is A superset of B?", set_a.issuperset(set_b))
print("Are A and B disjoint?", set_a.isdisjoint(set_b))
