## Text-Based Invoice Data Extraction
Here is a professional project format for Text-Based Invoice Data Extraction, suitable for a first-year B.Tech CSE-AIML student.
# 1. Problem Statement
The Text-Based Invoice Data Extraction System is designed to extract and organize important information from text-based invoices. The system accepts invoice text containing details such as invoice number, customer name, invoice date, product names, quantities, unit prices, and applicable taxes.

The program identifies the relevant information from the entered text, calculates the subtotal, tax amount, and final invoice total, and displays the extracted details in a structured format. This system helps reduce manual data entry, improve accuracy, and simplify invoice processing for businesses.

For this beginner-level project, invoice information is entered as plain text in a predefined format rather than extracted from scanned images or PDFs.
# 2. Algorithm
1. Start the program.
2. Enter the invoice text containing the invoice number, customer name, invoice date, and product details.
3. Extract the invoice number from the text.
4. Extract the customer name and invoice date.
5. Identify the product name, quantity, and unit price.
6. Calculate the amount for each product by multiplying its quantity by its unit price.
7. Calculate the subtotal by adding all product amounts.
8. Enter the applicable tax percentage.
9. Calculate the tax amount using the subtotal and tax percentage.
10. Calculate the final invoice total by adding the subtotal and tax amount.
11. Display the extracted invoice information and the calculated financial summary.
12. Stop the program.


# flowchart TD
    A([Start]) --> B[/Enter Invoice Text/]
    B --> C[Extract Invoice Number]
    C --> D[Extract Customer Name and Invoice Date]
    D --> E[Extract Product Name, Quantity and Unit Price]
    E --> F[Calculate Product Amounts]
    F --> G[Calculate Subtotal]
    G --> H[/Enter Tax Percentage/]
    H --> I[Calculate Tax Amount]
    I --> J[Calculate Final Invoice Total]
    J --> K[/Display Extracted Data and Invoice Summary/]
    K --> L([Stop])

# 4. Input
The program requires the following information from the invoice.
Input	Description	Example
Invoice number	Unique invoice identifier	INV101
Customer name	Name of the customer	Rahul
Invoice date	Date of invoice generation	29-10-2026
Product name	Name of the purchased item	Keyboard
Quantity	Number of units purchased	2
Unit price	Price per unit	₹800
Tax percentage	Applicable tax rate	18%

# Expected output
===== EXTRACTED INVOICE DETAILS =====

Invoice Number: INV101
Customer Name: Rahul
Invoice Date: 29-10-2026

Product Name: Keyboard
Quantity: 2
Unit Price: Rs. 800.00
Product Amount: Rs. 1600.00

Subtotal: Rs. 1600.00
Tax (18%): Rs. 288.00
Final Invoice Total: Rs. 1888.00

====================================
