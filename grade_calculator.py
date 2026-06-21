def grade_calculator(score):
    if score >= 90:
        return 'A' , "Excellent work!"
    elif score >= 80:
        return 'B' , "Good job!"
    elif score >= 70:
        return 'C' , "Satisfactory"
    elif score >= 60:
        return 'D'  , "Needs Improvement"
    else:
        return 'F'  , "Better luck next time"
    

name = input("Enter Student name: ")

while True:
    score = int(input("Enter Student score (0-100): "))

    if 0 <= score <= 100:
        break
    else:
        print("Invalid score! Please enter a number between 0 and 100.")



grade, feedback = grade_calculator(score)

print("\nStudent Name:", name)
print("Score:", score)
print("Grade:", grade)
print("Feedback:", feedback)