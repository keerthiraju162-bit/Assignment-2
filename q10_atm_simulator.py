# ============================================================
# Question 10: Simple ATM Simulator
# Difficulty: Medium-Hard | Points: 7
# Description: ATM with balance check, deposit, withdraw
# Bonus: Transaction history included
# ============================================================

# ── Constants ─────────────────────────────────────────────────
INITIAL_BALANCE  = 10000.0   # Starting balance in ₹
MINIMUM_BALANCE  = 500.0     # Minimum balance that must remain

# ── State ─────────────────────────────────────────────────────
current_balance  = INITIAL_BALANCE
transaction_history = []     # BONUS: list of (type, amount, balance_after)

def display_balance():
    """Prints the current account balance."""
    print(f"\n💳 Current Balance: ₹{current_balance:,.2f}")

def deposit(amount):
    """Adds amount to balance. Returns True on success, False otherwise."""
    global current_balance
    if amount <= 0:
        print("Error: Deposit amount must be greater than zero.")
        return False
    current_balance += amount
    transaction_history.append(("DEPOSIT", amount, current_balance))
    print(f"\n✅ Deposit of ₹{amount:,.2f} successful!")
    print(f"   New Balance: ₹{current_balance:,.2f}")
    return True

def withdraw(amount):
    """Deducts amount from balance, ensuring minimum balance rule."""
    global current_balance
    if amount <= 0:
        print("Error: Withdrawal amount must be greater than zero.")
        return False
    # Check if withdrawal would breach minimum balance
    if current_balance - amount < MINIMUM_BALANCE:
        shortfall = amount - (current_balance - MINIMUM_BALANCE)
        print(f"\n❌ Insufficient funds!")
        print(f"   Available for withdrawal: ₹{current_balance - MINIMUM_BALANCE:,.2f}")
        print(f"   (₹{MINIMUM_BALANCE:,.2f} minimum balance must be maintained)")
        return False
    current_balance -= amount
    transaction_history.append(("WITHDRAWAL", amount, current_balance))
    print(f"\n✅ Withdrawal of ₹{amount:,.2f} successful!")
    print(f"   New Balance: ₹{current_balance:,.2f}")
    return True

def show_transaction_history():
    """BONUS: Displays all past transactions."""
    if not transaction_history:
        print("\nNo transactions yet.")
        return
    print("\n=== TRANSACTION HISTORY ===")
    print(f"{'#':<4} {'Type':<12} {'Amount':>12} {'Balance After':>14}")
    print("-" * 45)
    for idx, (t_type, t_amount, t_balance) in enumerate(transaction_history, start=1):
        print(f"{idx:<4} {t_type:<12} ₹{t_amount:>10,.2f} ₹{t_balance:>12,.2f}")

# ── Main ATM Loop ─────────────────────────────────────────────
print("=" * 30)
print("       🏧 ATM SIMULATOR")
print("=" * 30)
print(f"Welcome! Initial Balance: ₹{INITIAL_BALANCE:,.2f}")

while True:
    # Display menu
    print("\n-------- MENU --------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    print("----------------------")

    try:
        menu_choice = int(input("Enter choice (1-5): "))

        if menu_choice == 1:
            display_balance()

        elif menu_choice == 2:
            try:
                deposit_amount = float(input("Enter amount to deposit: ₹"))
                deposit(deposit_amount)
            except ValueError:
                print("Error: Please enter a valid amount.")

        elif menu_choice == 3:
            try:
                withdraw_amount = float(input("Enter amount to withdraw: ₹"))
                withdraw(withdraw_amount)
            except ValueError:
                print("Error: Please enter a valid amount.")

        elif menu_choice == 4:
            show_transaction_history()

        elif menu_choice == 5:
            print(f"\nThank you for using ATM Simulator!")
            print(f"Final Balance: ₹{current_balance:,.2f}")
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    except ValueError:
        print("Error: Please enter a valid menu option.")
