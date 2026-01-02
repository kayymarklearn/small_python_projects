from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz1 = QuizBrain(question_bank)


while quiz1.still_has_question():
    quiz1.next_question() 
    print("")