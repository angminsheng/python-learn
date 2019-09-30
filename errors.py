def divide(dividend, divisor):
  if divisor ==0:
    raise ZeroDivisionError("Divisor cannot be zero!")
  return dividend / divisor

students = [
  {"name":"Bob", "grades":[80,75]},
  {"name":"Sally", "grades":[45,55]},
  {"name":"Sam", "grades":[35]},
  {"name":"Harry", "grades":[30,25]}
]

try:
  for student in students:
    name = student["name"]
    grades = student["grades"]
    average = divide(sum(grades), len(grades))
    print(f"{name}'s average is {average}.")
except ZeroDivisionError:
  print(f"{name}'s list is empty")
else:
  print("All students average calculated.")
finally:
  print("End of action.")
