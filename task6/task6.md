## ATM Transaction Sequence Simulation
Here is a professional project format for ATM Transaction Sequence Simulation, suitable for a first-year B.Tech CSE-AIML student.
# 1. Problem Statement
The ATM Transaction Sequence Simulation System is designed to simulate basic banking transactions performed through an Automated Teller Machine (ATM). The system allows a user to enter a PIN, verify the credentials, check the available account balance, withdraw money, deposit money, and exit the system.

The program validates the entered PIN, ensures that withdrawal amounts do not exceed the available balance, and updates the account balance after each successful transaction. It displays transaction messages and the updated balance after each operation. This system helps demonstrate conditional statements, loops, input validation, and sequential transaction processing in Python.

Note: This is an educational simulation and does not connect to a real bank account.
# 2. Algorithm
1. Start the program.
2. Initialize a sample account balance and a predefined ATM PIN.
3. Ask the user to enter the ATM PIN.
4. Verify the entered PIN.
5. If the PIN is incorrect, display an error message and stop the program.
6. If the PIN is correct, display the ATM transaction menu.
7. Allow the user to select one of the following options:
   - Check balance
   - Withdraw money
   - Deposit money
   - Exit
8. If the user selects Check Balance, display the current account balance.
9. If the user selects Withdraw Money, enter the withdrawal amount and check whether it is positive and does not exceed the available balance.
10. If the withdrawal is valid, deduct the amount from the balance and display the updated balance.
11. If the user selects Deposit Money, enter the deposit amount, validate it, add it to the balance, and display the updated balance.
12. If the user selects Exit, display a thank-you message and terminate the program.
13. If the user enters an invalid menu option, display an error message and show the menu again.
14. Repeat the transaction process until the user chooses to exit.
15. Stop the program.


# flowchart TD
    A([Start]) --> B[Initialize PIN and Account Balance]
    B --> C[/Enter ATM PIN/]
    C --> D{PIN Correct?}
    D -->|No| E[/Display Invalid PIN/]
    E --> Z([Stop])
    D -->|Yes| F[/Display ATM Menu/]
    F --> G[/Enter Transaction Choice/]
    G --> H{Choice?}

    H -->|1. Check Balance| I[/Display Current Balance/]
    I --> F

    H -->|2. Withdraw| J[/Enter Withdrawal Amount/]
    J --> K{Amount Positive and Within Balance?}
    K -->|Yes| L[Deduct Amount from Balance]
    L --> M[/Display Updated Balance/]
    M --> F
    K -->|No| N[/Display Invalid Amount or Insufficient Balance/]
    N --> F

    H -->|3. Deposit| O[/Enter Deposit Amount/]
    O --> P{Amount Positive?}
    P -->|Yes| Q[Add Amount to Balance]
    Q --> R[/Display Updated Balance/]
    R --> F
    P -->|No| S[/Display Invalid Deposit Amount/]
    S --> F

    H -->|4. Exit| T[/Display Thank You Message/]
    T --> Z

    H -->|Invalid Choice| U[/Display Invalid Choice/]
    U --> F

# 4. Input
The program requires the following inputs from the user.
Input	Description	Example
ATM PIN	PIN used to access the simulated account	1234
Initial balance	Starting account balance	₹10,000
Transaction choice	Selected menu operation	2
Withdrawal amount	Amount to withdraw	₹2,000
Deposit amount	Amount to deposit	₹1,500

# Expected output
===== ATM TRANSACTION SYSTEM =====

PIN verified successfully!

Withdrawal successful.
Amount withdrawn: Rs. 2000.00
Available balance: Rs. 8000.00

Deposit successful.
Amount deposited: Rs. 1500.00
Available balance: Rs. 9500.00

Current account balance: Rs. 9500.00

Thank you for using the ATM.
=================================

# 5. Sample calculation
   
Initial balance = ₹10,000

After withdrawal:

₹10,000-₹2,000=₹8,000

After deposit:

₹8,000+₹1,500=₹9,500

Final balance: ₹9,500
