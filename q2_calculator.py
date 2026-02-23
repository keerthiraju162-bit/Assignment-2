# ============================================================
# Question 2: Simple Calculator
# Difficulty: Easy | Points: 2
# Description: Takes two numbers and performs 6 operations
# ============================================================

try:
    # Get input from the user
    first_number  = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    # Display the number neatly (int if whole, float otherwise)
    def fmt(n):
        """Return int representation if number is whole, else float."""
        return int(n) if n == int(n) else n

    a = fmt(first_number)
    b = fmt(second_number)

    print("\nResults:")
    print(f"{a} + {b} = {fmt(first_number + second_number)}")
    print(f"{a} - {b} = {fmt(first_number - second_number)}")
    print(f"{a} * {b} = {fmt(first_number * second_number)}")

    # Handle division by zero
    if second_number == 0:
        print(f"{a} / {b} = Error (cannot divide by zero)")
        print(f"{a} % {b} = Error (cannot modulus by zero)")
    else:
        division_result = first_number / second_number
        modulus_result  = first_number % second_number
        print(f"{a} / {b} = {round(division_result, 2)}")
        print(f"{a} % {b} = {fmt(modulus_result)}")

    print(f"{a} ^ {b} = {fmt(first_number ** second_number)}")

except ValueError:
    # Handle non-numeric input
    print("Error: Please enter valid numbers.")
