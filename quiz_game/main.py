from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    questions = Question(question["text"], question["answer"])
    question_bank.append(questions)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You Completed the quiz.")
print(f"Your final score is {quiz.score}/{len(question_bank)}")
