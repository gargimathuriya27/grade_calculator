# Student Grade Calculator

A simple Python program that takes a student's name and marks as input, calculates their grade based on specific logic, and displays a formatted result with a feedback message.

## Grading Logic
- **A**: 90-100 (Excellent work!)
- **B**: 80-89 (Very Good! Keep it up!)
- **C**: 70-79 (Satisfactory)
- **D**: 60-69 (Needs Improvement)
- **F**: 0-59 (Better luck next time)

## Functions Used
- `grade_calculator(score)`: This function takes the numerical score as an argument and returns the corresponding grade letter and feedback message using `if-elif-else` conditional logic.
- `main()`: Handles user inputs (name and marks), includes data validation to check if marks are between 0 and 100, and prints the output.

## How to Run
Run the script using Python:
```bash
python grade_calculator.py
