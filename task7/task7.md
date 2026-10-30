## Student Timetable Conflict Detection
Here is a professional project format for Student Timetable Conflict Detection, suitable for a first-year B.Tech CSE-AIML student.
# 1. Problem Statement
The Student Timetable Conflict Detection System is designed to identify scheduling conflicts in a student's academic timetable. The system accepts details such as subject names, classroom numbers, days, and class start and end times.

The program compares the scheduled classes to determine whether two or more classes overlap on the same day. If an overlap is detected, the system displays a timetable conflict message and identifies the conflicting subjects. Otherwise, it confirms that the timetable is conflict-free. This system helps students and academic coordinators organize class schedules efficiently and avoid overlapping lectures.
# 2. Algorithm
1. Start the program.
2. Enter the total number of classes in the timetable.
3. For each class, enter the subject name, day, start time, end time, and classroom number.
4. Validate that each class has a valid start time and an end time later than its start time.
5. Compare each class with every subsequent class.
6. Check whether both classes are scheduled on the same day.
7. If they are on the same day, compare their time intervals.
8. If one class starts before the other class ends and ends after the other class starts, identify a timetable conflict.
9. Display the names of the conflicting subjects, day, and overlapping time.
10. Repeat the comparison until all pairs of classes have been checked.
11. If no conflicts are found, display a message confirming that the timetable is conflict-free.
12. Stop the program.

# flowchart TD
    A([Start]) --> B[/Enter Number of Classes/]
    B --> C[/Enter Subject, Day, Start Time, End Time and Room/]
    C --> D{All Class Times Valid?}
    D -->|No| E[/Display Invalid Timetable Data/]
    E --> Z([Stop])
    D -->|Yes| F[Initialize Conflict Found = False]
    F --> G[Select a Pair of Classes]
    G --> H{More Pairs to Compare?}
    H -->|No| I{Conflict Found?}
    H -->|Yes| J{Same Day?}
    J -->|No| G
    J -->|Yes| K{Time Intervals Overlap?}
    K -->|Yes| L[/Display Conflicting Classes/]
    L --> M[Set Conflict Found = True]
    M --> G
    K -->|No| G
    I -->|Yes| N[/Display Timetable Conflicts Found/]
    I -->|No| O[/Display Timetable is Conflict-Free/]
    N --> Z
    O --> Z

# 4. Input
The program requires the following inputs from the user.
Input	Description	Example
Number of classes	Total classes to check	3
Subject name	Name of the subject	Mathematics
Day	Day of the scheduled class	Monday
Start time	Class starting time	09:00
End time	Class ending time	10:00
Classroom number	Room assigned to the class	A101

# Expected output
===== TIMETABLE CONFLICT REPORT =====

Conflict Detected!

Subject 1: Mathematics
Subject 2: Physics
Day: Monday
Overlapping Time: 09:30 - 10:00

Programming: No conflict detected.

=====================================

# 5. Conflict detection logic
For two classes scheduled on the same day, a conflict exists if:

Start1 < END2

Start2 > END1

and
\[
\text{Start}_2 < \text{End}_1
\]                                md
