def search(sequence, expected, finder):
  for elem in sequence:
    if finder(elem) == expected:
      return elem
  raise RuntimeError("Could not find an element with {expected}")

friends = [
  {"name":"Min", "age":27},
  {"name":"John", "age": 28},
  {"name":"Bob", "age":30}
]

def get_friend(obj):
  return obj["name"]

print(search(friends,"Min", get_friend))