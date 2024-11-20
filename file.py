# Quiz data stored in program memory
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. J.K. Rowling", "D. Mark Twain"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["A. 50", "B. 100", "C. 150", "D. 200"],
        "answer": "B"
    },
]

# Function to run the quiz
def run_quiz():
    score = 0
    print("\nWelcome to the Quiz App!\n")
    
    for idx, item in enumerate(quiz_data, start=1):
        print(f"Question {idx}: {item['question']}")
        for option in item['options']:
            print(option)
        
        # Get the user's answer
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        
        # Check if the answer is correct
        if user_answer == item['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {item['answer']}.\n")
    
    print(f"You completed the quiz! Your final score is: {score}/{len(quiz_data)}")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
