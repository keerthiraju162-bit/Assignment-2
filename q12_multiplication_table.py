# ============================================================
# Question 12: Multiplication Table Generator
# Difficulty: Easy-Medium | Points: 4
# Description: Generates a multiplication table for a given number
# Bonus: Full 1-10 x 1-10 grid
# ============================================================

print("=== MULTIPLICATION TABLE GENERATOR ===\n")

try:
    table_number = int(input("Enter number: "))
    table_range  = int(input("Enter range (end): "))

    if table_range <= 0:
        raise ValueError("Range must be a positive integer.")

    # ── Single table ─────────────────────────────────────────
    print(f"\nMultiplication Table of {table_number}")
    print("-" * 25)
    for multiplier in range(1, table_range + 1):
        product = table_number * multiplier
        print(f"{table_number} x {multiplier:>2} = {product:>5}")

    # ── BONUS: Full 1-10 x 1-10 grid ─────────────────────────
    print("\n\n=== BONUS: Full Multiplication Grid (1–10) ===")

    # Grid size
    GRID_SIZE = 10
    CELL_W    = 5  # Width of each cell for alignment

    # Header row
    print(" " * CELL_W, end="")
    for col in range(1, GRID_SIZE + 1):
        print(f"{col:>{CELL_W}}", end="")
    print()
    print("-" * (CELL_W * (GRID_SIZE + 1)))

    # Data rows
    for row in range(1, GRID_SIZE + 1):
        # Row label
        print(f"{row:>{CELL_W}}", end="")
        for col in range(1, GRID_SIZE + 1):
            print(f"{row * col:>{CELL_W}}", end="")
        print()   # Newline after each row

except ValueError as e:
    print(f"Error: {e}")
