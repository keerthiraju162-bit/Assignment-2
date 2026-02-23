# ============================================================
# Question 15: Prime Number Checker
# Difficulty: Medium-Hard | Points: 7
# Description:
#   Part 1: Check if a single number is prime
#   Part 2: Find all primes in a given range
# ============================================================

def is_prime(number):
    """
    Returns True if number is prime, False otherwise.
    Handles edge cases: negatives, 0, 1, and 2.
    Uses trial division up to the square root for efficiency.
    """
    if number < 2:
        return False  # 0, 1, and negatives are not prime
    if number == 2:
        return True   # 2 is the only even prime
    if number % 2 == 0:
        return False  # All other even numbers are not prime

    # Check odd divisors from 3 up to sqrt(number)
    # (no need to check beyond sqrt — factors come in pairs)
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2  # Skip even numbers
    return True

# ── Part 1: Single number check ──────────────────────────────
print("=== PRIME NUMBER CHECKER ===\n")
print("--- Part 1: Single Number ---")

try:
    single_number = int(input("Enter a number: "))

    if single_number < 0:
        print(f"{single_number} is negative — prime numbers must be positive integers > 1.")
    elif single_number == 0:
        print("0 is NOT a prime number (primes must be greater than 1).")
    elif single_number == 1:
        print("1 is NOT a prime number (by mathematical convention).")
    elif single_number == 2:
        print("2 is a PRIME number (the only even prime).")
    elif is_prime(single_number):
        print(f"\n{single_number} is a PRIME number ✅")
        print(f"(It has no divisors other than 1 and itself)")
    else:
        # Find and display the factors to explain why it's not prime
        factors = [i for i in range(2, single_number) if single_number % i == 0]
        print(f"\n{single_number} is NOT a prime number ❌")
        print(f"Divisors: 1, {', '.join(map(str, factors))}, {single_number}")

except ValueError:
    print("Error: Please enter a valid integer.")
    exit()

# ── Part 2: Prime numbers in a range ─────────────────────────
print("\n--- Part 2: Primes in a Range ---")

try:
    start_range = int(input("Enter start of range: "))
    end_range   = int(input("Enter end of range: "))

    if start_range > end_range:
        start_range, end_range = end_range, start_range  # Swap if reversed
        print(f"(Range reversed: {start_range} to {end_range})")

    # Find all prime numbers in the range
    primes_in_range = [num for num in range(start_range, end_range + 1) if is_prime(num)]

    if primes_in_range:
        print(f"\nPrime numbers between {start_range} and {end_range}:")
        print(", ".join(map(str, primes_in_range)))
        print(f"Total primes found: {len(primes_in_range)}")
    else:
        print(f"No prime numbers found between {start_range} and {end_range}.")

except ValueError:
    print("Error: Please enter valid integers for the range.")
