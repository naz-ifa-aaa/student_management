from student_management.assessment_class import Assessment


class Quiz(Assessment):
    def __init__(self, title, max_score):
        super().__init__(title, max_score)


    def display_info(self):
        print(f"Quiz : {self.title}and the score is : {self.max_score}")


    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >=70:
            return "Great quiz result"
        else:
            return "Needs more practice"