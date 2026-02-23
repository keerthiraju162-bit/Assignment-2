# ============================================================
# Question 8: Leap Year Checker
# Difficulty: Medium | Points: 4
# Description: Checks if a year is a leap year using official rules
# ============================================================

print("=== LEAP YEAR CHECKER ===\n")

try:
    year = int(input("Enter a year: "))

    # Validate: years must be positive
    if year <= 0:
        raise ValueError("Year must be a positive integer.")

    # ── Leap Year Logic ──────────────────────────────────────
    # Rule: Divisible by 4 AND (NOT divisible by 100 OR divisible by 400)
    divisible_by_4   = (year % 4 == 0)
    divisible_by_100 = (year % 100 == 0)
    divisible_by_400 = (year % 400 == 0)

    is_leap_year = divisible_by_4 and (not divisible_by_100 or divisible_by_400)

    # ── Display result with reason ────────────────────────────
    print(f"\nYear: {year}")

    if is_leap_year:
        print(f"Result : ✅ {year} IS a Leap Year")
        if divisible_by_400:
            reason = f"{year} is divisible by 400 → Leap Year."
        else:
            reason = f"{year} is divisible by 4 but NOT by 100 → Leap Year."
    else:
        print(f"Result : ❌ {year} is NOT a Leap Year")
        if not divisible_by_4:
            reason = f"{year} is not divisible by 4 → Not a Leap Year."
        else:
            # divisible by 4 AND by 100 but NOT by 400
            reason = f"{year} is divisible by 100 but NOT by 400 → Not a Leap Year."

    print(f"Reason : {reason}")

    # ── Show days in February for context ─────────────────────
    feb_days = 29 if is_leap_year else 28
    print(f"Days in February {year}: {feb_days}")

except ValueError as e:
    print(f"Error: {e}")
