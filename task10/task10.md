## Integrated E-Commerce Order Processing and Reconciliation
# 1. Problem Statement
The Integrated E-Commerce Order Processing and Reconciliation System is designed to simulate the major operations involved in an online shopping platform. The system manages customer details, product selection, order processing, billing, payment verification, and order reconciliation.

The main objective of this project is to develop a Python-based application that processes customer orders, calculates the total bill, applies discounts, verifies payment details, and checks whether the payment amount matches the order amount.

The system allows customers to select products, enter quantities, calculate the final payable amount, and complete simulated payments. It also identifies payment mismatches, insufficient payments, and successful transactions.

This project demonstrates the practical application of Python programming concepts such as variables, dictionaries, conditional statements, loops, functions, arithmetic operations, and exception handling in real-world e-commerce operations.
# 2. Algorithm
1. Start the program.
2. Display the welcome message: Integrated E-Commerce Order Processing and Reconciliation.
3. Accept customer details such as customer ID and customer name.
4. Display the available products along with their prices.
5. Ask the customer to select a product.
6. Accept the required quantity.
7. Check whether the selected product exists and whether the quantity is valid.
8. Calculate the subtotal using:
\[
\text{Subtotal} = \text{Product Price} \times \text{Quantity}
\]

9. Apply a discount based on the order amount.
   - If subtotal is ₹5,000 or above, apply a 10% discount.
   - Otherwise, no discount is applied.
10. Calculate the final payable amount:
\[
\text{Final Amount} = \text{Subtotal} - \text{Discount}
\]

11. Display the order summary, including product name, quantity, subtotal, discount, and final amount.
12. Accept the payment amount from the customer.
13. Compare the payment amount with the final payable amount.
14. Display the payment result:
- If payment equals the final amount, mark the payment as successful.
- If payment is less than the final amount, display insufficient payment.
- If payment is greater than the final amount, calculate and display the change.
15. Perform order reconciliation by comparing the order amount and payment amount.
16. Display the reconciliation status.
17. Ask whether the customer wants to process another order.
18. Repeat the process if required.
19. Display the thank-you message.
20. Stop the program.


# flowchart TD
    A([Start]) --> B[Display Welcome Message]
    B --> C[Enter Customer Details]
    C --> D[Display Available Products]
    D --> E[Select Product and Quantity]
    E --> F{Valid Product and Quantity?}

    F -->|No| G[Display Error Message]
    G --> D

    F -->|Yes| H[Calculate Subtotal]
    H --> I{Subtotal >= 5000?}

    I -->|Yes| J[Apply 10% Discount]
    I -->|No| K[No Discount]

    J --> L[Calculate Final Amount]
    K --> L

    L --> M[Display Order Summary]
    M --> N[Enter Payment Amount]
    N --> O{Compare Payment}

    O -->|Equal| P[Payment Successful]
    O -->|Less| Q[Insufficient Payment]
    O -->|Greater| R[Calculate Change]

    P --> S[Perform Order Reconciliation]
    Q --> T[Display Payment Status]
    R --> S
    T --> U{Try Again?}
    S --> V[Display Reconciliation Status]
    V --> U

    U -->|Yes| D
    U -->|No| W[Display Thank You Message]
    W --> X([Stop])

# 4. Input
The program accepts the following inputs from the customer:
Module	Required Input
Customer Details	Customer ID, Customer Name
Product Selection	Product ID or Product Name
Quantity	Number of units required
Payment	Amount paid by the customer
Order Processing	Continue or Exit choice

Available Products (Sample Data)
Product ID	Product Name	Price
101	Laptop	₹45,000
102	Smartphone	₹20,000
103	Headphones	₹2,000
104	Keyboard	₹1,500
105	Mouse	₹800

# Sample Input
# 1. Customer Details
Enter Customer ID: C101
Enter Customer Name: Rahul



# 2. Product Selection
Available Products:
101 - Laptop - Rs. 45000
102 - Smartphone - Rs. 20000
103 - Headphones - Rs. 2000
104 - Keyboard - Rs. 1500
105 - Mouse - Rs. 800

Enter Product ID: 102
Enter Quantity: 1
# 3. Payment Details
Enter Payment Amount: 18000



# 4. Order Confirmation
Do you want to process another order? (yes/no): no



# 5. Expected Output (Sample)
===== E-COMMERCE ORDER PROCESSING SYSTEM =====

Customer ID: C101
Customer Name: Rahul

Product Name: Smartphone
Quantity: 1
Price per Unit: Rs. 20000

Subtotal: Rs. 20000
Discount (10%): Rs. 2000
Final Amount: Rs. 18000

Enter Payment Amount: 18000

Payment Status: SUCCESSFUL

Order Reconciliation:
Order Amount: Rs. 18000
Payment Amount: Rs. 18000

Reconciliation Status: MATCHED

Order Status: CONFIRMED

Thank you for shopping with us!
