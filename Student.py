class Student:
    def __init__(self,student_id,name,email):
        self.__student_id = student_id
        self.__name = name
        self.__email = email
        self.courses = []

    @property
    def get_id(self):
        return self.__student_id


    @property
    def get_name(self):
        return self.__name


    @property
    def email(self):
        return self.__email


    @email.setter
    def email(self,value):
        if "@"in value and "." in value.split("@")[-1]:
            self.__email = value
        else:
            print("Invalid email")
            if self.__email is None:
                print("Invalid email")


    def enroll_course(self,course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)
            print(f"course {course_code} enrolled")


    def display_info(self):
        print(f"student id: {self.__student_id}, name: {self.__name}, email: {self.__email} registered")
        print(f"courses: {self.courses}")

