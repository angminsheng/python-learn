digit = [1,2,3,4]
doubles = [x*2 for x in digit if x<4]
print(doubles)

friends = ["Sam", "Sui", "John", "Abby", "Samantha"]
starts_with_s_and_short = [friend.lower() for friend in friends if friend.startswith("S") and len(friend)< 5]

print(starts_with_s_and_short)

print(id(friends))

str = "mynameisminsheng"

print(str.split())

def DNA_strand(dna):
    str = ""
    for char in list(dna):
        if char == "A":
            str+="T"
        elif char == "T":
            str+="A"
        elif char == "G":
            str+="C"
        else:
            str+="G"
    return str

print(DNA_strand("TTTT"))

friends = [{"name":"Ang", "age":14}, {"name":"Anne", "age":15}]
print(friends[1]["name"])

student_attendance = {"rolf":15, "simon":15, "james":20}

for student in student_attendance:
  print(f"{student}'s attendance is {student_attendance[student]} days.")

if "Bob" in student_attendance:
  print(f"Bob {student_attendance['Bob']}")
else:
  print("Bob is not a student.")



