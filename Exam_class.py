from student_management.assessment_class import Assessment


class Exam(Assessment):
    def __init__(self, title, max_score):
        super().__init__(title, max_score)


    def display_info(self):
        return f"Exam: {self.title}, Max Score: {self.max_score}."


    def grade_massage(self,score):
        limitation = self.max_score * 0.55
        if score >= limitation:
            return "Passed exam"
        else:
            return "Failed exam"