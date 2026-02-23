text = input("Enter word/number: ").strip()

original = text
reversed_text = text[::-1]
cleaned = text.replace(" ", "").lower()

print(f"Original : {original}")
print(f"Reversed : {reversed_text}")

if cleaned == cleaned[::-1]:
    print("Result   : PALINDROME")
else:
    print("Result   : NOT a Palindrome")
