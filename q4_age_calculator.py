from datetime import date

try:
    birth_year  = int(input("Enter birth year: "))
    birth_month = int(input("Enter birth month: "))
    birth_day   = int(input("Enter birth day: "))

    birth_date = date(birth_year, birth_month, birth_day)
    today = date(2026, 2, 23)

    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    total_days = (today - birth_date).days

    print(f"\nCurrent Age    : {age} years")
    print(f"Age in Months  : {age * 12} months")
    print(f"Age in Days    : {total_days} days")
    print(f"Age in Hours   : {total_days * 24} hours")
    print(f"Age in Minutes : {total_days * 24 * 60} minutes")
    print(f"Years to 100   : {100 - age} years")

except ValueError:
    print("Invalid date entered.")
