correct_number = 7

# if user_input in ("y", "Y"):
#   user_number = input("Guess the correct number")
#   if int(user_number) == correct_number:
#     print(f"{user_number} is the correct number!")
#   elif abs(correct_number - user_number) == 1:
#     print("off by 1 !")
#   else:
#     print("Wrong !")

while True:
  user_input = input("Do you want to play a game?").lower()
  if user_input == "n":
    break
  user_number = int(input("Guess the correct number"))
  if int(user_number) == correct_number:
    print(f"{user_number} is the correct number!")
  elif abs(correct_number - user_number) == 1:
    print("off by 1 !")
  else:
    print("Wrong !")


