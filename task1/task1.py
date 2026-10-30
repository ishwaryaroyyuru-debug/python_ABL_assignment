# Hospital Billing and Patient Classification System

print("===== HOSPITAL BILLING SYSTEM =====")

# Input patient details
patient_name = input("Enter patient name: ")
patient_id = input("Enter patient ID: ")

# Input patient classification
patient_type = input(
    "Enter patient type (Outpatient/Inpatient): "
).strip().lower()

# Input charges
consultation_fee = float(input("Enter consultation fee: Rs. "))
treatment_charges = float(input("Enter treatment charges: Rs. "))

# Initialize room charges
room_charges = 0

# Classify patient and calculate bill
if patient_type == "outpatient":
    classification = "Outpatient"

elif patient_type == "inpatient":
    classification = "Inpatient"

    admission_days = int(
        input("Enter number of admission days: ")
    )
    daily_room_charge = float(
        input("Enter daily room charge: Rs. ")
    )

    if admission_days < 0 or daily_room_charge < 0:
        print("Invalid input: Days and room charges cannot be negative.")
        exit()

    room_charges = admission_days * daily_room_charge

else:
    print("Invalid patient type. Please enter Outpatient or Inpatient.")
    exit()

# Calculate total bill
if consultation_fee < 0 or treatment_charges < 0:
    print("Invalid input: Charges cannot be negative.")
    exit()

total_bill = consultation_fee + treatment_charges + room_charges

# Display hospital bill
print("\n========== HOSPITAL BILL ==========")
print("Patient Name:", patient_name)
print("Patient ID:", patient_id)
print("Patient Classification:", classification)
print("-----------------------------------")
print(f"Consultation Fee: Rs. {consultation_fee:.2f}")
print(f"Treatment Charges: Rs. {treatment_charges:.2f}")
print(f"Room Charges: Rs. {room_charges:.2f}")
print("-----------------------------------")
print(f"Total Bill: Rs. {total_bill:.2f}")
print("===================================")

===== HOSPITAL BILLING SYSTEM =====
Enter patient name: Rahul
Enter patient ID: 101
Enter patient type (Outpatient/Inpatient): Inpatient
Enter consultation fee: Rs. 500
Enter treatment charges: Rs. 2000
Enter number of admission days: 3
Enter daily room charge: Rs. 1500

========== HOSPITAL BILL ==========
Patient Name: Rahul
Patient ID: 101
Patient Classification: Inpatient
-----------------------------------
Consultation Fee: Rs. 500.00
Treatment Charges: Rs. 2000.00
Room Charges: Rs. 4500.00
-----------------------------------
Total Bill: Rs. 7000.00
===================================
