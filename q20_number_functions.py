def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 0:
        return None
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

def reverse_number(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def is_perfect_number(n):
    if n <= 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def math_menu():
    while True:
        print("\n1.  Factorial")
        print("2.  Prime Checker")
        print("3.  Fibonacci")
        print("4.  Sum of Digits")
        print("5.  Reverse Number")
        print("6.  Armstrong Checker")
        print("7.  GCD")
        print("8.  LCM")
        print("9.  Perfect Number")
        print("10. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 10:
                print("Goodbye!")
                break
            elif choice == 1:
                n = int(input("Enter n: "))
                r = factorial(n)
                print(f"{n}! = {r}" if r is not None else "Not defined for negatives.")
            elif choice == 2:
                n = int(input("Enter n: "))
                print(f"{n} is {'PRIME' if is_prime(n) else 'NOT prime'}")
            elif choice == 3:
                n = int(input("Enter position n: "))
                r = fibonacci(n)
                print(f"Fibonacci({n}) = {r}" if r is not None else "Enter positive number.")
            elif choice == 4:
                n = int(input("Enter n: "))
                print(f"Sum of digits = {sum_of_digits(n)}")
            elif choice == 5:
                n = int(input("Enter n: "))
                print(f"Reversed = {reverse_number(n)}")
            elif choice == 6:
                n = int(input("Enter n: "))
                print(f"{n} {'IS' if is_armstrong(n) else 'is NOT'} an Armstrong number")
            elif choice == 7:
                a, b = int(input("Enter a: ")), int(input("Enter b: "))
                print(f"GCD({a}, {b}) = {gcd(a, b)}")
            elif choice == 8:
                a, b = int(input("Enter a: ")), int(input("Enter b: "))
                print(f"LCM({a}, {b}) = {lcm(a, b)}")
            elif choice == 9:
                n = int(input("Enter n: "))
                print(f"{n} {'IS' if is_perfect_number(n) else 'is NOT'} a perfect number")
            else:
                print("Enter 1 to 10.")
        except ValueError:
            print("Invalid input.")

math_menu()
