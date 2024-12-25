# Get the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Calculate the squares and separate into odd and even
squares = [x**2 for x in range(start, end + 1)]
odd_squares = [sq for sq in squares if sq % 2 != 0]
even_squares = [sq for sq in squares if sq % 2 == 0]

# Print the results
print("\nAll squares in the range:")
print(squares)
print("\nOdd squares:")
print(odd_squares)
print("\nEven squares:")
print(even_squares)
