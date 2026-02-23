# ============================================================
# Question 18: Calculator Functions
# Difficulty: Medium | Points: 7
# Description: Calculator built with individual math functions
# Bonus: square root and percentage functions added
# ============================================================

import math  # Used for square root

# ── Individual operation functions ───────────────────────────

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns a minus b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns a divided by b. Handles division by zero."""
    if b == 0:
        return None  # Signal an error without raising
    return a / b

def modulus(a, b):
    """Returns the remainder of a divided by b."""
    if b == 0:
        return None
    return a % b

def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b

def square_root(a):
    """BONUS: Returns the square root of a. Handles negatives."""
    if a < 0:
        return None  # Square root of negative is undefined in real numbers
    return math.sqrt(a)

def percentage(a, b):
    """BONUS: Returns a% of b (i.e. what is a% of b)."""
    return (a / 100) * b

# ── Main calculator function ──────────────────────────────────

def calculator():
    """Displays a menu and calls the appropriate function based on user input."""
    print("=" * 35)
    print("        🧮 CALCULATOR")
    print("=" * 35)

    while True:
        # Display the full menu
        print("\nOperations:")
        print("1.  Addition        (a + b)")
        print("2.  Subtraction     (a - b)")
        print("3.  Multiplication  (a * b)")
        print("4.  Division        (a / b)")
        print("5.  Modulus         (a % b)")
        print("6.  Power           (a ^ b)")
        print("7.  Square Root     (√a)     [Bonus]")
        print("8.  Percentage      (a% of b)[Bonus]")
        print("9.  Exit")

        try:
            operation_choice = int(input("\nEnter choice (1-9): "))

            if operation_choice == 9:
                print("Goodbye! 👋")
                break

            # Operations 7 and 8 need only one / different input handling
            if operation_choice == 7:
                num_a = float(input("Enter number: "))
                result = square_root(num_a)
                if result is None:
                    print("Error: Cannot take square root of a negative number.")
                else:
                    print(f"\n√{num_a} = {result:.4f}")

            elif operation_choice == 8:
                num_a = float(input("Enter percentage value: "))
                num_b = float(input("Enter the number: "))
                result = percentage(num_a, num_b)
                print(f"\n{num_a}% of {num_b} = {result:.4f}")

            elif operation_choice in (1, 2, 3, 4, 5, 6):
                num_a = float(input("Enter first number (a): "))
                num_b = float(input("Enter second number (b): "))

                # Map choice to function and symbol
                operations_map = {
                    1: (add,      "+"),
                    2: (subtract, "-"),
                    3: (multiply, "*"),
                    4: (divide,   "/"),
                    5: (modulus,  "%"),
                    6: (power,    "^"),
                }
                func, symbol = operations_map[operation_choice]
                result = func(num_a, num_b)

                if result is None:
                    print("Error: Cannot divide or modulus by zero.")
                else:
                    print(f"\n{num_a} {symbol} {num_b} = {result}")

            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

        except ValueError:
            print("Error: Please enter valid numbers.")

# ── Entry point ───────────────────────────────────────────────
calculator()
