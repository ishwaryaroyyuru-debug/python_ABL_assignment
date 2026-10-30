## University Admission Decision Engine
Here is a professional project format for University Admission Decision Engine, suitable for a first-year B.Tech CSE-AIML student.
# 1. Problem Statement
The University Admission Decision Engine is designed to evaluate students' eligibility for admission to a university based on their academic performance and admission requirements. The system accepts student details, entrance examination marks, and qualifying examination percentages, then compares the entered values against predefined eligibility criteria.

Based on the criteria, the program determines whether a student is eligible or not eligible for admission. It displays the student's details, academic scores, and final admission decision. This system helps simplify the initial screening process, improve consistency, and reduce manual errors in admission evaluation.

Note: The eligibility criteria used in this project are illustrative and should be adjusted according to the university's actual admission rules.
# 2. Algorithm
1. Start the program.
2. Enter the student's name and application ID.
3. Enter the qualifying examination percentage.
4. Enter the entrance examination score.
5. Enter the minimum qualifying percentage and minimum entrance score required for admission.
6. Validate the entered values to ensure they are within the permitted ranges.
7. Check whether the qualifying percentage meets the minimum requirement.
8. Check whether the entrance examination score meets the minimum requirement.
9. If both conditions are satisfied, classify the student as Eligible for Admission.
10. Otherwise, classify the student as Not Eligible for Admission.
11. Display the student's details, scores, and admission decision.
12. Stop the program.


# flowchart TD
    A([Start]) --> B[/Enter Student Name and Application ID/]
    B --> C[/Enter Qualifying Percentage and Entrance Score/]
    C --> D[/Enter Minimum Eligibility Criteria/]
    D --> E{Are all scores within valid ranges?}
    E -->|No| F[/Display Invalid Input/]
    F --> K([Stop])
    E -->|Yes| G{Qualifying Percentage >= Minimum?}
    G -->|No| J[/Display Not Eligible/]
    G -->|Yes| H{Entrance Score >= Minimum?}
    H -->|Yes| I[/Display Eligible for Admission/]
    H -->|No| J
    I --> L[/Display Student Details and Decision/]
    J --> L
    L --> K
# 4. Input
The program requires the following inputs from the user.
Input	Description	Example
Student name	Name of the applicant	Rahul
Application ID	Unique application number	2026
Qualifying percentage	Percentage in the qualifying examination	85
Entrance examination score	Score obtained in the entrance test	78
Minimum qualifying percentage	Required minimum percentage	60
Minimum entrance score	Required minimum entrance score	50

# Expected output
===== UNIVERSITY ADMISSION REPORT =====

Student Name: Rahul
Application ID: 2026
Qualifying Examination Percentage: 85%
Entrance Examination Score: 78

Admission Status: ELIGIBLE FOR ADMISSION
=======================================                    md
