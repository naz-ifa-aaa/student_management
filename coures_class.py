class CourseClass:
    def __init__(self,course_code,course_name, students, assessment):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.assessment = []


    def add_student( self ,student_id):
        if student_id not in self.students:
            self.students.append(student_id)
            print(f"The student {student_id} has been added to the course")
        else:
            print(f"The student {student_id} is already in the course")



    def add_assessment( self ,assessment):
        self.assessment.append(assessment)
        print(f"The assessment {assessment} has been added to the course")


    def find_assessment( self , title):
        for assessment in self.assessment:
            if assessment.title == title:
                return assessment
        return None


    def display_info(self):
        print(f"The course code {self.course_code}.")
        print(f"The course name {self.course_name}.")
        print(f"Enrolled students : {len(self.students)}.")
