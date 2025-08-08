student_scores = { "Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62, }
student_grades = {}

for key, value in student_scores.items():
    if value > 90 and value <= 100:
        student_grades.update({key : "Outstanding"})
    elif value > 80:
        student_grades.update({key : "Exceeds Expectations"})
    elif value > 70:
        student_grades.update({key : "Acceptatble"})
    else:
        student_grades.update({key: "Fail"})
for key, value in student_grades.items():
    print(f"{key}: {value}")
