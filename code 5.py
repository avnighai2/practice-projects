# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the test dictionary
print("Test Dictionary:")
for key, value in test_dict.items():
    print(f"{key}: {value}")

# Ask the user for a value to check frequency
user_value = int(input("\nEnter the value to check its frequency in the dictionary: "))

# Count and print the frequency
frequency = list(test_dict.values()).count(user_value)
print(f"\nThe frequency of the value {user_value} is: {frequency}")
