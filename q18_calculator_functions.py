def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a % b

def power(a, b):
    return a ** b

def calculator():
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        try:
            choice = int(input("Enter choice: "))
            if choice == 7:
                print("Goodbye!")
                break
            elif choice in range(1, 7):
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == 1:
                    print(f"Result: {add(a, b)}")
                elif choice == 2:
                    print(f"Result: {subtract(a, b)}")
                elif choice == 3:
                    print(f"Result: {multiply(a, b)}")
                elif choice == 4:
                    print(f"Result: {divide(a, b)}")
                elif choice == 5:
                    print(f"Result: {modulus(a, b)}")
                elif choice == 6:
                    print(f"Result: {power(a, b)}")
            else:
                print("Enter 1 to 7.")
        except ValueError:
            print("Invalid input.")

calculator()
