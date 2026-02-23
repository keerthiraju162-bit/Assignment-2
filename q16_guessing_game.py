import random

while True:
    secret   = random.randint(1, 100)
    attempts = 7

    print("\nI've picked a number between 1 and 100. You have 7 attempts.")

    for i in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {i}/7 - Your guess: "))

            if guess == secret:
                print(f"Correct! You guessed it in {i} attempt(s)!")
                break
            elif guess < secret:
                print(f"Too LOW! Attempts remaining: {attempts - i}")
            else:
                print(f"Too HIGH! Attempts remaining: {attempts - i}")
        except ValueError:
            print("Enter a valid number.")
            i -= 1
    else:
        print(f"Game over! The number was {secret}.")

    again = input("Play again? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Goodbye!")
        break
