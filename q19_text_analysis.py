# ============================================================
# Question 19: Text Analysis Functions
# Difficulty: Hard | Points: 9
# Description: 9 text analysis functions + analyze_text() driver
# ============================================================

def count_words(text):
    """Returns the number of words in text."""
    return len(text.split())

def count_vowels(text):
    """Returns the number of vowel characters in text (case-insensitive)."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def count_consonants(text):
    """Returns the number of consonant characters in text (letters only, no vowels)."""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in text if char in consonants)

def reverse_text(text):
    """Returns the text reversed character by character."""
    return text[::-1]

def is_palindrome(text):
    """
    Returns True if text is a palindrome.
    Ignores spaces and case for comparison.
    """
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def remove_vowels(text):
    """Returns the text with all vowel characters removed."""
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

def word_frequency(text):
    """
    Returns a dictionary mapping each word (lowercase) to
    its frequency count in the text.
    """
    frequency_map = {}
    for word in text.lower().split():
        # Strip punctuation from word boundaries
        word = word.strip(".,!?;:\"'")
        if word:  # Ignore empty strings after stripping
            frequency_map[word] = frequency_map.get(word, 0) + 1
    return frequency_map

def longest_word(text):
    """Returns the longest word found in the text."""
    words = text.split()
    if not words:
        return ""
    # Find the word with maximum length; tie-break by first occurrence
    return max(words, key=len)

def analyze_text(text):
    """
    Calls all analysis functions and prints a formatted report.
    """
    print("\n=== TEXT ANALYSIS ===")
    print(f"Words           : {count_words(text)}")
    print(f"Vowels          : {count_vowels(text)}")
    print(f"Consonants      : {count_consonants(text)}")
    print(f"Reversed        : {reverse_text(text)}")
    print(f"Palindrome      : {'Yes' if is_palindrome(text) else 'No'}")
    print(f"Without vowels  : {remove_vowels(text)}")

    # Longest word with letter count
    longest = longest_word(text)
    print(f"Longest word    : {longest} ({len(longest)} letters)")

    # Word frequency dictionary formatted for display
    freq = word_frequency(text)
    freq_display = ", ".join(f"{word}: {count}" for word, count in freq.items())
    print(f"Word Frequency  : {freq_display}")

# ── Entry point ───────────────────────────────────────────────
print("=== TEXT ANALYSIS TOOL ===\n")

user_text = input("Enter text: ").strip()

if not user_text:
    print("Error: Please enter some text.")
else:
    analyze_text(user_text)
