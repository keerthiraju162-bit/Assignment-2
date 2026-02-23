# ============================================================
# Question 5: Bill Splitter
# Difficulty: Medium | Points: 4
# Description: Splits a restaurant bill among people
#              including tax and tip calculations
# ============================================================

print("=== RESTAURANT BILL SPLITTER ===\n")

try:
    # Collect all inputs from the user
    subtotal        = float(input("Enter total bill: ₹"))
    num_people      = int(input("Number of people: "))
    tax_percentage  = float(input("Tax percentage: "))
    tip_percentage  = float(input("Tip percentage: "))

    # Validate inputs — amounts and people must be positive
    if subtotal <= 0:
        raise ValueError("Bill amount must be greater than zero.")
    if num_people <= 0:
        raise ValueError("Number of people must be at least 1.")
    if tax_percentage < 0 or tip_percentage < 0:
        raise ValueError("Tax and tip percentages cannot be negative.")

    # ── Calculations ─────────────────────────────────────────
    tax_amount      = subtotal * (tax_percentage / 100)
    bill_after_tax  = subtotal + tax_amount
    tip_amount      = bill_after_tax * (tip_percentage / 100)
    total_bill      = bill_after_tax + tip_amount
    amount_per_person = total_bill / num_people

    # ── Display breakdown ─────────────────────────────────────
    print("\n=== BILL BREAKDOWN ===")
    print(f"Subtotal         : ₹{subtotal:.2f}")
    print(f"Tax ({tax_percentage}%)       : ₹{tax_amount:.2f}")
    print(f"After tax        : ₹{bill_after_tax:.2f}")
    print(f"Tip ({tip_percentage}%)       : ₹{tip_amount:.2f}")
    print(f"Total            : ₹{total_bill:.2f}")
    print(f"Per person       : ₹{amount_per_person:.2f}")

except ValueError as e:
    print(f"Error: {e}")
