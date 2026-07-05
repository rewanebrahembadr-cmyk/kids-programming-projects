# Quiz Game Project
# This project helps beginners practice lists, loops, conditions, and score tracking.

questions = [
    {
        "question": "What is the capital of Egypt?",
        "answer": "cairo"
    },
    {
        "question": "Which programming language are we learning?",
        "answer": "python"
    },
    {
        "question": "What is 5 + 3?",
        "answer": "8"
    },
    {
        "question": "Which keyword is used for conditions in Python?",
        "answer": "if"
    }
]

score = 0

print("Welcome to the Quiz Game!")
print("Answer the following questions:")

for item in questions:
    user_answer = input(item["question"] + " ").lower()

    if user_answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer.")
        print("The correct answer is:", item["answer"])

print("Quiz finished!")
print("Your score is:", score, "out of", len(questions))
