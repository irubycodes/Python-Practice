def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

print(calculate_grade(90))
print(calculate_grade(65))
print(calculate_grade(45))
print(calculate_grade(110))
print(calculate_grade(-5))