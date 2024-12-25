# Get the total bill amount from the user
total_bill = float(input("Enter the total bill amount: "))

# Get the amount paid by the customer
amount_paid = float(input("Enter the amount paid by the customer: "))

# Calculate the due amount or change
if amount_paid < total_bill:
    due_amount = total_bill - amount_paid
    print(f"The customer still owes ${due_amount:.2f}.")
elif amount_paid > total_bill:
    change = amount_paid - total_bill
    print(f"The customer should receive ${change:.2f} in change.")
else:
    print("The bill is fully paid. No due amount or change.")
