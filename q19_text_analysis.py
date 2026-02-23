def count_words(text):
    return len(text.split())

def count_vowels(text):
    return sum(1 for c in text if c in "aeiouAEIOU")

def count_consonants(text):
    return sum(1 for c in text if c.isalpha() and c not in "aeiouAEIOU")

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def remove_vowels(text):
    return "".join(c for c in text if c not in "aeiouAEIOU")

def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq

def longest_word(text):
    return max(text.split(), key=len)

def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print(f"Words         : {count_words(text)}")
    print(f"Vowels        : {count_vowels(text)}")
    print(f"Consonants    : {count_consonants(text)}")
    print(f"Reversed      : {reverse_text(text)}")
    print(f"Palindrome    : {'Yes' if is_palindrome(text) else 'No'}")
    print(f"Without vowels: {remove_vowels(text)}")
    lw = longest_word(text)
    print(f"Longest word  : {lw} ({len(lw)} letters)")
    freq = word_frequency(text)
    print(f"Word Frequency: {', '.join(f'{k}: {v}' for k, v in freq.items())}")

text = input("Enter text: ")
analyze_text(text)
