subjects = ["Maths", "Science", "English", "History", "Computer Science"]
marks = []

for sub in subjects:
    while True:
        try:
            m = float(input(f"Enter marks for {sub} (0-100): "))
            if 0 <= m <= 100:
                marks.append(m)
                break
            else:
                print("Enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input.")

total = sum(marks)
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

result = "PASS" if all(m >= 40 for m in marks) else "FAIL"

print(f"\nTotal      : {total}/500")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print(f"Result     : {result}")
