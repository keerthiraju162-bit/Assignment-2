try:
    count = int(input("How many numbers? "))
    numbers = []

    for i in range(1, count + 1):
        numbers.append(float(input(f"Enter number {i}: ")))

    print(f"\nSum     : {sum(numbers)}")
    print(f"Average : {sum(numbers) / count:.2f}")
    print(f"Maximum : {max(numbers)}")
    print(f"Minimum : {min(numbers)}")

except ValueError:
    print("Invalid input.")
