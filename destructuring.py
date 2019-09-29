# destructuring
student_attendance = {"rolf":15, "simon":15, "james":20}

for student, attendance in student_attendance.items():
  print(f"{student} {attendance}")

print(student_attendance.keys())

jobs = [(42,"Bob","carpenter"), (20, "John", "student"), (35, "Simon", "teacher")]

for age, name, occupation in jobs:
  print(f"{age} {name} {occupation}")

head,*body,tail = [1,2,3,4,5]
print(head)
print(body)
print(tail)
