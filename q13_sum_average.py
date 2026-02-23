# ============================================================
# Question 13: Sum and Average Calculator
# Difficulty: Easy | Points: 4
# Description: Takes N numbers and calculates sum, average, max, min
# Bonus: Also calculates median and mode
# ============================================================

print("=== SUM AND AVERAGE CALCULATOR ===\n")

try:
    count = int(input("How many numbers? "))

    if count <= 0:
        raise ValueError("Count must be a positive integer.")

    # Collect numbers from the user using a loop
    numbers_list = []
    for i in range(1, count + 1):
        while True:
            try:
                number = float(input(f"Enter number {i}: "))
                numbers_list.append(number)
                break
            except ValueError:
                print("  Invalid input. Please enter a valid number.")

    # ── Core Calculations ─────────────────────────────────────
    total_sum   = sum(numbers_list)
    average     = total_sum / count
    maximum     = max(numbers_list)
    minimum     = min(numbers_list)

    # ── BONUS: Median and Mode ────────────────────────────────
    sorted_numbers = sorted(numbers_list)

    # Median: middle value (or average of two middles for even count)
    midpoint = count // 2
    if count % 2 == 1:
        median = sorted_numbers[midpoint]
    else:
        median = (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2

    # Mode: most frequently occurring number
    frequency = {}
    for num in numbers_list:
        frequency[num] = frequency.get(num, 0) + 1
    max_frequency = max(frequency.values())
    mode_values   = [k for k, v in frequency.items() if v == max_frequency]

    # ── Display Results ───────────────────────────────────────
    print("\n=== RESULTS ===")
    print(f"Numbers  : {numbers_list}")
    print(f"Sum      : {total_sum}")
    print(f"Average  : {average:.2f}")
    print(f"Maximum  : {maximum}")
    print(f"Minimum  : {minimum}")
    print(f"\n--- BONUS ---")
    print(f"Median   : {median}")
    if max_frequency == 1:
        print("Mode     : No mode (all values occur once)")
    else:
        print(f"Mode     : {mode_values} (appears {max_frequency} times)")

except ValueError as e:
    print(f"Error: {e}")
