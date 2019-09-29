users = [(0, "Bob", "password"), (2,"Jamie", "12345"), (4,"Susan","longpassword" )]

mapped_user = {user[1]:user for user in users}

print(mapped_user)

# input_username = input("insert username")
# input_password = input("insert password")

# _, username, password = mapped_user[input_username]

# if input_password == password:
#   print("login successful")
# else:  
#   print("login failed")

student = {"name":"Jose", "school": "computing", "grades":(66,77,88)}
students = [ {"name":"Jose", "school": "computing", "grades":(66,77,88)}, {"name":"May", "school": "computing", "grades":(36,47,88)}]

def average_grade(data):
  grades = data["grades"]
  return sum(grades)/ len(grades)

print(average_grade(student))

def average_grade_all_students(studentsList):
  total = 0
  count = 0
  for student in studentsList:
    total += sum(student["grades"])
    count += len(student["grades"])
  return total/count

print(average_grade_all_students(students))