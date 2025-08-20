#  WORKFLOW
# Start
#    ↓
# Generate 5 random math questions
#    ↓
# Record Start Time
#    ↓
# [For each question]
#    ↓
# Show Question
#    ↓
# Get User Answer (no skipping allowed)
#    ↓
# Check Answer (Correct or Wrong)
#    ↓
# After all questions
#    ↓
# Record End Time
#    ↓
# Calculate Time Taken
#    ↓
# Show Score + Time Taken
#    ↓
# Exit


import random
import time

def math_challenge():
    # Generate 5 random math questions
    questions = []
    for _ in range(5):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(["+", "-", "*"])
        
        # Prepare the question text
        question_text = f"{num1} {operator} {num2}"
        # Evaluate the correct answer
        correct_answer = eval(question_text)
        
        questions.append((question_text, correct_answer))
    
    # Record Start Time
    print("\n⚡ Math Challenge Started! Answer as fast as you can ⚡")
    start_time = time.time()
    
    score = 0

    # [For each question]
    for i, (question, correct_answer) in enumerate(questions, start=1):
        while True:  # keep asking until user gives an input (no skipping)
            try:
                # Show Question
                user_input = int(input(f"Q{i}: {question} = "))
                break  # exit loop if input is valid
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        # Check Answer
        if user_input == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {correct_answer}")
    
    # Record End Time
    end_time = time.time()
    
    # Calculate Time Taken
    total_time = round(end_time - start_time, 2)
    
    # Show Score + Time Taken
    print("\n🏁 Challenge Completed!")
    print(f"Your Score: {score}/5")
    print(f"Time Taken: {total_time} seconds")

# Run the game
if __name__ == "__main__":
    math_challenge()
