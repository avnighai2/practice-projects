# Function to check if age is valid
def is_valid_age(age):
    return 0 <= age <= 120  # Assuming age should be between 0 and 120

# Get the age input from the user
try:
    age = int(input("Enter your age: "))
    
    # Validate the age
    if not is_valid_age(age):
        print("Error: The entered age is not valid. Age should be between 0 and 120.")
    else:
        # Check if the age is even or odd
        if age % 2 == 0:
            print(f"The entered age {age} is even.")
        else:
            print(f"The entered age {age} is odd.")
except ValueError:
    print("Error: Please enter a valid integer for age.")
