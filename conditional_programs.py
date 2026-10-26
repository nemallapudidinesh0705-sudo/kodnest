"""
Collection of 12 Python Programs Demonstrating Conditional Statements:
- Part 1: Simple 'if' statements (Programs 1 - 4)
- Part 2: 'if-else' statements (Programs 5 - 8)
- Part 3: 'if-elif-else' statements (Programs 9 - 12)
"""

# ==============================================================================
# PART 1: SIMPLE 'if' STATEMENTS (Programs 1 - 4)
# ==============================================================================

def program_1_check_positive(num: float) -> None:
    """Program 1: Check if a number is positive."""
    print(f"--- Program 1: Check Positive ({num}) ---")
    if num > 0:
        print(f"{num} is a positive number.")


def program_2_voting_eligibility(age: int) -> None:
    """Program 2: Check if eligible to vote."""
    print(f"--- Program 2: Voting Eligibility (Age: {age}) ---")
    if age >= 18:
        print("You are eligible to vote!")


def program_3_discount_eligibility(amount: float) -> None:
    """Program 3: Apply discount if purchase exceeds 1000."""
    print(f"--- Program 3: Discount Check (Amount: {amount}) ---")
    final_amount = amount
    if amount > 1000:
        discount = amount * 0.10
        final_amount = amount - discount
        print(f"10% discount applied: -{discount:.2f}")
    print(f"Final Payable Amount: {final_amount:.2f}")


def program_4_check_pass(score: int) -> None:
    """Program 4: Check if student has passed."""
    print(f"--- Program 4: Pass Check (Score: {score}) ---")
    if score >= 40:
        print("Congratulations! You passed the examination.")


# ==============================================================================
# PART 2: 'if-else' STATEMENTS (Programs 5 - 8)
# ==============================================================================

def program_5_even_or_odd(num: int) -> None:
    """Program 5: Determine if a number is even or odd."""
    print(f"--- Program 5: Even or Odd ({num}) ---")
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")


def program_6_pass_or_fail(score: int) -> None:
    """Program 6: Check pass or fail status."""
    print(f"--- Program 6: Pass or Fail (Score: {score}) ---")
    if score >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")


def program_7_max_of_two(a: float, b: float) -> None:
    """Program 7: Find the larger of two numbers."""
    print(f"--- Program 7: Maximum of Two ({a}, {b}) ---")
    if a > b:
        print(f"{a} is greater than {b}.")
    else:
        print(f"{b} is greater than or equal to {a}.")


def program_8_leap_year(year: int) -> None:
    """Program 8: Check if a year is a leap year."""
    print(f"--- Program 8: Leap Year Check ({year}) ---")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year.")
    else:
        print(f"{year} is NOT a Leap Year.")


# ==============================================================================
# PART 3: 'if-elif-else' STATEMENTS (Programs 9 - 12)
# ==============================================================================

def program_9_number_sign(num: float) -> None:
    """Program 9: Classify number as Positive, Negative, or Zero."""
    print(f"--- Program 9: Number Sign ({num}) ---")
    if num > 0:
        print(f"{num} is Positive.")
    elif num < 0:
        print(f"{num} is Negative.")
    else:
        print("The number is Zero.")


def program_10_grade_evaluation(score: int) -> None:
    """Program 10: Evaluate student grade based on score."""
    print(f"--- Program 10: Grade Evaluation (Score: {score}) ---")
    if score >= 90:
        grade = "A (Outstanding)"
    elif score >= 75:
        grade = "B (Very Good)"
    elif score >= 60:
        grade = "C (Good)"
    elif score >= 40:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"
    print(f"Score: {score} -> Grade: {grade}")


def program_11_max_of_three(a: float, b: float, c: float) -> None:
    """Program 11: Find the largest among three numbers."""
    print(f"--- Program 11: Maximum of Three ({a}, {b}, {c}) ---")
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    print(f"The largest number among {a}, {b}, and {c} is {largest}.")


def program_12_traffic_light(signal: str) -> None:
    """Program 12: Traffic light instruction simulator."""
    print(f"--- Program 12: Traffic Light ('{signal}') ---")
    sig = signal.strip().lower()
    if sig == "red":
        print("Action: STOP!")
    elif sig == "yellow":
        print("Action: SLOW DOWN / PREPARE TO STOP.")
    elif sig == "green":
        print("Action: GO!")
    else:
        print("Action: Invalid signal color.")


# ==============================================================================
# MAIN EXECUTION: Run all 12 sample programs
# ==============================================================================
if __name__ == "__main__":
    print("================ RUNNING 12 CONDITIONAL PROGRAMS ================\n")

    # Part 1: if
    program_1_check_positive(15)
    program_2_voting_eligibility(19)
    program_3_discount_eligibility(1250.0)
    program_4_check_pass(55)

    print()
    # Part 2: if-else
    program_5_even_or_odd(7)
    program_6_pass_or_fail(42)
    program_7_max_of_two(18, 42)
    program_8_leap_year(2024)

    print()
    # Part 3: if-elif-else
    program_9_number_sign(-8.5)
    program_10_grade_evaluation(82)
    program_11_max_of_three(34, 89, 52)
    program_12_traffic_light("red")

    print("\n================ COMPLETED ALL DEMONSTRATIONS ================")
