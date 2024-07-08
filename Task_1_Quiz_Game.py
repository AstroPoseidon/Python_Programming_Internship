quiz = [
    {
        "question": "Q1) Who is the current Prime Minister of India?",
        "options": ["A. Narendra Modi", "B. Rahul Gandhi", "C. Mamta Banerjee", "D. Arvind Kejriwal"],
        "answer": "A",
        "explain": "The current Prime Minister of India is Narendra Modi, who got re-elected for a third term in 2024."
    },
    {
        "question": "Q2) Which country recently became the newest member of the European Union?",
        "options": ["A. Ukraine", "B. Serbia", "C. Albania", "D. North Macedonia"],
        "answer": "D",
        "explain": "North Macedonia became the newest member of the European Union, joining on January 1, 2024."
    },
    {
        "question": "Q3) Which country will host the 2024 Summer Olympics?",
        "options": ["A. Japan", "B. France", "C. United States", "D. Brazil"],
        "answer": "B",
        "explain": "The 2024 Summer Olympics will be held in Paris, France."
    },
    {
        "question": "Q4) Which tech company recently acquired the game development studio Activision Blizzard?",
        "options": ["A. Sony", "B. Microsoft", "C. Google", "D. Amazon"],
        "answer": "B",
        "explain": "Microsoft acquired Activision Blizzard in a deal announced in January 2022."
    },
    {
        "question": "Q5) Which country recently became the first to implement a nationwide ban on single-use plastics?",
        "options": ["A. Canada", "B. India", "C. France", "D. New Zealand"],
        "answer": "B",
        "explain": "India became the first country to implement a nationwide ban on single-use plastics on July 1, 2022, in an effort to reduce plastic pollution."
    }
]

def rules():
    print("\nWelcome to the Quiz Game!\n")
    print("Here are the rules for this game:")
    print("1. The quiz contains 5 multiple choice questions.")
    print("2. Each question has 4 options, and only one of them is correct.")
    print("3. Each question carries one point.")
    print("4. There is no negative marking for wrong answers.")
    print("\nEnjoy the game!\n")

def run_quiz(quiz):
    score = 0
    total_questions = len(quiz)
    
    for question in quiz:
        display_question(question)
        user_answer = get_user_answer()
        
        if check_answer(question, user_answer):
            score += 1
        print()

    print(f"\nQuiz completed! Your final score is {score}/{total_questions}.\n")
    
    if total_questions > 0:
        percentage = (score * 100) // total_questions
        print(f"{percentage}% of answers are correct.")
    else:
        print("No questions found.")
    
    print("\nThank you for playing!")

def get_user_answer():
    valid_answers = ['A', 'B', 'C', 'D']
    while True:
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        if user_answer in valid_answers:
            return user_answer
        else:
            print("Invalid input. Please enter A, B, C, or D.")

def display_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)

def check_answer(question_data, user_answer):
    correct_answer = question_data["answer"]
    
    if user_answer == correct_answer:
        print("\nCorrect! You get 1 point!")
        return True
    else:
        print(f"\nIncorrect. The correct answer is {correct_answer}.")
        print(f"\nExplanation:\n{question_data['explain']}")
        return False

def main():
    rules()
    run_quiz(quiz)

if __name__ == "__main__":
    main()