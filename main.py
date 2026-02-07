print("Simple Quiz Application")

score = 0

questions = [
    {
        "question": "1. What is the capital of Bangladesh?",
        "options": ["a) Chittagong", "b) Dhaka", "c) Khulna", "d) Rajshahi"],
        "answer": "b"
    },
    {
        "question": "2. Which language is used for web development?",
        "options": ["a) Python", "b) HTML", "c) Java", "d) All of the above"],
        "answer": "d"
    },
    {
        "question": "3. What does CPU stand for?",
        "options": ["a) Central Process Unit", "b) Central Processing Unit",
                    "c) Computer Personal Unit", "d) Control Processing Unit"],
        "answer": "b"
    },
    {
        "question": "4. Which symbol is used for comments in Python?",
        "options": ["a) //", "b) <!-- -->", "c) #", "d) /* */"],
        "answer": "c"
    },
    {
        "question": "5. Which data type is used to store True or False?",
        "options": ["a) int", "b) float", "c) bool", "d) str"],
        "answer": "c"
    }
]

for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)

    user_ans = input("Enter your answer (a/b/c/d): ").strip().lower()

    if user_ans == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n=== Quiz Finished ===")
print(f"Your Score: {score} out of {len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage}%")

if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: F")
