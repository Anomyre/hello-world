
from Question import Question

question_prompts = [
    "What's the capital of Brazil?\n(a) Rio de Janeiro\n(b) Brazilia\n(c) Sao Paolo\n\n",
    "What's the capital of Australia?\n(a) Canberra\n(b) Sydney\n(c) Perth\n\n",
    "What's the capital of Pakistan?\n(a) Lahore\n(b) Islamabad\n(c) Karachi\n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct.")


run_test(questions)
