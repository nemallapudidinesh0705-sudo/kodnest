def calculate_grade(marks: float) -> str:
    """Assigns a letter grade and remarks based on numerical marks (0-100)."""
    if marks < 0 or marks > 100:
        return "Invalid Marks! (Marks must be between 0 and 100)"
    elif marks >= 90:
        return "Grade: A+ (Outstanding)"
    elif marks >= 80:
        return "Grade: A (Excellent)"
    elif marks >= 70:
        return "Grade: B (Good)"
    elif marks >= 60:
        return "Grade: C (Average)"
    elif marks >= 50:
        return "Grade: D (Pass)"
    else:
        return "Grade: F (Fail)"


def main() -> None:
    print("================ GRADE CALCULATOR ================")
    try:
        user_input = input("Enter student marks (0 - 100): ")
        marks = float(user_input)
        result = calculate_grade(marks)
        print("-" * 35)
        print(f"Marks Entered: {marks}")
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter a valid numerical value.")


if __name__ == "__main__":
    # Test cases demonstrating the grading logic
    print("--- Automated Test Cases ---")
    test_scores = [95, 83, 74, 62, 51, 38, 105, -5]
    for score in test_scores:
        print(f"Marks: {score:<4} -> {calculate_grade(score)}")
    print("----------------------------\n")
    
    # Run interactive prompt
    # main()
