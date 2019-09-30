# similar to rest parameter in js
def mult(*args):
  print(args)
  total = 1
  for arg in args:
    total *= arg
  return total


print(mult(1,2,3,4))

arr = [2,3,4]

def multi(x,y,z):
  return x*y*z

# similar to spread operator
print(multi(*arr))

obj = {"x":15, "y":25, "z":20}
print(multi(**obj))

test = (1,2,3,4)

print(mult(*test))

def apply(*args, operator):
  if operator == "*":
    return mult(*args)
  elif operator == "+":
    return sum(args)
  else:
    return "not valid operator"

print(apply(1,2,3,4,5,operator="*"))

# collecting arguments
def createDic(**kwargs):
  print(kwargs)

createDic(name="Bob", age=15)

def details(name,age):
  print(f"{name} {age}")

me = {"name":"min", "age":27}
details(**me)

# ** when use in function definition serves as collect when used in function invocation serves as unpack.

def printName(**kwargs):
  print(kwargs.items())
  for key,value in kwargs.items():
    print(f"{key} : {value} ")

printName(name="Min", age="28")
