import question_model
import data
from quiz_brain import QuizBrain

question_bank = []

for i in data.question_data:
    question_bank.append(question_model.Question(i["text"], i["answer"]))

quiz = QuizBrain(question_bank)

while quiz.ques_left():
    quiz.next_ques()

print(f"Hurry! You completed the quiz, your score is {quiz.score}/{quiz.ques_num}")