# Campus Event Financial Planning System

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input event details
event_name = input("Enter event name: ")
participants = int(input("Enter number of participants: "))

# Input income details
registration_fee = float(
    input("Enter registration fee per participant: Rs. ")
)
sponsorship = float(input("Enter sponsorship amount: Rs. "))

# Input expense details
venue_expenses = float(input("Enter venue expenses: Rs. "))
food_expenses = float(input("Enter food expenses: Rs. "))
decoration_expenses = float(input("Enter decoration expenses: Rs. "))
transport_expenses = float(input("Enter transportation expenses: Rs. "))
other_expenses = float(input("Enter miscellaneous expenses: Rs. "))

# Validate inputs
if (
    participants < 0
    or registration_fee < 0
    or sponsorship < 0
    or venue_expenses < 0
    or food_expenses < 0
    or decoration_expenses < 0
    or transport_expenses < 0
    or other_expenses < 0
):
    print("Invalid input! Values cannot be negative.")

else:
    # Calculate income
    registration_income = participants * registration_fee
    total_income = registration_income + sponsorship

    # Calculate total expenditure
    total_expenses = (
        venue_expenses
        + food_expenses
        + decoration_expenses
        + transport_expenses
        + other_expenses
    )

    # Calculate financial balance
    balance = total_income - total_expenses

    # Determine financial result
    if balance > 0:
        result = "PROFIT"
    elif balance < 0:
        result = "LOSS"
    else:
        result = "BREAK-EVEN"

    # Display financial report
    print("\n===== CAMPUS EVENT FINANCIAL REPORT =====")
    print("Event Name:", event_name)
    print("Number of Participants:", participants)

    print("\n----- INCOME DETAILS -----")
    print(f"Registration Income: Rs. {registration_income:.2f}")
    print(f"Sponsorship Income: Rs. {sponsorship:.2f}")
    print(f"Total Income: Rs. {total_income:.2f}")

    print("\n----- EXPENSE DETAILS -----")
    print(f"Venue Expenses: Rs. {venue_expenses:.2f}")
    print(f"Food Expenses: Rs. {food_expenses:.2f}")
    print(f"Decoration Expenses: Rs. {decoration_expenses:.2f}")
    print(f"Transportation Expenses: Rs. {transport_expenses:.2f}")
    print(f"Miscellaneous Expenses: Rs. {other_expenses:.2f}")
    print(f"Total Expenditure: Rs. {total_expenses:.2f}")

    print("\n----- FINAL RESULT -----")
    print(f"Financial Balance: Rs. {balance:.2f}")
    print("Result:", result)
    print("=========================================")

# sample Outpt:
===== CAMPUS EVENT FINANCIAL PLANNING =====
Enter event name: Tech Fest
Enter number of participants: 200
Enter registration fee per participant: Rs. 200
Enter sponsorship amount: Rs. 15000
Enter venue expenses: Rs. 10000
Enter food expenses: Rs. 20000
Enter decoration expenses: Rs. 5000
Enter transportation expenses: Rs. 3000
Enter miscellaneous expenses: Rs. 2000

===== CAMPUS EVENT FINANCIAL REPORT =====
Event Name: Tech Fest
Number of Participants: 200

----- INCOME DETAILS -----
Registration Income: Rs. 40000.00
Sponsorship Income: Rs. 15000.00
Total Income: Rs. 55000.00

----- EXPENSE DETAILS -----
Venue Expenses: Rs. 10000.00
Food Expenses: Rs. 20000.00
Decoration Expenses: Rs. 5000.00
Transportation Expenses: Rs. 3000.00
Miscellaneous Expenses: Rs. 2000.00
Total Expenditure: Rs. 40000.00

----- FINAL RESULT -----
Financial Balance: Rs. 15000.00
Result: PROFIT
=========================================               (2py)
