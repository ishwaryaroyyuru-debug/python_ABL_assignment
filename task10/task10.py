# Integrated E-Commerce Order Processing and Reconciliation

# Available Products
products = {
    101: {"name": "Laptop", "price": 45000},
    102: {"name": "Smartphone", "price": 20000},
    103: {"name": "Headphones", "price": 2000},
    104: {"name": "Keyboard", "price": 1500},
    105: {"name": "Mouse", "price": 800}
}

print("===== E-COMMERCE ORDER PROCESSING SYSTEM =====")

# Customer Details
customer_id = input("Enter Customer ID: ")
customer_name = input("Enter Customer Name: ")

while True:

    print("\n========== AVAILABLE PRODUCTS ==========")

    for product_id, details in products.items():
        print(product_id, "-", details["name"],
              "- Rs.", details["price"])

    # Product Selection
    try:
        product_id = int(input("\nEnter Product ID: "))

        if product_id not in products:
            print("Invalid Product ID. Please try again.")
            continue

        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        # Calculate Subtotal
        product_name = products[product_id]["name"]
        price = products[product_id]["price"]

        subtotal = price * quantity

        # Calculate Discount
        if subtotal >= 5000:
            discount = subtotal * 0.10
        else:
            discount = 0

        final_amount = subtotal - discount

        # Display Order Summary
        print("\n========== ORDER SUMMARY ==========")
        print("Customer ID:", customer_id)
        print("Customer Name:", customer_name)
        print("Product Name:", product_name)
        print("Quantity:", quantity)
        print("Price per Unit: Rs.", price)
        print("Subtotal: Rs.", subtotal)
        print("Discount: Rs.", discount)
        print("Final Amount: Rs.", final_amount)

        # Payment Processing
        payment = float(input("\nEnter Payment Amount: Rs."))

        if payment < 0:
            print("Payment amount cannot be negative.")
            continue

        print("\n========== PAYMENT DETAILS ==========")

        if payment == final_amount:
            print("Payment Status: SUCCESSFUL")
            reconciliation = "MATCHED"
            order_status = "CONFIRMED"

        elif payment < final_amount:
            print("Payment Status: INSUFFICIENT")
            print("Remaining Amount: Rs.", final_amount - payment)
            reconciliation = "MISMATCHED"
            order_status = "PENDING"

        else:
            change = payment - final_amount
            print("Payment Status: SUCCESSFUL")
            print("Change to Return: Rs.", change)
            reconciliation = "MATCHED"
            order_status = "CONFIRMED"

        # Order Reconciliation
        print("\n========== ORDER RECONCILIATION ==========")
        print("Order Amount: Rs.", final_amount)
        print("Payment Amount: Rs.", payment)
        print("Reconciliation Status:", reconciliation)
        print("Order Status:", order_status)

        # Continue or Exit
        choice = input(
            "\nDo you want to process another order? (yes/no): "
        ).lower()

        if choice != "yes":
            break

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")

print("\nThank you for shopping with us!")
print("===== PROGRAM ENDED =====")

# 1. Successful Order Processing

===== E-COMMERCE ORDER PROCESSING SYSTEM =====

Enter Customer ID: C101
Enter Customer Name: Rahul

========== AVAILABLE PRODUCTS ==========

101 - Laptop - Rs. 45000
102 - Smartphone - Rs. 20000
103 - Headphones - Rs. 2000
104 - Keyboard - Rs. 1500
105 - Mouse - Rs. 800

Enter Product ID: 102
Enter Quantity: 1

========== ORDER SUMMARY ==========

Customer ID: C101
Customer Name: Rahul
Product Name: Smartphone
Quantity: 1
Price per Unit: Rs. 20000
Subtotal: Rs. 20000
Discount: Rs. 2000.0
Final Amount: Rs. 18000.0

Enter Payment Amount: Rs.18000

========== PAYMENT DETAILS ==========

Payment Status: SUCCESSFUL

========== ORDER RECONCILIATION ==========

Order Amount: Rs. 18000.0
Payment Amount: Rs. 18000.0
Reconciliation Status: MATCHED
Order Status: CONFIRMED

Do you want to process another order? (yes/no): no

Thank you for shopping with us!
===== PROGRAM ENDED =====

# 2. Insufficient Payment
===== E-COMMERCE ORDER PROCESSING SYSTEM =====

Enter Customer ID: C102
Enter Customer Name: Priya

========== AVAILABLE PRODUCTS ==========

101 - Laptop - Rs. 45000
102 - Smartphone - Rs. 20000
103 - Headphones - Rs. 2000
104 - Keyboard - Rs. 1500
105 - Mouse - Rs. 800

Enter Product ID: 103
Enter Quantity: 2

========== ORDER SUMMARY ==========

Customer ID: C102
Customer Name: Priya
Product Name: Headphones
Quantity: 2
Price per Unit: Rs. 2000
Subtotal: Rs. 4000
Discount: Rs. 0
Final Amount: Rs. 4000

Enter Payment Amount: Rs.3000

========== PAYMENT DETAILS ==========

Payment Status: INSUFFICIENT
Remaining Amount: Rs. 1000.0

========== ORDER RECONCILIATION ==========

Order Amount: Rs. 4000
Payment Amount: Rs. 3000.0
Reconciliation Status: MISMATCHED
Order Status: PENDING

Do you want to process another order? (yes/no): no

Thank you for shopping with us!
===== PROGRAM ENDED =====

# 3. Successful Payment with Extra Amount

===== E-COMMERCE ORDER PROCESSING SYSTEM =====

Enter Customer ID: C103
Enter Customer Name: Arjun

========== AVAILABLE PRODUCTS ==========

101 - Laptop - Rs. 45000
102 - Smartphone - Rs. 20000
103 - Headphones - Rs. 2000
104 - Keyboard - Rs. 1500
105 - Mouse - Rs. 800

Enter Product ID: 104
Enter Quantity: 2

========== ORDER SUMMARY ==========

Customer ID: C103
Customer Name: Arjun
Product Name: Keyboard
Quantity: 2
Price per Unit: Rs. 1500
Subtotal: Rs. 3000
Discount: Rs. 0
Final Amount: Rs. 3000

Enter Payment Amount: Rs.3500

========== PAYMENT DETAILS ==========

Payment Status: SUCCESSFUL
Change to Return: Rs. 500.0

========== ORDER RECONCILIATION ==========

Order Amount: Rs. 3000
Payment Amount: Rs. 3500.0
Reconciliation Status: MATCHED
Order Status: CONFIRMED

Do you want to process another order? (yes/no): no

Thank you for shopping with us!
===== PROGRAM ENDED =====
