## Campus Event Financial Planning
Here is a professional project format for Campus Event Financial Planning, suitable for a first-year B.Tech CSE-AIML student.
# 1. Problem Statement
The Campus Event Financial Planning System is designed to estimate and manage the budget required to organize a college or campus event. The system accepts details such as the number of participants, venue expenses, food expenses, decoration costs, transportation charges, and other miscellaneous expenses.

Based on the given inputs, the program calculates the total event expenditure, estimates the expected income from registration fees or sponsorships, and determines the overall profit or loss. This system helps event organizers allocate resources efficiently, monitor expenses, and make informed financial decisions while planning campus events.
# 2. Algorithm
1. Start the program.
2. Enter the campus event name.
3. Enter the number of participants.
4. Enter the registration fee per participant.
5. Enter the expected sponsorship amount.
6. Enter the estimated venue, food, decoration, transportation, and miscellaneous expenses.
7. Calculate the registration income by multiplying the number of participants by the registration fee.
8. Calculate the total income by adding registration income and sponsorship income.
9. Calculate the total expenditure by adding all event expenses.
10. Calculate the financial balance by subtracting total expenditure from total income.
11. If the balance is positive, display the profit.
12. If the balance is negative, display the loss.
13. If the balance is zero, display that the event is at the break-even point.
14. Display the event name, total income, total expenditure, and final financial result.
15. Stop the program.


# flowchart TD
    A([Start]) --> B[/Enter Event Name and Number of Participants/]
    B --> C[/Enter Registration Fee and Sponsorship Amount/]
    C --> D[/Enter Venue, Food, Decoration, Transport and Other Expenses/]
    D --> E[Calculate Registration Income]
    E --> F[Calculate Total Income]
    F --> G[Calculate Total Expenditure]
    G --> H[Calculate Balance = Total Income - Total Expenditure]
    H --> I{Balance?}
    I -->|Positive| J[Display Profit]
    I -->|Negative| K[Display Loss]
    I -->|Zero| L[Display Break-even]
    J --> M[/Display Financial Report/]
    K --> M
    L --> M
    M --> N([Stop])
# 4. Input
The program requires the following inputs from the user.
Input	Description	Example
Event name	Name of the campus event	Tech Fest
Number of participants	Expected attendees	200
Registration fee	Fee per participant	₹200
Sponsorship amount	Expected sponsor contribution	₹15,000
Venue expenses	Cost of booking the venue	₹10,000
Food expenses	Total catering expenses	₹20,000
Decoration expenses	Cost of decorations	₹5,000
Transportation expenses	Travel-related expenses	₹3,000
Miscellaneous expenses	Other event costs	₹2,000

# Expected output
======= CAMPUS EVENT FINANCIAL REPORT =======

Event Name: Tech Fest
Number of Participants: 200

Registration Income: Rs. 40000
Sponsorship Income: Rs. 15000
Total Income: Rs. 55000

Venue Expenses: Rs. 10000
Food Expenses: Rs. 20000
Decoration Expenses: Rs. 5000
Transportation Expenses: Rs. 3000
Miscellaneous Expenses: Rs. 2000

Total Expenditure: Rs. 40000
Financial Balance: Rs. 15000
Result: PROFIT

=============================================

Calculation

Registration income

200 * ₹200 = ₹40,000

Total income

₹40,000 + ₹15,000 = ₹55,000

Total expenditure

₹10,000+₹20,000+₹5,000+₹3,000+₹2,000=₹40,000

Financial balance

₹55,000-₹40,000=₹15,000
