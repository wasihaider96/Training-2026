students = [
    {"name": "Ali", "scores": [80, 75, 90], "subject": "Math"},
    {"name": "Ahmed", "scores": [60, 65, 70], "subject": "Math"},
    {"name": "Sara", "scores": [90, 92, 95], "subject": "Math"},
    {"name": "Zain", "scores": [50, 55, 60], "subject": "Math"},
    {"name": "Ayesha", "scores": [85, 88, 84], "subject": "Math"}
]

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

def class_topper(students):
    top_student = None
    highest_avg = 0

    for student in students:
        avg = calculate_average(student["scores"])
        if avg > highest_avg:
            highest_avg = avg
            top_student = student

    return top_student

topper = class_topper(students)

sorted_students = sorted(
    students,
    key=lambda s: calculate_average(s["scores"]),
    reverse=True
)

print("Name | Avg | Grade")
print("-------------------")

for student in sorted_students:
    avg = calculate_average(student["scores"])
    grade = get_grade(avg)

    line = f"{student['name']} | {avg:.2f} | {grade}"

    if student["name"] == topper["name"]:
        line += "  *** TOP ***"

    print(line)