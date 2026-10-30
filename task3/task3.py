# University Admission Decision Engine

print("===== UNIVERSITY ADMISSION DECISION ENGINE =====")

# Input student details
student_name = input("Enter student name: ")
application_id = input("Enter application ID: ")

# Input academic scores
qualifying_percentage = float(
    input("Enter qualifying examination percentage: ")
)
entrance_score = float(
    input("Enter entrance examination score: ")
)

# Input minimum eligibility criteria
minimum_percentage = float(
    input("Enter minimum qualifying percentage: ")
)
minimum_entrance_score = float(
    input("Enter minimum entrance score: ")
)

# Validate input values
if (
    qualifying_percentage < 0 or qualifying_percentage > 100
    or entrance_score < 0 or entrance_score > 100
    or minimum_percentage < 0 or minimum_percentage > 100
    or minimum_entrance_score < 0 or minimum_entrance_score > 100
):
    print("\nInvalid input! Scores and percentages must be between 0 and 100.")

else:
    # Check admission eligibility
    if (
        qualifying_percentage >= minimum_percentage
        and entrance_score >= minimum_entrance_score
    ):
        admission_status = "ELIGIBLE FOR ADMISSION"
    else:
        admission_status = "NOT ELIGIBLE FOR ADMISSION"

    # Display admission report
    print("\n===== UNIVERSITY ADMISSION REPORT =====")
    print("Student Name:", student_name)
    print("Application ID:", application_id)
    print(f"Qualifying Examination Percentage: {qualifying_percentage:.2f}%")
    print(f"Entrance Examination Score: {entrance_score:.2f}")
    print("Admission Status:", admission_status)
    print("=======================================")
# Sample output
===== UNIVERSITY ADMISSION DECISION ENGINE =====
Enter student name: Rahul
Enter application ID: 2026
Enter qualifying examination percentage: 85
Enter entrance examination score: 78
Enter minimum qualifying percentage: 60
Enter minimum entrance score: 50

===== UNIVERSITY ADMISSION REPORT =====
Student Name: Rahul
Application ID: 2026
Qualifying Examination Percentage: 85.00%
Entrance Examination Score: 78.00
Admission Status: ELIGIBLE FOR ADMISSION
=======================================
