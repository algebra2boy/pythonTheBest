from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q["question"], q["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.has_next_question():
    quiz.next_question()

print("You have completed the open trivial challenge")
print(f"Your final score is {quiz.score}/{len(question_bank)}")