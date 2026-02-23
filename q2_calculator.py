try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\nResults:")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")

    if b == 0:
        print(f"{a} / {b} = Cannot divide by zero")
        print(f"{a} % {b} = Cannot divide by zero")
    else:
        print(f"{a} / {b} = {round(a / b, 2)}")
        print(f"{a} % {b} = {a % b}")

    print(f"{a} ^ {b} = {a ** b}")

except ValueError:
    print("Invalid input. Please enter numbers.")
