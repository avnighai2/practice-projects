# Task 1: Generate Lists of Odd and Even Numbers
# Take input from the user
number = int(input("Enter a number: "))

# Create a list of odd numbers and even numbers under the input value
odd_numbers = [x for x in range(1, number) if x % 2 != 0]
even_numbers = [x for x in range(1, number) if x % 2 == 0]

# Print the results
print(f"\nOdd numbers under {number}: {odd_numbers}")
print(f"Even numbers under {number}: {even_numbers}")

# Task 2: Capitalize the First Letter of Fruits
# List of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Create a new list with the first letter capitalized
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

# Print the results
print(f"\nOriginal list of fruits: {fruits}")
print(f"Updated list of fruits: {capitalized_fruits}")
