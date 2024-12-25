# Input two sets from the user
set1 = set(map(int, input("Enter elements of the first set, separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of the second set, separated by spaces: ").split()))

# Calculate the symmetric difference
symmetric_difference = set1.symmetric_difference(set2)

# Print the result
print(f"\nThe symmetric difference between the two sets is: {symmetric_difference}")
