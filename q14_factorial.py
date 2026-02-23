try:
    n = int(input("Enter a number: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")
    elif n == 0:
        print("0! = 1")
    else:
        result = 1
        steps  = []
        for i in range(n, 0, -1):
            result *= i
            steps.append(str(i))
        print(f"{n}! = {' x '.join(steps)} = {result}")

except ValueError:
    print("Invalid input.")
