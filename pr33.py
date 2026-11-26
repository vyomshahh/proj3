print(" ")
print("Welcome to Student Data Organizer!")
print(" ")

student = [
    {
        "ID": 101,
        "Name": "Vyom",
        "Age": 18,
        "Grade": "A+",
        "Date of Birth(YYYY-MM-DD)": "2008-07-01",
        "Subjects": ["Java", "Css"]
    }
]

while True:
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    print()

    choice = int(input("Enter Your Choice:"))
    print()

    if choice < 1 or choice > 6:
        print("Invalid choice, Enter valid choice!")
        continue

    elif choice == 1:

        student_id = int(input("Enter Student ID:"))

        for s in student:
            if s["ID"] == student_id:
                print("Student already exists. If you want to update then choose 3!")
                break
        else:
            print()
            print("Add Student")
            print()

            name = input("Enter Name:")
            age = int(input("Enter Age:"))
            grade = input("Enter Grade:")
            dob = input("Enter Date of Birth(YYYY-MM-DD):")
            subjects = input("Enter Subjects(comma-separated):")

            immutable_info = (student_id, dob)

            student_all_info = {
                "ID": student_id,
                "Immutable_info": immutable_info,
                "Name": name,
                "Age": age,
                "Grade": grade,
                "Subjects": [sub.strip() for sub in subjects.split(",")]
            }

            student.append(student_all_info)

            print("Student added successfully.")

    elif choice == 2:

        for s in student:

            print("\nStudent ID: {}".format(s["ID"]))
            print("Name: {}".format(s["Name"]))
            print("Age: %d" % s["Age"])
            print(f"Grade: {s['Grade']}")
            print("Date of Birth:", s["Immutable_info"][1] if "Immutable_info" in s else s["Date of Birth(YYYY-MM-DD)"])
            print("Subjects:", ", ".join(s["Subjects"]))

    elif choice == 3:

        print()
        print("Update Student Information")
        print()

        student_id = int(input("Enter Student ID to update:"))

        for s in student:

            if s["ID"] == student_id:

                name = input("Enter Name:")
                age = int(input("Enter Age:"))
                grade = input("Enter Grade:")
                dob = input("Enter Date of Birth(YYYY-MM-DD):")
                subjects = input("Enter Subjects(comma-separated):")

                s["Name"] = name
                s["Age"] = age
                s["Grade"] = grade
                s["Date of Birth(YYYY-MM-DD)"] = dob
                s["Subjects"] = [sub.strip() for sub in subjects.split(",")]

                print("Student information updated successfully.")
                break

        else:
            print("Student ID not found.")

    elif choice == 4:

        print()
        print("Delete Student")
        print()

        student_id = int(input("Enter Student ID to delete:"))

        for s in student:

            if s["ID"] == student_id:

                student.remove(s)
                print("Student deleted successfully.")
                break

        else:
            print("Student ID not found.")

    elif choice == 5:

        print()
        print("Display Subjects Offered")
        print()

        subjects_set = set()

        for s in student:
            subjects_set.update(s["Subjects"])

        print("Subjects offered:")

        for subject in sorted(subjects_set):
            print(subject)

    elif choice == 6:

        print()
        print("Exiting the program. Goodbye!")
        break