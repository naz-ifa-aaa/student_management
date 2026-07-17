from student_management.assessment_class import Assessment


class Project(Assessment):
    def __init__(self,title,max_score):
        super().__init__(title,max_score)


    def display_info(self):
        return f"Project {self.title}:Max score{self.max_score}"


    def grade_massage(self,score):
        percentage = score/self.max_score * 100
        if percentage >= 85:
            return"Excellent project"
        elif percentage >= 55:
            return" project submitted"
        else:
            return" Project needs improvement"