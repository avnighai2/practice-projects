def shutdown(command):
    """
    Shutdown function that accepts a command and responds accordingly.
    """
    if command.lower() == "yes":
        return "Shutting down..."
    elif command.lower() == "no":
        return "Shutdown canceled."
    else:
        return "Invalid command. Please enter 'yes' or 'no'."

# Get user input
user_input = input("Do you want to shut down? (yes/no): ")

# Call the shutdown function and print the result
result = shutdown(user_input)
print(result)
