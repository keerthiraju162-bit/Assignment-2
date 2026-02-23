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

try:
    # Part 1
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is NOT a prime number")

    # Part 2
    start = int(input("Enter start range: "))
    end   = int(input("Enter end range: "))
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    print(f"Prime numbers: {', '.join(map(str, primes))}")

except ValueError:
    print("Invalid input.")
