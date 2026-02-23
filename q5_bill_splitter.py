try:
    subtotal = float(input("Enter total bill: "))
    people   = int(input("Number of people: "))
    tax_pct  = float(input("Tax percentage: "))
    tip_pct  = float(input("Tip percentage: "))

    tax_amount  = subtotal * (tax_pct / 100)
    after_tax   = subtotal + tax_amount
    tip_amount  = after_tax * (tip_pct / 100)
    total       = after_tax + tip_amount
    per_person  = total / people

    print("\n=== BILL BREAKDOWN ===")
    print(f"Subtotal    : Rs.{subtotal:.2f}")
    print(f"Tax ({tax_pct}%) : Rs.{tax_amount:.2f}")
    print(f"After tax   : Rs.{after_tax:.2f}")
    print(f"Tip ({tip_pct}%) : Rs.{tip_amount:.2f}")
    print(f"Total       : Rs.{total:.2f}")
    print(f"Per person  : Rs.{per_person:.2f}")

except ValueError:
    print("Invalid input.")
