user_age = int(input("What is your age?"))
user_age_month = user_age * 12
print(f"you are {user_age}years old or {user_age_month} months old.")

l = ["bob", "john", "sally"]
t = ("bob", "john", "sally")
h = {"bob", "john", "sally"}

l.append("rosie")

h.add("molly")

friends = {"bob", "ken" , "simon"}
other_friends = {"jasmine", "tom", "jimmy"}
abroad = {"bob", "ken"}
local_friends = friends.difference(abroad)
print(local_friends)

total_friends = friends.union(other_friends)
print(total_friends)

art = {"bob", "tom", "susie"}
science = {"bob"}
both = art.intersection(science)
print(both)

team_a = ["ken", "bob"]
team_b = ["ken", "bob"]

print(team_a == team_b)
print(team_a is team_b)

# if statment
day_of_week = input("Which day of the week is today?").lower()

if day_of_week == "Monday":
  print("Have a nice week!")
elif day_of_week == "Tuesday":
  print("Full speed ahead!")
else:
  print("Almost there!")

fruits = ["apple", "orange", "pear"]
print("apple" in fruits)