class Student:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major ='BMI' or 'BMS'
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score

    def print_details(self):
        print(f"Name: {self.name}, Major: {self.major}, Code Portfolio Score: {self.code_portfolio_score}, "
              f"Group Project Score: {self.group_project_score}, Exam Score: {self.exam_score}")

# For Example:
if __name__ == "__main__":
    student1 = Student( name="Chen Jiangrun", major="BMI",code_portfolio_score=60, group_project_score=60, exam_score=60)
    student1.print_details()