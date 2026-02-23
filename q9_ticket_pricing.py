try:
    age     = int(input("Enter age: "))
    day     = input("Enter day (e.g. Monday): ").strip().capitalize()
    tickets = int(input("Number of tickets: "))

    if age < 3:
        base_price = 0
        category   = "Free (Under 3)"
    elif age <= 12:
        base_price = 150
        category   = "Child"
    elif age <= 59:
        base_price = 300
        category   = "Adult"
    else:
        base_price = 200
        category   = "Senior"

    weekend = ["Friday", "Saturday", "Sunday"]
    discount = 0.20 if day in weekend else 0

    discounted_price = base_price - (base_price * discount)
    total = discounted_price * tickets

    print(f"\nCategory      : {category}")
    print(f"Base Price    : Rs.{base_price}")
    print(f"Discount      : {int(discount * 100)}%")
    print(f"Price/Ticket  : Rs.{discounted_price:.2f}")
    print(f"Total Amount  : Rs.{total:.2f}")

except ValueError:
    print("Invalid input.")
