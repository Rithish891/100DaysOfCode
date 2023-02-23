class QuizBrain:
    def __init__(self, ques_list):
        self.ques_num = 0
        self.ques_list = ques_list
        self.score = 0

    def ques_left(self):
        if len(self.ques_list) > self.ques_num:
            return True
        else:
            return False

    def next_ques(self):
        cur_ques = self.ques_list[self.ques_num]
        self.ques_num += 1
        self.check_answer(input(f"{self.ques_num}: {cur_ques.text} (True/False)?..."), cur_ques.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Your answer is correct!")
            self.score += 1
        else:
            print("Answer is wrong")
            print(f"Correct answer is: {correct_answer}")
        print(f"Your score is {self.score}\n")
