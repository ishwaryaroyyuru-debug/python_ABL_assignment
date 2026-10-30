# Comprehensive Smart Campus Management Simulation

# Student Information
print("===== SMART CAMPUS MANAGEMENT SYSTEM =====")

student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")
department = input("Enter Department: ")
year = input("Enter Year: ")

# Library Information
books = {
    "Python Programming": True,
    "Data Structures": True,
    "Computer Networks": True
}

# Campus Facilities
facilities = {
    "Seminar Hall": True,
    "Computer Lab": True,
    "Sports Ground": True
}

# Fee Information
fee_paid = 0

while True:
    print("\n========== MAIN MENU ==========")
    print("1. Student Information")
    print("2. Attendance Management")
    print("3. Library Management")
    print("4. Fee Payment Management")
    print("5. Campus Facility Booking")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        # 1. Student Information
        if choice == 1:
            print("\n--- STUDENT INFORMATION ---")
            print("Student ID:", student_id)
            print("Student Name:", student_name)
            print("Department:", department)
            print("Year:", year)

        # 2. Attendance Management
        elif choice == 2:
            print("\n--- ATTENDANCE MANAGEMENT ---")

            total_classes = int(input("Enter Total Classes: "))
            attended_classes = int(input("Enter Classes Attended: "))

            if total_classes <= 0:
                print("Total classes must be greater than zero.")
            elif attended_classes < 0 or attended_classes > total_classes:
                print("Invalid attendance details.")
            else:
                percentage = (attended_classes / total_classes) * 100

                print("Attendance Percentage:",
                      round(percentage, 2), "%")

                if percentage >= 75:
                    print("Attendance Status: Satisfactory")
                else:
                    print("Attendance Status: Shortage")

        # 3. Library Management
        elif choice == 3:
            print("\n--- LIBRARY MANAGEMENT ---")

            print("Available Books:")
            for book, available in books.items():
                status = "Available" if available else "Borrowed"
                print(book, "-", status)

            book_name = input("Enter Book Name: ")

            if book_name not in books:
                print("Book not found.")
            else:
                print("1. Borrow Book")
                print("2. Return Book")

                operation = input("Select Operation: ")

                if operation == "1":
                    if books[book_name]:
                        books[book_name] = False
                        print("Book borrowed successfully!")
                    else:
                        print("Book is already borrowed.")

                elif operation == "2":
                    if not books[book_name]:
                        books[book_name] = True
                        print("Book returned successfully!")
                    else:
                        print("Book is already available.")

                else:
                    print("Invalid library operation.")

        # 4. Fee Payment Management
        elif choice == 4:
            print("\n--- FEE PAYMENT MANAGEMENT ---")

            try:
                total_fee = float(input("Enter Total Fee: "))
                amount_paid = float(input("Enter Amount Paid Now: "))

                if total_fee < 0 or amount_paid < 0:
                    print("Fee amounts cannot be negative.")
                elif fee_paid + amount_paid > total_fee:
                    print("Payment exceeds the remaining fee.")
                else:
                    fee_paid += amount_paid
                    remaining_fee = total_fee - fee_paid

                    print("Total Fee: Rs.", total_fee)
                    print("Total Amount Paid: Rs.", fee_paid)
                    print("Remaining Fee: Rs.", remaining_fee)

                    if remaining_fee == 0:
                        print("Payment Status: Fully Paid")
                    elif fee_paid > 0:
                        print("Payment Status: Partially Paid")
                    else:
                        print("Payment Status: Not Paid")

            except ValueError:
                print("Please enter valid fee amounts.")

        # 5. Campus Facility Booking
        elif choice == 5:
            print("\n--- CAMPUS FACILITY BOOKING ---")

            print("Available Facilities:")
            for facility, available in facilities.items():
                status = "Available" if available else "Booked"
                print(facility, "-", status)

            facility_name = input("Enter Facility Name: ")

            if facility_name not in facilities:
                print("Facility not found.")
            elif not facilities[facility_name]:
                print("Facility is already booked.")
            else:
                booking_date = input("Enter Booking Date: ")
                time_slot = input("Enter Time Slot: ")

                if not booking_date or not time_slot:
                    print("Date and time slot cannot be empty.")
                else:
                    facilities[facility_name] = False

                    print("\nBooking Confirmed!")
                    print("Facility:", facility_name)
                    print("Booking Date:", booking_date)
                    print("Time Slot:", time_slot)

        # 6. Exit
        elif choice == 6:
            print("\nThank you for using")
            print("Smart Campus Management System!")
            break

        else:
            print("Invalid choice. Please select 1 to 6.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Sample Output:
===== SMART CAMPUS MANAGEMENT SYSTEM =====

1) Enter Student ID: 101
Enter Student Name: Rahul
Enter Department: CSE-AIML
Enter Year: 1

========== MAIN MENU ==========
1. Student Information
2. Attendance Management
3. Library Management
4. Fee Payment Management
5. Campus Facility Booking
6. Exit

Enter your choice: 1

--- STUDENT INFORMATION ---
Student ID: 101
Student Name: Rahul
Department: CSE-AIML
Year: 1

2)========== MAIN MENU ==========

Enter your choice: 2

--- ATTENDANCE MANAGEMENT ---

Enter Total Classes: 50
Enter Classes Attended: 45

Attendance Percentage: 90.0 %
Attendance Status: Satisfactory

3)========== MAIN MENU ==========

Enter your choice: 3

--- LIBRARY MANAGEMENT ---

Available Books:
Python Programming - Available
Data Structures - Available
Computer Networks - Available

Enter Book Name: Python Programming

1. Borrow Book
2. Return Book

Select Operation: 1

Book borrowed successfully!

4) ========== MAIN MENU ==========

Enter your choice: 4

--- FEE PAYMENT MANAGEMENT ---

Enter Total Fee: 50000
Enter Amount Paid Now: 30000

Total Fee: Rs. 50000.0
Total Amount Paid: Rs. 30000.0
Remaining Fee: Rs. 20000.0

Payment Status: Partially Paid

5) ========== MAIN MENU ==========

Enter your choice: 5

--- CAMPUS FACILITY BOOKING ---

Available Facilities:
Seminar Hall - Available
Computer Lab - Available
Sports Ground - Available

Enter Facility Name: Seminar Hall
Enter Booking Date: 05-11-2026
Enter Time Slot: 10:00 AM

Booking Confirmed!
Facility: Seminar Hall
Booking Date: 05-11-2026
Time Slot: 10:00 AM

6)========== MAIN MENU ==========

Enter your choice: 6

Thank you for using
Smart Campus Management System!
