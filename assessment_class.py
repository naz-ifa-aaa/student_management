class Assessment:
    def __init__(self, title , max_score):
        self.title = title
        self.max_score = max_score


    def calculate_percentage(self, score):
        if self.max_score== 0 :
            return 0.0
        return score/self.max_score


    def grade_massage(self, score):
        percentage = self.calculate_percentage(score)
        return f"Grade: you take {score}/{self.max_score}. Your percentage is {percentage:.1f}%."


    def display_info(self):
        print(f"{self.title}: _Max score{self.max_score}.")
