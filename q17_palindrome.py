# ============================================================
# Question 17: Palindrome Checker
# Difficulty: Medium | Points: 4
# Description: Checks if a word or number is a palindrome
#              with step-by-step verification shown
# ============================================================

print("=== PALINDROME CHECKER ===\n")

user_input = input("Enter a word or number: ").strip()

# Edge case: empty input
if not user_input:
    print("Error: Please enter a non-empty word or number.")
else:
    # ── Normalise for comparison ──────────────────────────────
    # For words: ignore case; for numbers: use as-is
    # Strip spaces and convert to lowercase for comparison only
    cleaned_input    = user_input.replace(" ", "").lower()
    reversed_cleaned = cleaned_input[::-1]

    # Build a "display" reversed version that mirrors original casing
    # (reverse the characters, flip case to match expected output)
    display_reversed = user_input[::-1]

    is_palindrome = (cleaned_input == reversed_cleaned)

    # ── Step-by-step verification ─────────────────────────────
    print(f"\nOriginal : {user_input}")
    print(f"Reversed : {display_reversed}")

    # Show character-by-character comparison
    print("\nCharacter Comparison:")
    is_match = True
    for left_char, right_char in zip(cleaned_input, reversed_cleaned):
        match_symbol = "✓" if left_char == right_char else "✗"
        if left_char != right_char:
            is_match = False
        print(f"  '{left_char}' ↔ '{right_char}'  {match_symbol}")

    # ── Result ────────────────────────────────────────────────
    if is_palindrome:
        print(f"\nResult: ✅ PALINDROME")
        print(f"'{user_input}' reads the same forwards and backwards.")
    else:
        print(f"\nResult: ❌ NOT a Palindrome")
        print(f"'{user_input}' does not read the same forwards and backwards.")
