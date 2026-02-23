try:
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year.")
        if year % 400 == 0:
            print(f"Reason: {year} is divisible by 400.")
        else:
            print(f"Reason: {year} is divisible by 4 but not by 100.")
    else:
        print(f"{year} is NOT a Leap Year.")
        if year % 4 != 0:
            print(f"Reason: {year} is not divisible by 4.")
        else:
            print(f"Reason: {year} is divisible by 100 but not by 400.")

except ValueError:
    print("Invalid input.")
