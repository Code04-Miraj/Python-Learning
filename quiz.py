# ======================================
# QUIZ GAME WORKFLOW
# ======================================
# Start
#    ↓
# Load Questions
#    ↓
# Set score = 0
#    ↓
# [For each question]
#    ↓
# Show Question + Options
#    ↓
# Get User Answer
#    ↓
# Correct? ── Yes → +1 Score
#    │
#    └─ No → Show Correct Answer
#    ↓
# After all questions
#    ↓
# Show Final Score
#    ↓
# Play again? → Yes → Restart
#              → No → Exit
# ======================================


def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "Which language is known as the language of the web?",
            "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
            "answer": "B"
        },
        {
            "question": "Who developed Python?",
            "options": ["A. James Gosling", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
            "answer": "C"
        }
    ]

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong! The correct answer was:", q["answer"])

    print(f"\nYour final score is {score}/{len(questions)}")


if __name__ == "__main__":
    while True:
        quiz_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye 👋")
            break
