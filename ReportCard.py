import os
import json

class StudentReportCard:
    def add_student():
        Student_List = []
        while True:
            Ch = input("Do you want to add more students? (Y/N): ")
            if Ch.upper().strip() == 'N':
                break
            name = input("enter name of the student: ")
            Roll = int(input("Enter his/her roll no. : "))
            Marks = int(input("Enter Marks obtained: "))

            S_Dict = {
                "Name": name,
                "Roll no.": Roll,
                "Marks": Marks
            }
            Student_List.append(S_Dict)

        if os.path.exists('ReportCard.json'):
            with open('ReportCard.json', 'r') as file:
                data = json.load(file)
            Student_List.extend(data)

        with open('ReportCard.json', 'w') as file:
            json.dump(Student_List, file)
        print("Student data saved successfully")

    def view_details():
        if not os.path.exists('ReportCard.json'):
            print("No Student Report Card found")
            return
        else:
            with open("ReportCard.json", "r") as file:
                Students_Data = json.load(file)
                for Student_Data in Students_Data:
                    print("Name", Student_Data['Name'])
                    print("Roll no.", Student_Data["Roll no."])
                    print("Marks: ", Student_Data["Marks"])

    def roll_src(Rollno):
        if not os.path.exists('ReportCard.json'):
            print("No Student Report Card found")
            return
        with open("ReportCard.json", "r") as file:
            Students_list = json.load(file)

        found = False
        for Student in Students_list:
            if Student['Roll no.'] == Rollno:
                found = True
                print("Student Found!")
                print("Name", Student['Name'])
                print("Roll no.", Student["Roll no."])
                print("Marks: ", Student["Marks"])
                break
        if found == False:
            print("Student not found")

    def upd_marks():
        if not os.path.exists('ReportCard.json'):
            print("No Student Report Card found")
            return
        else:
            name = input("Enter Student name you want to update marks of : ")
            with open("ReportCard.json", "r") as file:
                Students_Data = json.load(file)
            for Student_Data in Students_Data:
                if Student_Data["Name"] == name:
                    new = int(input("Enter updated marks: "))
                    Student_Data["Marks"] = new
            with open("ReportCard.json", "w") as file:
                json.dump(Students_Data, file)
            print("Student marks updated successfully!")
        return

    def delete_student():
        if not os.path.exists('ReportCard.json'):
            print("No Student Report Card found")
            return
        else:
            name = input("Enter Student name you want to delete details of: ")
            with open("ReportCard.json", "r") as file:
                Students_Data = json.load(file)
            Student_found = False
            for Student_Data in Students_Data:
                if Student_Data["Name"] == name:
                    Students_Data.remove(Student_Data)
                    Student_found = True
            if Student_found == False:
                print("Student not found")
            with open("ReportCard.json", "w") as file:
                json.dump(Students_Data, file)
            print("Student data deleted successfully!")
        return

    while True:
        print("\n===== Student Report Card Menu =====")
        print('1. Add Student')
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            view_details()
        elif choice == 3:
            Rollno = int(input("Enter the roll no. "))
            roll_src(Rollno)
        elif choice == 4:
            upd_marks()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            print("Exited successfully.")
            break
        else:
            print("Error: Invalid option selected.")