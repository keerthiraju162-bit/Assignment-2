try:
    pattern = int(input("Choose pattern (1-4): "))
    height  = int(input("Enter height: "))

    if pattern == 1:
        for i in range(1, height + 1):
            print(" ".join(str(n) for n in range(1, i + 1)))

    elif pattern == 2:
        for i in range(1, height + 1):
            print(" ".join(str(i) for _ in range(i)))

    elif pattern == 3:
        for i in range(height, 0, -1):
            print(" ".join(str(n) for n in range(i, 0, -1)))

    elif pattern == 4:
        for i in range(1, height + 1):
            up   = "".join(str(n) for n in range(1, i + 1))
            down = "".join(str(n) for n in range(i - 1, 0, -1))
            print(up + down)

    else:
        print("Enter 1 to 4.")

except ValueError:
    print("Invalid input.")
