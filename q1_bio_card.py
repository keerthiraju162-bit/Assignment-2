# ============================================================
# Question 1: Personal Bio Card
# Difficulty: Easy | Points: 2
# Description: Displays student information in a formatted box
# ============================================================

# Student information stored in variables
student_name   = "John Doe"
student_age    = 20
student_course = "Python Programming"
student_college = "ABC University"
student_email  = "john@example.com"

# Box border width (inner content width)
BOX_WIDTH = 34

# Helper function to format a single row inside the box
def format_row(label, value):
    """Returns a formatted row string padded to BOX_WIDTH."""
    content = f" {label:<8}: {value} "
    # Pad the content to fit exactly inside the box
    content = content.ljust(BOX_WIDTH)
    return f"║{content}║"

# Print the bio card
print("╔" + "═" * BOX_WIDTH + "╗")
print("║" + " STUDENT BIO CARD".center(BOX_WIDTH) + "║")
print("╠" + "═" * BOX_WIDTH + "╣")
print(format_row("Name",    student_name))
print(format_row("Age",     f"{student_age} years"))
print(format_row("Course",  student_course))
print(format_row("College", student_college))
print(format_row("Email",   student_email))
print("╚" + "═" * BOX_WIDTH + "╝")
