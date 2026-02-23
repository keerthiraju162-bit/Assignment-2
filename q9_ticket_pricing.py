# ============================================================
# Question 9: Ticket Pricing System
# Difficulty: Medium | Points: 4
# Description: Movie ticket pricing with age-based and day-based rules
# ============================================================

print("=== MOVIE TICKET PRICING SYSTEM ===\n")

try:
    # ── User Inputs ──────────────────────────────────────────
    age            = int(input("Enter age: "))
    day_of_week    = input("Enter day (e.g. Monday): ").strip().capitalize()
    num_tickets    = int(input("Number of tickets: "))

    # Validate inputs
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if num_tickets <= 0:
        raise ValueError("Number of tickets must be at least 1.")

    # Valid days list for validation
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                  "Friday", "Saturday", "Sunday"]
    if day_of_week not in valid_days:
        raise ValueError(f"'{day_of_week}' is not a valid day of the week.")

    # ── Age-based Pricing ────────────────────────────────────
    if age < 3:
        base_price   = 0
        category     = "Child (Under 3)"
    elif age <= 12:
        base_price   = 150
        category     = "Child (3-12)"
    elif age <= 59:
        base_price   = 300
        category     = "Adult (13-59)"
    else:
        base_price   = 200
        category     = "Senior (60+)"

    # ── Day-based Discount ────────────────────────────────────
    weekend_days     = ["Friday", "Saturday", "Sunday"]
    if day_of_week in weekend_days:
        discount_pct = 20
    else:
        discount_pct = 0

    # ── Calculations ─────────────────────────────────────────
    discount_amount  = base_price * (discount_pct / 100)
    price_per_ticket = base_price - discount_amount
    total_amount     = price_per_ticket * num_tickets

    # ── Display ───────────────────────────────────────────────
    print("\n=== TICKET SUMMARY ===")
    print(f"Category        : {category}")
    print(f"Day             : {day_of_week}")
    print(f"Base Price      : ₹{base_price:.2f} per ticket")

    if discount_pct > 0:
        print(f"Weekend Discount: {discount_pct}% (₹{discount_amount:.2f} off per ticket)")
        print(f"Price After Disc: ₹{price_per_ticket:.2f} per ticket")
    else:
        print(f"Discount        : None (Weekday)")

    print(f"Tickets         : {num_tickets}")
    print(f"Total Amount    : ₹{total_amount:.2f}")

    if base_price == 0:
        print("🎉 FREE entry for children under 3!")

except ValueError as e:
    print(f"Error: {e}")
