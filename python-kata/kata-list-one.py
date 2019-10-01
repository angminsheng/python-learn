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

def digitize(n):
    new_list = list(str(n))
    new_list.reverse()
    return new_list

def digitize2(n):
    return [int(x) for x in str(n)[::-1]]

def getCount(inputStr):
    num_vowels = 0
    for alphabet in list(inputStr):
        if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u":
            num_vowels+=1
    
    return num_vowels

def getCount2(inputStr):
  return sum([1 for string in inputStr if string in "aeiou"])

def is_isogram(string):
    if len(list(string.lower())) != len(set(string.lower())):
        return False
    else:
        return True

def is_isogram2(string):
    return len(string) == len(set(string.lower()))