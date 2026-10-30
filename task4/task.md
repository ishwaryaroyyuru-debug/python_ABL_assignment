## Retail Billing with Multiple Discount Rules
Here is a professional project format for Retail Billing with Multiple Discount Rules, suitable for a first-year B.Tech CSE-AIML student.
# 1. Problem Statement
The Retail Billing with Multiple Discount Rules system is designed to calculate the final bill for customers purchasing products from a retail store. The system accepts the product price, quantity, and applicable discount rules, such as discounts based on the total purchase amount and additional discounts for eligible customers.

The program calculates the subtotal, determines the applicable discounts, deducts them from the subtotal, and generates the final bill. It also displays the discount amount and final payable amount. This system helps automate billing, minimize calculation errors, and provide customers with accurate bills.

For this academic project, the discount percentages and eligibility conditions are predefined examples and can be modified as needed.
# 2. Algorithm
1. Start the program.
2. Enter the customer's name.
3. Enter the product name, unit price, and quantity.
4. Calculate the subtotal by multiplying the unit price by the quantity.
5. Check whether the subtotal is at least ₹5,000.
6. If yes, apply a 10% discount; otherwise, apply no purchase-based discount.
7. Ask whether the customer is eligible for an additional 5% membership discount.
8. Calculate the membership discount on the amount remaining after the purchase-based discount.
9. Add the applicable discounts to obtain the total discount.
10. Subtract the total discount from the subtotal to calculate the final payable amount.
11. Display the customer details, product details, subtotal, discounts, and final bill.
12. Stop the program.


# flowchart TD
    A([Start]) --> B[/Enter Customer and Product Details/]
    B --> C[/Enter Unit Price and Quantity/]
    C --> D[Calculate Subtotal = Price x Quantity]
    D --> E{Subtotal >= 5000?}
    E -->|Yes| F[Purchase Discount = 10% of Subtotal]
    E -->|No| G[Purchase Discount = 0]
    F --> H[Calculate Amount After Purchase Discount]
    G --> H
    H --> I{Membership Customer?}
    I -->|Yes| J[Membership Discount = 5% of Remaining Amount]
    I -->|No| K[Membership Discount = 0]
    J --> L[Calculate Total Discount]
    K --> L
    L --> M[Calculate Final Payable Amount]
    M --> N[/Display Itemized Bill/]
    N --> O([Stop])

# 4. Input
The program requires the following inputs from the user.
Input	Description	Example
Customer name	Name of the customer	Rahul
Product name	Name of the purchased product	Headphones
Unit price	Price of one product	₹2,000
Quantity	Number of products purchased	3
Membership status	Whether the customer is a member	Yes

# Expected output
======= RETAIL BILL =======

Customer Name: Rahul
Product Name: Headphones
Unit Price: Rs. 2000
Quantity: 3

Subtotal: Rs. 6000
Purchase Discount (10%): Rs. 600
Membership Discount (5%): Rs. 270
Total Discount: Rs. 870

Final Payable Amount: Rs. 5130

===========================
5. Sample calculation
Step 1: Calculate subtotal

2000 * 3 = ₹6000

Step 2: Calculate purchase discount

6000 * 10/100 = ₹600

Step 3: Calculate membership discount

6000-600*5/100=₹270

Step 4: Calculate final bill

Final Bill=6000-600-270

textFinal Bill=₹5130
