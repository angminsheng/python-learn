class Student:
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades
  
  def average_grades(self):
    return sum(self.grades) / len(self.grades)

student_one = Student("Bob", (10,9,8))

class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  
  def __str__(self):
    return f"{self.name} is {self.age} years old."

  def __repr__(self):
    return f"<Person('{self.name}',{self.age})>"

bob = Person("Bob", 25)


class Store:
  def __init__(self,name):
    self.name = name
    self.items = []
  
  def add_item(self, name, price):
    new_item = {"name":name, "price":price}
    self.items.append(new_item)

  def stock_price(self):
    # sum = 0
    # for item in self.items:
    #   sum += item["price"]
    # return sum
    return sum([item["price"] for item in self.items])

tea_mate = Store("TeaMate")
tea_mate.add_item("tea", 25)
tea_mate.add_item("cup", 55)
print(tea_mate.stock_price())
