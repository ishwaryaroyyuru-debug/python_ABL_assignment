# Retail Billing with Multiple Discount Rules

print("===== RETAIL BILLING SYSTEM =====")

# Input customer details
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")

# Input product details
unit_price = float(input("Enter unit price: Rs. "))
quantity = int(input("Enter quantity: "))
membership = input("Is the customer a member? (yes/no): ").strip().lower()

# Validate input
if unit_price < 0 or quantity <= 0:
    print("Invalid input! Price cannot be negative and quantity must be positive.")

elif membership not in ("yes", "no"):
    print("Invalid membership status! Enter yes or no.")

else:
    # Calculate subtotal
    subtotal = unit_price * quantity

    # Initialize discounts
    purchase_discount = 0
    membership_discount = 0

    # Apply purchase discount
    if subtotal >= 5000:
        purchase_discount = subtotal * 0.10

    # Calculate amount after purchase discount
    amount_after_discount = subtotal - purchase_discount

    # Apply membership discount
    if membership == "yes":
        membership_discount = amount_after_discount * 0.05

    # Calculate final bill
    total_discount = purchase_discount + membership_discount
    final_amount = subtotal - total_discount

    # Display bill
    print("\n========== RETAIL BILL ==========")
    print("Customer Name:", customer_name)
    print("Product Name:", product_name)
    print(f"Unit Price: Rs. {unit_price:.2f}")
    print("Quantity:", quantity)
    print(f"Subtotal: Rs. {subtotal:.2f}")
    print(f"Purchase Discount (10%): Rs. {purchase_discount:.2f}")
    print(f"Membership Discount (5%): Rs. {membership_discount:.2f}")
    print(f"Total Discount: Rs. {total_discount:.2f}")
    print(f"Final Payable Amount: Rs. {final_amount:.2f}")
    print("=================================")

# Sample output
===== RETAIL BILLING SYSTEM =====
Enter customer name: Rahul
Enter product name: Headphones
Enter unit price: Rs. 2000
Enter quantity: 3
Is the customer a member? (yes/no): yes

========== RETAIL BILL ==========
Customer Name: Rahul
Product Name: Headphones
Unit Price: Rs. 2000.00
Quantity: 3
Subtotal: Rs. 6000.00
Purchase Discount (10%): Rs. 600.00
Membership Discount (5%): Rs. 270.00
Total Discount: Rs. 870.00
Final Payable Amount: Rs. 5130.00
=================================               py
