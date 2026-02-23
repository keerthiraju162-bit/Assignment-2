try:
    num   = int(input("Enter number: "))
    end   = int(input("Enter range (end): "))

    print(f"\nMultiplication Table of {num}")
    for i in range(1, end + 1):
        print(f"{num} x {i} = {num * i}")

except ValueError:
    print("Invalid input.")
