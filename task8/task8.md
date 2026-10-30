## Manufacturing Cost and Profitability Analysis
Here is a professional project format for Manufacturing Cost and Profitability Analysis, suitable for a first-year B.Tech CSE-AIML student.
# 1. Problem Statement
The Manufacturing Cost and Profitability Analysis System is designed to calculate the total cost of manufacturing products and evaluate the profitability of a manufacturing business. The system accepts details such as the quantity of products manufactured, raw material costs, labor costs, overhead expenses, selling price per unit, and quantity of products sold.

The program calculates the total manufacturing cost, cost per unit, total sales revenue, and overall profit or loss. It then determines whether the business is profitable based on the difference between sales revenue and manufacturing costs. This system helps manufacturers understand their expenses, set suitable selling prices, and make informed financial decisions.

Note: This beginner-level project assumes that all products manufactured during the period have the same unit cost and that the cost of unsold inventory is excluded from the profit calculation only when no products remain unsold.
# 2. Algorithm
1. Start the program.
2. Enter the product name.
3. Enter the quantity of products manufactured and the quantity sold.
4. Enter the raw material cost, labor cost, and manufacturing overhead cost.
5. Enter the selling price per unit.
6. Validate that quantities and costs are non-negative, the manufactured quantity is positive, and the quantity sold does not exceed the quantity manufactured.
7. Calculate the total manufacturing cost by adding raw material, labor, and overhead costs.
8. Calculate the manufacturing cost per unit by dividing total manufacturing cost by the quantity manufactured.
9. Calculate total sales revenue by multiplying the quantity sold by the selling price per unit.
10. Calculate the cost of products sold by multiplying the manufacturing cost per unit by the quantity sold.
11. Calculate profit or loss by subtracting the cost of products sold from total sales revenue.
12. If profit is positive, display a profit result.
13. If profit is negative, display a loss result.
14. If profit is zero, display a break-even result.
15. Display the manufacturing cost, cost per unit, revenue, profit or loss, and profitability status.
16. Stop the program.


# flowchart TD
    A([Start]) --> B[/Enter Product Name and Quantities/]
    B --> C[/Enter Material, Labor, Overhead Costs and Selling Price/]
    C --> D{Are Inputs Valid?}
    D -->|No| E[/Display Invalid Input/]
    E --> Z([Stop])
    D -->|Yes| F[Calculate Total Manufacturing Cost]
    F --> G[Calculate Cost Per Unit]
    G --> H[Calculate Total Sales Revenue]
    H --> I[Calculate Cost of Products Sold]
    I --> J[Calculate Profit or Loss]
    J --> K{Profit or Loss?}
    K -->|Positive| L[Display Profit]
    K -->|Negative| M[Display Loss]
    K -->|Zero| N[Display Break-even]
    L --> O[/Display Financial Report/]
    M --> O
    N --> O
    O --> Z
    
# 4. Input
The program requires the following inputs from the user.
Input	Description	Example
Product name	Name of the manufactured product	Chairs
Quantity manufactured	Total units produced	100
Quantity sold	Total units sold	80
Raw material cost	Total cost of materials	₹10,000
Labor cost	Total wages for production	₹5,000
Manufacturing overhead	Electricity, machine maintenance, etc.	₹3,000
Selling price per unit	Selling price of each unit	₹300

# Expected output
===== MANUFACTURING COST REPORT =====

Product Name: Chairs
Quantity Manufactured: 100
Quantity Sold: 80

Raw Material Cost: Rs. 10000
Labor Cost: Rs. 5000
Manufacturing Overhead: Rs. 3000

Total Manufacturing Cost: Rs. 28000
Manufacturing Cost Per Unit: Rs. 280.00

Total Sales Revenue: Rs. 24000
Cost of Products Sold: Rs. 22400

Profit: Rs. 1600
Profitability Status: PROFIT

=====================================

5. Sample calculation
Step 1: Total manufacturing cost

10000+5000+3000=₹28000

Step 2: Manufacturing cost per unit

₹28000/100=₹280


Step 3: Total sales revenue

80 * ₹300=₹24000

Step 4: Cost of products sold

80 * ₹280=₹22400

Step 5: Profit
                     8md
₹24000-₹22400=₹1600
