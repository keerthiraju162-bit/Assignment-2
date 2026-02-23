# ============================================================
# Question 16: Number Guessing Game
# Difficulty: Hard | Points: 7
# Description: Computer picks a random number; user gets 7 attempts
# Bonus: Best score tracking, hints when close (within 5),
#        difficulty levels (Easy: 1-50, Medium: 1-100, Hard: 1-1000)
# ============================================================

import random

# Track the best score (fewest attempts used to win) across sessions
best_score = None  # None means no win yet

def play_game(lower_bound, upper_bound, max_attempts):
    """
    Runs one round of the guessing game.
    Returns the number of attempts used if player wins, else None.
    """
    # Computer picks a secret number in the given range
    secret_number  = random.randint(lower_bound, upper_bound)
    attempts_used  = 0
    player_won     = False

    print(f"\n🎯 I've picked a number between {lower_bound} and {upper_bound}.")
    print(f"   You have {max_attempts} attempts. Good luck!\n")

    while attempts_used < max_attempts:
        attempts_remaining = max_attempts - attempts_used

        try:
            player_guess  = int(input(f"Attempt {attempts_used + 1}/{max_attempts} — Your guess: "))
            attempts_used += 1

            # ── Validate guess is within range ────────────────
            if player_guess < lower_bound or player_guess > upper_bound:
                print(f"  ⚠️  Please guess between {lower_bound} and {upper_bound}.")
                attempts_used -= 1  # Don't count invalid guess
                continue

            # ── Check guess ───────────────────────────────────
            if player_guess == secret_number:
                player_won = True
                print(f"\n🎉 Correct! You guessed it in {attempts_used} attempt(s)!")
                break

            elif player_guess < secret_number:
                direction = "📈 Too LOW!"
            else:
                direction = "📉 Too HIGH!"

            # BONUS: Hint when within 5 of the answer
            difference = abs(player_guess - secret_number)
            if difference <= 5:
                hint = " 🔥 You're very close!"
            elif difference <= 15:
                hint = " 🌡️  Getting warmer..."
            else:
                hint = ""

            print(f"  {direction}{hint}")
            print(f"  Attempts remaining: {attempts_remaining - 1}")

        except ValueError:
            print("  ⚠️  Please enter a valid integer.")

    if not player_won:
        print(f"\n😞 Game over! The number was {secret_number}.")

    return attempts_used if player_won else None

# ── Main game loop ────────────────────────────────────────────
print("=" * 40)
print("     🎮 NUMBER GUESSING GAME")
print("=" * 40)

while True:
    # BONUS: Difficulty selection
    print("\nSelect Difficulty:")
    print("1. Easy   (1 – 50,   10 attempts)")
    print("2. Medium (1 – 100,   7 attempts)")
    print("3. Hard   (1 – 1000,  7 attempts)")

    try:
        difficulty = int(input("Choose difficulty (1-3): "))
        if difficulty == 1:
            low, high, attempts = 1, 50, 10
        elif difficulty == 2:
            low, high, attempts = 1, 100, 7
        elif difficulty == 3:
            low, high, attempts = 1, 1000, 7
        else:
            print("Invalid choice. Defaulting to Medium.")
            low, high, attempts = 1, 100, 7
    except ValueError:
        print("Invalid input. Defaulting to Medium.")
        low, high, attempts = 1, 100, 7

    # Play one round
    score = play_game(low, high, attempts)

    # BONUS: Update best score
    if score is not None:
        if best_score is None or score < best_score:
            best_score = score
            print(f"🏆 New Best Score: {best_score} attempt(s)!")
        else:
            print(f"🏆 Best Score So Far: {best_score} attempt(s)")

    # Ask if user wants to play again
    play_again = input("\nPlay again? (yes/no): ").strip().lower()
    if play_again not in ("yes", "y"):
        print("\nThanks for playing! 👋")
        if best_score is not None:
            print(f"Your all-time best: {best_score} attempt(s)")
        break
