from math import prod

# Get the tuple from the user
user_input = input("Enter the numbers in the tuple, separated by commas: ")
numbers_tuple = tuple(map(int, user_input.split(',')))

# Calculate the product of all numbers
product = prod(numbers_tuple)

# Print the result
print("\nThe product of all numbers in the tuple is:", product)
