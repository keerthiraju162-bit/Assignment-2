balance = 10000.0

print("ATM SIMULATOR")

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            print(f"Balance: Rs.{balance:.2f}")

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Amount must be positive.")
            else:
                balance += amount
                print(f"Deposited Rs.{amount:.2f}. New balance: Rs.{balance:.2f}")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Amount must be positive.")
            elif balance - amount < 500:
                print(f"Cannot withdraw. Minimum balance of Rs.500 must remain.")
                print(f"Max you can withdraw: Rs.{balance - 500:.2f}")
            else:
                balance -= amount
                print(f"Withdrawn Rs.{amount:.2f}. New balance: Rs.{balance:.2f}")

        elif choice == 4:
            print("Thank you. Goodbye!")
            break
        else:
            print("Enter 1 to 4.")

    except ValueError:
        print("Invalid input.")
