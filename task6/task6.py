# ATM Transaction Sequence Simulation

print("===== ATM TRANSACTION SYSTEM =====")

# Initialize account details
correct_pin = "1234"
balance = 10000.00

# PIN verification
pin = input("Enter ATM PIN: ")

if pin != correct_pin:
    print("Incorrect PIN! Access denied.")

else:
    print("\nPIN verified successfully!")

    # Transaction menu
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Check balance
        if choice == "1":
            print(f"Current account balance: Rs. {balance:.2f}")

        # Withdraw money
        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: Rs. "))

                if amount <= 0:
                    print("Invalid amount! Enter a positive amount.")

                elif amount > balance:
                    print("Insufficient balance!")

                else:
                    balance -= amount
                    print("Withdrawal successful.")
                    print(f"Amount withdrawn: Rs. {amount:.2f}")
                    print(f"Available balance: Rs. {balance:.2f}")

            except ValueError:
                print("Invalid input! Enter a numeric amount.")

        # Deposit money
        elif choice == "3":
            try:
                amount = float(input("Enter deposit amount: Rs. "))

                if amount <= 0:
                    print("Invalid amount! Enter a positive amount.")

                else:
                    balance += amount
                    print("Deposit successful.")
                    print(f"Amount deposited: Rs. {amount:.2f}")
                    print(f"Available balance: Rs. {balance:.2f}")

            except ValueError:
                print("Invalid input! Enter a numeric amount.")

        # Exit ATM
        elif choice == "4":
            print("\nThank you for using the ATM.")
            break

        # Invalid menu choice
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

print("=================================")

# sample Output:
===== ATM TRANSACTION SYSTEM =====
Enter ATM PIN: 1234

PIN verified successfully!

----- ATM MENU -----
1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit
Enter your choice: 2
Enter withdrawal amount: Rs. 2000
Withdrawal successful.
Amount withdrawn: Rs. 2000.00
Available balance: Rs. 8000.00

----- ATM MENU -----
1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit
Enter your choice: 3
Enter deposit amount: Rs. 1500
Deposit successful.
Amount deposited: Rs. 1500.00
Available balance: Rs. 9500.00

----- ATM MENU -----
1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit
Enter your choice: 1
Current account balance: Rs. 9500.00

----- ATM MENU -----
1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit
Enter your choice: 4

Thank you for using the ATM.
=================================
