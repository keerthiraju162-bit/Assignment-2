while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 7:
            print("Goodbye!")
            break
        elif choice in range(1, 7):
            temp = float(input("Enter temperature: "))

            if choice == 1:
                print(f"Result: {(temp * 9/5) + 32:.2f} F")
            elif choice == 2:
                print(f"Result: {(temp - 32) * 5/9:.2f} C")
            elif choice == 3:
                print(f"Result: {temp + 273.15:.2f} K")
            elif choice == 4:
                print(f"Result: {temp - 273.15:.2f} C")
            elif choice == 5:
                print(f"Result: {(temp - 32) * 5/9 + 273.15:.2f} K")
            elif choice == 6:
                print(f"Result: {(temp - 273.15) * 9/5 + 32:.2f} F")
        else:
            print("Enter 1 to 7.")

    except ValueError:
        print("Invalid input.")
