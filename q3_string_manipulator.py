# ============================================================
# Question 3: String Manipulator
# Difficulty: Medium | Points: 4
# Description: Takes a sentence and performs 10 string operations
# ============================================================

# Get input from the user
sentence = input("Enter a sentence: ")

# Edge case: empty input
if not sentence.strip():
    print("Error: Please enter a non-empty sentence.")
else:
    # Split into words for word-based operations
    words = sentence.split()

    # 1. Original sentence
    original_sentence = sentence

    # 2. Character count WITH spaces
    char_count_with_spaces = len(sentence)

    # 3. Character count WITHOUT spaces
    char_count_without_spaces = len(sentence.replace(" ", ""))

    # 4. Total words
    total_words = len(words)

    # 5-7. Case transformations
    uppercase_sentence = sentence.upper()
    lowercase_sentence = sentence.lower()
    titlecase_sentence = sentence.title()

    # 8. First word
    first_word = words[0]

    # 9. Last word
    last_word = words[-1]

    # 10. Reversed sentence (character-by-character)
    reversed_sentence = sentence[::-1]

    # Display all results
    print(f"\nOriginal: {original_sentence}")
    print(f"Characters (with spaces): {char_count_with_spaces}")
    print(f"Characters (without spaces): {char_count_without_spaces}")
    print(f"Words: {total_words}")
    print(f"UPPERCASE: {uppercase_sentence}")
    print(f"lowercase: {lowercase_sentence}")
    print(f"Title Case: {titlecase_sentence}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Reversed: {reversed_sentence}")
