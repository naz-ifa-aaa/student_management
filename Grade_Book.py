class GradeBook:
    def __init__(self,passing_grade=55):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.enrollments = {}
        self.passing_grade = passing_grade


    def add_student(self,student):
        self.students[student.student_id] = student
        if student.student_id not in self.enrollments:
            self.enrollments[student.student_id] = set()
            self.grades[student.student_id] = {}
        print(f"Student{student.student_id} added successfully.")


    def add_course(self,course):
        self.courses[course.course_id] = course
        print(f"Course({course.name}){course.course_id} added successfully.")


    def enroll_student(self,student_id,course_code):
        if student_id not in self.students:
            print("Error: Student does not exist.")
            return
        if course_code not in self.courses:
            print("Error: Course does not exist.")
            return

        self.enrollments[student_id].add(course_code)
        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}
        print(f"Student{student_id} enroll successfully in {course_code}.")


    def add_assignment(self,course_code,assessment):
        if course_code not in self.courses:
            print("Error: Course does not exist.")
            return
        self.courses[course_code].assessments.append(assessment)
        print(f"Assessment {assessment}added to course {course_code} .")

    def record_grade(self,student_id,course_code,assessment_title,score):
        if student_id not in self.students:
            print("Error: Student does not exist.")
            return
        if course_code not in self.courses:
            print("Error: Course does not exist.")
            return
        if course_code not in self.enrollments[student_id]:
            print("Error: Student is not enrolled in this course.")
            return
        if assessment_title not in self.courses[course_code].assessments:
            print("Error: Assessment does not exist in this course.")
            return
        self.grades[student_id][course_code][assessment_title] = score
        print(f"Recorded score {score} for {student_id} in {assessment_title}.")


    def calculate_average(self,student_id,course_code):
        if student_id not in self.grades or course_code not in self.grades[student_id]:
            return 0.0

        scores = self.grades[student_id][course_code].values()
        if not scores:
            return 0.0
        return sum(scores)/len(scores)

    def get_result(self,average):
        return "Passed" if average >= self.passing_grade else "Failed"

    def get_letter_grade(self, average):
        if average >= 90: return "A"
        elif average >= 80: return "B"
        elif average >= 70: return "C"
        elif average >= 60: return "D"
        else: return "F"


    def show_report(self,student_id):
        if student_id not in self.students:
            print("Error: Student not found.")
            return

        student = self.students[student_id]
        print(f"\n---reported for {student.name},{student_id}---")
        enrolled_course = self.enrollments.get(student_id,[])

        if not enrolled_course:
            print("Not enrolled in any courses.")
            return

        for course_code in enrolled_course:
            course = self.courses[course_code]
            average = self.calculate_average(student_id,course_code)
            letter = self.get_letter_grade(average)
            status = self.get_result(average)

            print(f"Course:{course.name} ({course_code})")
            print(f"Grades: {dict(self.grades[student_id][course_code])}")
            print(f"Average: {average:.2f}, Letter: {letter}, Status: {status}")

    def search_student(self,keyword):
        result = []
        for student_id,student in self.students.items():
            if keyword.lower() in student_id.lower() or keyword.lower in student.name.lower():
                result.append(student)
        if not result:
            print(f"No student found matching {keyword}.")
        for student in result:
            print(f"Found: ID:{student.student_id}, Name:{student.name}")


    def delete_student(self,student_id):
        if student_id  in self.students:
            del self.students[student_id]
            if student_id in self.enrollments:
                del self.enrollments[student_id]
            if student_id in self.grades:
                del self.grades[student_id]
            print(f"Student{student_id}removed completely.")
        else:
            print("Error: Student not found.")




