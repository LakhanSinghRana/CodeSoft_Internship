def display_question(question, options):
    print(question)
    for index, option in enumerate(options, 1):
        print(f"{index}. {option}")

def get_user_answer():
    while True:
        user_input = input("Enter your choice (1, 2, 3, ...): ")
        if user_input.isdigit() and 1 <= int(user_input) <= 4:
            return int(user_input)
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

def check_answer(answer, user_choice):
    return answer == user_choice

def display_result(result):
    if result:
        print("Correct!")
    else:
        print("Wrong!")

def quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "answer": 1
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Jupiter", "Venus", "Saturn"],
            "answer": 1
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Stephen King", "Harper Lee", "J.K. Rowling", "George Orwell"],
            "answer": 2
        }
    ]

    score = 0
    for question in questions:
        display_question(question["question"], question["options"])
        user_choice = get_user_answer()
        result = check_answer(question["answer"], user_choice)
        display_result(result)
        if result:
            score += 1

    print(f"You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    quiz()