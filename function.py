
def greeting(name, surname):
  print(f"{name}, {surname}")

# positional and key argument. Key argument cannot come before positional argument
greeting(surname="Lenning", name="John")
greeting("John", "Lenning")

# default parameter must go before non default parameter

def addition(x,y=5):
  return x+y

print("test"*5)

num = [1,2,3,4,5]
double = list(map(lambda x: x*2, num))
print(double)

