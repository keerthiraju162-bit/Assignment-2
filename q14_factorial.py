# ============================================================
# Question 14: Factorial Calculator
# Difficulty: Medium | Points: 4
# Description: Calculates factorial with step-by-step display
# ============================================================

print("=== FACTORIAL CALCULATOR ===\n")

try:
    number = int(input("Enter a number: "))

    # ── Edge cases ────────────────────────────────────────────
    if number < 0:
        print(f"Error: Factorial is not defined for negative numbers ({number}).")

    elif number == 0:
        # By mathematical definition, 0! = 1
        print(f"\n0! = 1")
        print("(By definition, the factorial of 0 is 1)")

    elif number == 1:
        print(f"\n1! = 1")

    else:
        # ── Loop-based calculation ────────────────────────────
        factorial_result = 1
        step_parts = []   # Stores each factor for step-by-step display

        for factor in range(number, 0, -1):
            factorial_result *= factor
            step_parts.append(str(factor))

        # Build the step-by-step string: "5 × 4 × 3 × 2 × 1"
        step_expression = " × ".join(step_parts)

        # Display the result
        print(f"\n{number}! = {step_expression} = {factorial_result}")

except ValueError:
    print("Error: Please enter a valid integer.")
