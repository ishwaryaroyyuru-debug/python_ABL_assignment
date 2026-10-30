# Student Timetable Conflict Detection System

from datetime import datetime

print("===== STUDENT TIMETABLE CONFLICT DETECTION =====")

try:
    # Input number of classes
    n = int(input("Enter number of classes: "))

    if n <= 0:
        print("Invalid input! Number of classes must be positive.")
    else:
        timetable = []

        # Input class details
        for i in range(n):
            print(f"\nEnter details for Class {i + 1}")

            subject = input("Enter subject name: ").strip()
            day = input("Enter day: ").strip().lower()
            start = input("Enter start time (HH:MM): ").strip()
            end = input("Enter end time (HH:MM): ").strip()
            room = input("Enter classroom: ").strip()

            # Convert times to minutes
            start_time = datetime.strptime(start, "%H:%M")
            end_time = datetime.strptime(end, "%H:%M")

            start_minutes = start_time.hour * 60 + start_time.minute
            end_minutes = end_time.hour * 60 + end_time.minute

            # Validate class details
            if (
                not subject
                or not day
                or not room
                or end_minutes <= start_minutes
            ):
                raise ValueError(
                    "Invalid class details or end time must be after start time."
                )

            timetable.append({
                "subject": subject,
                "day": day,
                "start": start_minutes,
                "end": end_minutes,
                "room": room
            })

        # Detect timetable conflicts
        conflicts_found = False

        print("\n===== TIMETABLE CONFLICT REPORT =====")

        for i in range(n):
            for j in range(i + 1, n):

                class1 = timetable[i]
                class2 = timetable[j]

                # Check whether classes occur on the same day
                if class1["day"] == class2["day"]:

                    # Check overlapping time intervals
                    if (
                        class1["start"] < class2["end"]
                        and class2["start"] < class1["end"]
                    ):
                        conflicts_found = True

                        overlap_start = max(
                            class1["start"], class2["start"]
                        )
                        overlap_end = min(
                            class1["end"], class2["end"]
                        )

                        start_display = (
                            f"{overlap_start // 60:02d}:"
                            f"{overlap_start % 60:02d}"
                        )
                        end_display = (
                            f"{overlap_end // 60:02d}:"
                            f"{overlap_end % 60:02d}"
                        )

                        print("\nConflict Detected!")
                        print("Subject 1:", class1["subject"])
                        print("Subject 2:", class2["subject"])
                        print("Day:", class1["day"].capitalize())
                        print(
                            f"Overlapping Time: "
                            f"{start_display} - {end_display}"
                        )

        if not conflicts_found:
            print("No timetable conflicts detected.")
            print("The timetable is conflict-free.")

        print("=====================================")

except ValueError as error:
    print("Invalid input:", error)

# sample Output:
===== STUDENT TIMETABLE CONFLICT DETECTION =====
Enter number of classes: 3

Enter details for Class 1
Enter subject name: Mathematics
Enter day: Monday
Enter start time (HH:MM): 09:00
Enter end time (HH:MM): 10:00
Enter classroom: A101

Enter details for Class 2
Enter subject name: Physics
Enter day: Monday
Enter start time (HH:MM): 09:30
Enter end time (HH:MM): 10:30
Enter classroom: A102

Enter details for Class 3
Enter subject name: Programming
Enter day: Tuesday
Enter start time (HH:MM): 09:00
Enter end time (HH:MM): 10:00
Enter classroom: Lab1

===== TIMETABLE CONFLICT REPORT =====

Conflict Detected!
Subject 1: Mathematics
Subject 2: Physics
Day: Monday
Overlapping Time: 09:30 - 10:00
=====================================
