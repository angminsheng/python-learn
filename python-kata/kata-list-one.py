def yes_or_no(boolean):
  return "Yes" if boolean else "No"

def remove_space(string):
  string_list = list(string)
  new_list = [char for char in string_list if char != " "]
  return "".join(new_list)

def remove_space2(string):
  return string.replace(" ", "")

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "/":
        return value1/value2
    else:
        return value1 * value2

# dictionary.get() returns value of the dictionary but does not throw an error if nothing is found.
obj = {"name":"min", "age":27}
print(obj.get("name"),obj.get("age"), obj.get("job","Not found!"))

def basic_op2(operator, a,b):
  return {"+":a+b, "-":a-b, "/":a/b, "*":a*b}.get(operator)

def solution(string):
    new_list = list(string)
    new_list.reverse()
    return "".join(new_list)

# slicing syntax
# [start:stop-1]
items = ["a","b","c","d","e","f","g","h","i"]
new_items = items[::-1]

def solution2(string):
  return string[::-1]