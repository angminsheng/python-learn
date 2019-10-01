import functools

user = {"username":"Min", "role":"guest"}

def secure_password(func):
  @functools.wraps(func)
  def secure(*args, **kwargs):
      return func(*args, **kwargs)
  return secure

@secure_password
def get_password(role):
  if role == "admin":
    return "1234"
  elif role == "billing":
    return "super_secure_password"


#functools.wraps allows the function name to be kept as the original name instead of the return function of the decorator.
print(get_password("billing"))

def test(*args, **kwargs):
  print(f"args:{args} kwargs:{kwargs}")

test(1,{"name":"min"})
