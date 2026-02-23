# ============================================================
# Question 4: Age Calculator
# Difficulty: Medium | Points: 4
# Description: Calculates age and related time measurements
# Bonus: Uses exact birth date for precise calculation
# ============================================================

# Using datetime for the bonus precise calculation
from datetime import date

# ── BONUS: Exact birth date input ──────────────────────────
print("=== AGE CALCULATOR ===")
print("(Bonus: Enter exact birth date for precise calculation)\n")

try:
    birth_day   = int(input("Enter birth day   (DD): "))
    birth_month = int(input("Enter birth month (MM): "))
    birth_year  = int(input("Enter birth year  (YYYY): "))

    # Validate the date by creating a date object (raises ValueError if invalid)
    birth_date  = date(birth_year, birth_month, birth_day)
    today       = date(2026, 2, 23)  # Current date: 2026-02-23

    # ── Precise age calculation ──────────────────────────────
    # Check if birthday has occurred this year
    had_birthday_this_year = (today.month, today.day) >= (birth_date.month, birth_date.day)

    precise_age_years  = today.year - birth_year - (0 if had_birthday_this_year else 1)

    # Total number of days lived
    total_days_lived   = (today - birth_date).days

    # Derived calculations (approximate)
    age_in_months      = precise_age_years * 12 + (today.month - birth_date.month if had_birthday_this_year
                         else today.month - birth_date.month + 12)
    age_in_days        = total_days_lived
    age_in_hours       = total_days_lived * 24
    age_in_minutes     = age_in_hours * 60
    years_until_100    = 100 - precise_age_years

    # ── Display results ──────────────────────────────────────
    print(f"\n=== YOUR AGE BREAKDOWN ===")
    print(f"Date of Birth   : {birth_date.strftime('%d %B %Y')}")
    print(f"Today's Date    : {today.strftime('%d %B %Y')}")
    print(f"Current Age     : {precise_age_years} years")
    print(f"Age in Months   : ~{age_in_months} months")
    print(f"Age in Days     : ~{age_in_days} days")
    print(f"Age in Hours    : ~{age_in_hours:,} hours")
    print(f"Age in Minutes  : ~{age_in_minutes:,} minutes")
    print(f"Years to 100    : {years_until_100} years")

    if years_until_100 < 0:
        print("🎉 Congratulations! You have already crossed 100 years!")

except ValueError as e:
    # Handle both invalid date and non-integer input
    print(f"Error: Invalid input — {e}. Please enter valid numbers for the date.")
