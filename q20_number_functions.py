# ============================================================
# Question 20: Number System Functions
# Difficulty: Hard | Points: 9
# Description: 10 mathematical functions + math_menu() driver
# ============================================================

def factorial(n):
    """
    Returns n! (n factorial).
    Edge cases: 0! = 1, negative numbers return None.
    """
    if n < 0:
        return None      # Factorial undefined for negatives
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result        # 0! = 1 (loop doesn't execute for n=0)

def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    Handles: negatives, 0, 1, 2 as special cases.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Trial division up to √n
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True

def fibonacci(n):
    """
    Returns the nth Fibonacci number (1-indexed: F(1)=1, F(2)=1, F(3)=2 …).
    Returns None for n <= 0.
    """
    if n <= 0:
        return None
    if n == 1 or n == 2:
        return 1
    prev, curr = 1, 1
    for _ in range(2, n):
        prev, curr = curr, prev + curr
    return curr

def sum_of_digits(n):
    """Returns the sum of all digits of n (uses absolute value for negatives)."""
    return sum(int(digit) for digit in str(abs(n)))

def reverse_number(n):
    """Returns the integer n with its digits reversed. Handles negatives."""
    is_negative = n < 0
    reversed_str = str(abs(n))[::-1]
    reversed_int = int(reversed_str)
    return -reversed_int if is_negative else reversed_int

def is_armstrong(n):
    """
    Returns True if n is an Armstrong (narcissistic) number.
    An Armstrong number equals the sum of its digits raised to
    the power of the number of digits. Example: 153 = 1³ + 5³ + 3³.
    """
    if n < 0:
        return False  # Armstrong numbers are non-negative by convention
    digit_list  = [int(d) for d in str(n)]
    power       = len(digit_list)
    return sum(d ** power for d in digit_list) == n

def gcd(a, b):
    """
    Returns the Greatest Common Divisor of a and b using Euclidean algorithm.
    Works with negative integers too (uses absolute values).
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Returns the Least Common Multiple of a and b.
    LCM = |a × b| / GCD(a, b).
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def is_perfect_number(n):
    """
    Returns True if n is a perfect number (sum of proper divisors equals n).
    Example: 6 = 1 + 2 + 3. Returns False for n <= 0.
    """
    if n <= 1:
        return False
    # Sum all divisors of n that are less than n
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

# ── Main menu ─────────────────────────────────────────────────

def math_menu():
    """Displays a menu and lets the user test each mathematical function."""
    print("=" * 40)
    print("    🔢 NUMBER SYSTEM FUNCTIONS MENU")
    print("=" * 40)

    while True:
        print("\n1.  Factorial          (n!)")
        print("2.  Prime Checker      (is n prime?)")
        print("3.  Fibonacci          (nth term)")
        print("4.  Sum of Digits      (digit sum of n)")
        print("5.  Reverse Number     (reversal of n)")
        print("6.  Armstrong Checker  (is n Armstrong?)")
        print("7.  GCD                (of a and b)")
        print("8.  LCM                (of a and b)")
        print("9.  Perfect Number     (is n perfect?)")
        print("10. Exit")

        try:
            choice = int(input("\nEnter choice (1-10): "))

            if choice == 10:
                print("Goodbye! 👋")
                break

            elif choice == 1:
                n = int(input("Enter n for n!: "))
                result = factorial(n)
                if result is None:
                    print("Factorial is undefined for negative numbers.")
                else:
                    print(f"{n}! = {result}")

            elif choice == 2:
                n = int(input("Enter n to check primality: "))
                if is_prime(n):
                    print(f"{n} is PRIME ✅")
                else:
                    print(f"{n} is NOT prime ❌")

            elif choice == 3:
                n = int(input("Enter position n (1-indexed): "))
                result = fibonacci(n)
                if result is None:
                    print("Position must be a positive integer.")
                else:
                    print(f"Fibonacci({n}) = {result}")

            elif choice == 4:
                n = int(input("Enter n: "))
                print(f"Sum of digits of {n} = {sum_of_digits(n)}")

            elif choice == 5:
                n = int(input("Enter n: "))
                print(f"Reverse of {n} = {reverse_number(n)}")

            elif choice == 6:
                n = int(input("Enter n: "))
                if is_armstrong(n):
                    digit_list = [int(d) for d in str(n)]
                    power = len(digit_list)
                    formula = " + ".join(f"{d}^{power}" for d in digit_list)
                    print(f"{n} IS an Armstrong number ✅  ({formula} = {n})")
                else:
                    print(f"{n} is NOT an Armstrong number ❌")

            elif choice == 7:
                a = int(input("Enter first number a: "))
                b = int(input("Enter second number b: "))
                print(f"GCD({a}, {b}) = {gcd(a, b)}")

            elif choice == 8:
                a = int(input("Enter first number a: "))
                b = int(input("Enter second number b: "))
                print(f"LCM({a}, {b}) = {lcm(a, b)}")

            elif choice == 9:
                n = int(input("Enter n: "))
                if is_perfect_number(n):
                    divisors = [i for i in range(1, n) if n % i == 0]
                    print(f"{n} IS a Perfect Number ✅  ({' + '.join(map(str, divisors))} = {n})")
                else:
                    print(f"{n} is NOT a Perfect Number ❌")

            else:
                print("Invalid choice. Please enter a number between 1 and 10.")

        except ValueError:
            print("Error: Please enter a valid integer.")

# ── Entry point ───────────────────────────────────────────────
math_menu()
