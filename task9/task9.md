# Manufacturing Cost and Profitability Analysis

print("===== MANUFACTURING COST AND PROFITABILITY ANALYSIS =====")

# Input product details
product_name = input("Enter product name: ")

try:
    quantity_manufactured = int(
        input("Enter quantity manufactured: ")
    )
    quantity_sold = int(
        input("Enter quantity sold: ")
    )

    # Input manufacturing costs
    raw_material_cost = float(
        input("Enter raw material cost: Rs. ")
    )
    labor_cost = float(
        input("Enter labor cost: Rs. ")
    )
    overhead_cost = float(
        input("Enter manufacturing overhead: Rs. ")
    )
    selling_price = float(
        input("Enter selling price per unit: Rs. ")
    )

    # Validate inputs
    if (
        quantity_manufactured <= 0
        or quantity_sold < 0
        or quantity_sold > quantity_manufactured
        or raw_material_cost < 0
        or labor_cost < 0
        or overhead_cost < 0
        or selling_price < 0
    ):
        print("Invalid input! Please check quantities and costs.")

    else:
        # Calculate total manufacturing cost
        total_manufacturing_cost = (
            raw_material_cost + labor_cost + overhead_cost
        )

        # Calculate manufacturing cost per unit
        cost_per_unit = (
            total_manufacturing_cost / quantity_manufactured
        )

        # Calculate sales revenue
        total_revenue = quantity_sold * selling_price

        # Calculate cost of products sold
        cost_of_goods_sold = quantity_sold * cost_per_unit

        # Calculate profit or loss
        profit_loss = total_revenue - cost_of_goods_sold

        # Determine profitability status
        if profit_loss > 0:
            status = "PROFIT"
        elif profit_loss < 0:
            status = "LOSS"
        else:
            status = "BREAK-EVEN"

        # Display financial report
        print("\n===== MANUFACTURING COST REPORT =====")
        print("Product Name:", product_name)
        print("Quantity Manufactured:", quantity_manufactured)
        print("Quantity Sold:", quantity_sold)

        print("\n----- MANUFACTURING COSTS -----")
        print(f"Raw Material Cost: Rs. {raw_material_cost:.2f}")
        print(f"Labor Cost: Rs. {labor_cost:.2f}")
        print(f"Manufacturing Overhead: Rs. {overhead_cost:.2f}")

        print(
            f"Total Manufacturing Cost: "
            f"Rs. {total_manufacturing_cost:.2f}"
        )
        print(f"Manufacturing Cost Per Unit: Rs. {cost_per_unit:.2f}")

        print("\n----- PROFITABILITY ANALYSIS -----")
        print(f"Total Sales Revenue: Rs. {total_revenue:.2f}")
        print(f"Cost of Products Sold: Rs. {cost_of_goods_sold:.2f}")
        print(f"Profit/Loss: Rs. {profit_loss:.2f}")
        print("Profitability Status:", status)

        print("=======================================")

except ValueError:
    print("Invalid input! Enter valid numeric values for quantities and costs.")

# Sample Output:
===== MANUFACTURING COST AND PROFITABILITY ANALYSIS =====
Enter product name: Chairs
Enter quantity manufactured: 100
Enter quantity sold: 80
Enter raw material cost: Rs. 10000
Enter labor cost: Rs. 5000
Enter manufacturing overhead: Rs. 3000
Enter selling price per unit: Rs. 300

===== MANUFACTURING COST REPORT =====
Product Name: Chairs
Quantity Manufactured: 100
Quantity Sold: 80

----- MANUFACTURING COSTS -----
Raw Material Cost: Rs. 10000.00
Labor Cost: Rs. 5000.00
Manufacturing Overhead: Rs. 3000.00
Total Manufacturing Cost: Rs. 28000.00
Manufacturing Cost Per Unit: Rs. 280.00

----- PROFITABILITY ANALYSIS -----
Total Sales Revenue: Rs. 24000.00
Cost of Products Sold: Rs. 22400.00
Profit/Loss: Rs. 1600.00
Profitability Status: PROFIT
=======================================
