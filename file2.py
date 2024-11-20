import json
import os

# Function to load quiz data from file
def load_quiz_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to parse the quiz data file!")
        return []

# Function to run the quiz
def run_quiz(quiz_data):
    if not quiz_data:
        print("No quiz data available. Exiting...")
        return

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

# Main script
if __name__ == "__main__":
    # Path to the JSON file inside the 'project' folder
    folder_path = "project1"
    file_name = "quiz_data.json"
    file_path = os.path.join(folder_path, file_name)  # Construct full path

    # Load the quiz data and run the quiz
    quiz_data = load_quiz_data(file_path)
    run_quiz(quiz_data)
