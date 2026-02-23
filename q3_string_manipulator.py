sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"Original: {sentence}")
print(f"Characters (with spaces): {len(sentence)}")
print(f"Characters (without spaces): {len(sentence.replace(' ', ''))}")
print(f"Words: {len(words)}")
print(f"UPPERCASE: {sentence.upper()}")
print(f"lowercase: {sentence.lower()}")
print(f"Title Case: {sentence.title()}")
print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Reversed: {sentence[::-1]}")
