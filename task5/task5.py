# Text-Based Invoice Data Extraction System

print("===== TEXT-BASED INVOICE DATA EXTRACTION =====")

# Input invoice text
invoice_text = input("Enter invoice number: ")
customer_name = input("Enter customer name: ")
invoice_date = input("Enter invoice date (DD-MM-YYYY): ")
product_name = input("Enter product name: ")

# Input quantity, price, and tax
try:
    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: Rs. "))
    tax_percentage = float(input("Enter tax percentage: "))

    # Validate input
    if quantity <= 0 or unit_price < 0:
        print("Invalid input! Quantity must be positive and price cannot be negative.")

    elif tax_percentage < 0 or tax_percentage > 100:
        print("Invalid input! Tax percentage must be between 0 and 100.")

    else:
        # Extracted invoice details
        invoice_number = invoice_text.strip()

        # Calculate product amount and subtotal
        product_amount = quantity * unit_price
        subtotal = product_amount

        # Calculate tax and final total
        tax_amount = subtotal * tax_percentage / 100
        final_total = subtotal + tax_amount

        # Display extracted invoice
        print("\n===== EXTRACTED INVOICE DETAILS =====")
        print("Invoice Number:", invoice_number)
        print("Customer Name:", customer_name)
        print("Invoice Date:", invoice_date)

        print("\n----- PRODUCT DETAILS -----")
        print("Product Name:", product_name)
        print("Quantity:", quantity)
        print(f"Unit Price: Rs. {unit_price:.2f}")
        print(f"Product Amount: Rs. {product_amount:.2f}")

        print("\n----- BILL SUMMARY -----")
        print(f"Subtotal: Rs. {subtotal:.2f}")
        print(f"Tax ({tax_percentage}%): Rs. {tax_amount:.2f}")
        print(f"Final Invoice Total: Rs. {final_total:.2f}")
        print("======================================")

except ValueError:
    print("Invalid input! Enter numeric values for quantity, price, and tax.")

# Expected output
===== TEXT-BASED INVOICE DATA EXTRACTION =====
Enter invoice number: INV101
Enter customer name: Rahul
Enter invoice date (DD-MM-YYYY): 29-10-2026
Enter product name: Keyboard
Enter quantity: 2
Enter unit price: Rs. 800
Enter tax percentage: 18

===== EXTRACTED INVOICE DETAILS =====
Invoice Number: INV101
Customer Name: Rahul
Invoice Date: 29-10-2026

----- PRODUCT DETAILS -----
Product Name: Keyboard
Quantity: 2
Unit Price: Rs. 800.00
Product Amount: Rs. 1600.00

----- BILL SUMMARY -----
Subtotal: Rs. 1600.00
Tax (18.0%): Rs. 288.00
Final Invoice Total: Rs. 1888.00
======================================                               py
