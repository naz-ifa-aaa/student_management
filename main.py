import sys

from Student import Student
from coures_class import CourseClass
from quiz_class import Quiz
from Exam_class import Exam
from Project_class import Project
from Grade_Book import GradeBook

def show_menu():
    print("   COURSE MANAGER SYSTEM   ")
    print("Step 1: Add Student")
    print("Step 2: Add course")
    print("Step 3: Enroll student in course")
    print("Step 4: Add assessment to course")
    print("Step 5: Record student grades")
    print("Step 6: Calculate averages & Show student report")
    print("Step 7: Advanced Student Search")
    print("Step 8: Exit")
    return input("Choose a step(1-8):").strip()

def main():
    gb = GradeBook()

    while True:
        choice= show_menu()
        if choice == "1":
            print("\n---Step 1: Add a New Student---")
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            email = input("Enter student email: ").strip()

            if not student_id or not name or not email:
                print("Error: Please enter your (ID, Name, Email)!")
                continue
            try:
                new_student = Student(student_id,name,email)
                gb.students[student_id] = new_student
                print(f"Student {name} added successfully!")
            except Exception as e:
                print(f"Error during adding {e}")

        elif choice == "2":
            print("\n---Step 2: Add a New Course---")
            course_code = input("Enter course code: ").strip()
            course_name = input("Enter course name: ").strip()

            if not course_code or not course_name:
                print("Error: Please enter your course code & course name!")
                continue
            gb.courses[course_code] = CourseClass(course_code,course_name)
            print(f"Course {course_name} defined successfully!")

        elif choice == "3":
            print("\n---Step 3: Enroll student in course---")
            student_id = input("Enter student ID: ").strip()
            course_code = input("Enter course code: ").strip()

            if student_id not in gb.students:
                print("Error: Student ID does not exist!")
                continue
            if course_code not in gb.courses:
                print("Error: Course code does not exist!")
                continue

            gb.courses[course_code].add_student(student_id)

            if student_id not in gb.enrollments:
                gb.enrollments[student_id] = []
            if course_code not in gb.enrollments[student_id]:
                gb.enrollments[student_id].append(course_code)
                print(f"student {student_id} enrolled in course {course_code}!")
            else:
                print("Student already enrolled in course.")

        elif choice == "4":
            print("\n---Step 4: Add assessment to course---")
            course_code = input("Enter course code: ").strip()
            if course_code not in gb.courses:
                print("Error: Course not found!")
                continue
            print("Select Assessment Type:")
            print("Select type: 1) Quiz 2) Exam 3) project")
            type_choice = input("Enter your choice(1-3): ").strip()

            title = input("Enter assessment title: ").strip()
            try:
                max_score = float(input("Enter max score: "))
                if max_score <= 0:
                    print("Error: Max score must be greater than 0!")
                    continue
            except ValueError:
                print("Error: Invalid number for max score!")
                continue

            if type_choice == "1":
                asm = Quiz(title,max_score)
            elif type_choice == "2":
                asm = Exam(title,max_score)
            elif type_choice == "3":
                asm= Project(title,max_score)
            else:
                print("Error: Invalid choice!")
                continue

            gb.courses[course_code].add_assessment(asm)

        elif choice == "5":
            print("\n---Step 5: Record student grades---")
            student_id= input("Enter student ID: ").strip()
            course_code = input("Enter course code: ").strip()
            title = input("Enter assessment title: ").strip()

            try:
                score = float(input("Enter your score: "))
                if score < 0:
                    print("Error: Score can not be negative !")
                    continue
            except ValueError:
                print("Error: Invalid number for score!")
                continue

            if student_id not in gb.grades:
                gb.grades[student_id] = {}
            if course_code not in gb.grades[student_id]:
                gb.grades[student_id][course_code] = {}

            gb.grades[student_id][course_code][title] = score
            print("Grade recorded successfully!")

        elif choice == "6":
            print("\n---Step 6: student report card---")
            student_id= input("Enter student ID to generate report card: ").strip()
            gb.show_report(student_id)

        elif choice == "7":
            print("\n---Step 7: Advanced Student Search---")
            keyword = input("Enter a keyword or student name to search: ").strip()
            gb.search_student(keyword)


        elif choice == "8":
            print("\n---Exiting The System---")
            sys.exit()
        else:
            print("Error: Invalid choice! Please select a step between 1 and 8.")

if __name__ == "__main__":
    main()










