# ============================================================
# Question 11: Number Pattern Printer
# Difficulty: Medium | Points: 4
# Description: Prints 4 different number patterns based on user choice
# ============================================================

def print_pattern_1(height):
    """
    Pattern 1: Increasing number row
    1
    1 2
    1 2 3
    """
    print("\n--- Pattern 1 ---")
    for row in range(1, height + 1):
        # Each row prints numbers from 1 to current row number
        print(" ".join(str(num) for num in range(1, row + 1)))

def print_pattern_2(height):
    """
    Pattern 2: Row number repeated per row
    1
    2 2
    3 3 3
    """
    print("\n--- Pattern 2 ---")
    for row in range(1, height + 1):
        # Each row prints the row number repeated row times
        print(" ".join(str(row) for _ in range(row)))

def print_pattern_3(height):
    """
    Pattern 3: Countdown rows (descending)
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1
    """
    print("\n--- Pattern 3 ---")
    for row in range(height, 0, -1):
        # Each row counts down from current row number to 1
        print(" ".join(str(num) for num in range(row, 0, -1)))

def print_pattern_4(height):
    """
    Pattern 4: Palindrome pyramid
    1
    121
    12321
    1234321
    """
    print("\n--- Pattern 4 ---")
    for row in range(1, height + 1):
        # Ascending part: 1 to row
        ascending  = "".join(str(num) for num in range(1, row + 1))
        # Descending part: (row-1) down to 1
        descending = "".join(str(num) for num in range(row - 1, 0, -1))
        print(ascending + descending)

# ── Main program ──────────────────────────────────────────────
print("=== NUMBER PATTERN PRINTER ===")
print("\nAvailable Patterns:")
print("1. Increasing number rows")
print("2. Row number repeated")
print("3. Countdown rows")
print("4. Palindrome pyramid")
print("5. Print ALL patterns")

try:
    pattern_choice = int(input("\nChoose pattern (1-5): "))
    pattern_height = int(input("Enter height (rows): "))

    if pattern_height <= 0:
        raise ValueError("Height must be a positive integer.")
    if pattern_choice not in range(1, 6):
        raise ValueError("Pattern choice must be between 1 and 5.")

    # Call the appropriate pattern function(s)
    if pattern_choice == 1:
        print_pattern_1(pattern_height)
    elif pattern_choice == 2:
        print_pattern_2(pattern_height)
    elif pattern_choice == 3:
        print_pattern_3(pattern_height)
    elif pattern_choice == 4:
        print_pattern_4(pattern_height)
    elif pattern_choice == 5:
        print_pattern_1(pattern_height)
        print_pattern_2(pattern_height)
        print_pattern_3(pattern_height)
        print_pattern_4(pattern_height)

except ValueError as e:
    print(f"Error: {e}")
