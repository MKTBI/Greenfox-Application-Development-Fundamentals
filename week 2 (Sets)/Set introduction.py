# Create a set
numbers = {1, 2, 3, 4, 5}

# Add at least 5 members to the set
numbers.update({6, 7, 8, 9, 10})

# Remove at most 2 members from the set
numbers.discard(1)
numbers.discard(2)

# Iterate over the set and print its members
for num in numbers:
    print(num)

# Remove 482 from the set if it is present
if 482 in numbers:
    numbers.remove(482)

# Remove 42 from the set even if it is not present
numbers.discard(42)
