# ============================================================
# Question 6: Grade Calculator
# Difficulty: Easy-Medium | Points: 4
# Description: Calculates grade and pass/fail for 5 subjects
# ============================================================

print("=== GRADE CALCULATOR ===\n")

# Subject names list for clean display
subject_names = ["Mathematics", "Science", "English", "History", "Computer Science"]
marks_list    = []  # Will store marks for each subject

# Collect marks for each subject using a loop
for subject in subject_names:
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            # Validate marks are in the valid range
            if 0 <= marks <= 100:
                marks_list.append(marks)
                break
            else:
                print("  Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("  Invalid input. Please enter a number.")

# ── Calculations ─────────────────────────────────────────────
total_marks      = sum(marks_list)
max_possible     = 500
percentage       = (total_marks / max_possible) * 100

# Determine grade based on percentage
if percentage >= 90:
    grade       = "A+"
    grade_label = "Outstanding"
elif percentage >= 80:
    grade       = "A"
    grade_label = "Excellent"
elif percentage >= 70:
    grade       = "B"
    grade_label = "Good"
elif percentage >= 60:
    grade       = "C"
    grade_label = "Average"
elif percentage >= 50:
    grade       = "D"
    grade_label = "Pass"
else:
    grade       = "F"
    grade_label = "Fail"

# Pass only if ALL subjects have marks >= 40 (no subject failure)
passed_all_subjects = all(m >= 40 for m in marks_list)
result              = "PASS" if passed_all_subjects else "FAIL"

# ── Display results ───────────────────────────────────────────
print("\n=== RESULT CARD ===")
print(f"{'Subject':<25} {'Marks':>6} {'Max':>6}")
print("-" * 40)
for subject, marks in zip(subject_names, marks_list):
    status = "✓" if marks >= 40 else "✗ (Failed)"
    print(f"{subject:<25} {marks:>6.1f} {100:>6}  {status}")

print("-" * 40)
print(f"{'Total':<25} {total_marks:>6.1f} {max_possible:>6}")
print(f"\nPercentage : {percentage:.2f}%")
print(f"Grade      : {grade} ({grade_label})")
print(f"Result     : {result}")

# Show which subjects were failed (if any)
if not passed_all_subjects:
    failed_subjects = [subject_names[i] for i, m in enumerate(marks_list) if m < 40]
    print(f"Failed in  : {', '.join(failed_subjects)}")
