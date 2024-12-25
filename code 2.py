import calendar

def display_months():
    print("Here are the names of all the months:")
    for month_num in range(1, 13):  # Loop through numbers 1 to 12
        month_name = calendar.month_name[month_num]
        print(f"{month_num}: {month_name}")

# Run the function
display_months()
