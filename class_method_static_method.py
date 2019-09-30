class TestClass:
  # instance method has access to the instance of the class.
  def instance_method(self):
    print(f"calling instance method of {self}")

  # class method has access to the class itself.
  @classmethod
  def class_method(cls):
    print(f"calling class method of {cls}")

  @staticmethod
  def static_method():
    print(f"calling a static method.")

# second example
class Book:
  TYPE = ("hardcover", "paperback")

  def __init__(self, name, book_type, weight):
    self.name = name
    self.book_type = book_type
    self.weight = weight

  def __str__(self):
    return f"This is {self.name} with {self.book_type} and weights {self.weight}g."
  
  @classmethod
  def hardcover(cls, name: str, weight: int) -> "Book":
    return cls(name, cls.TYPE[0], weight+100)

  @classmethod
  def paperback(cls, name:str, weight:int) -> "Book":
    return cls(name, cls.TYPE[1], weight)
  
book = Book.hardcover("harry potter", 150)
light = Book.paperback("hobbit", 140)


#exercises

class Store:
  def __init__(self,name):
    self.name = name
    self.items = []

  def add_item(self,name, price):
    self.items.append({"name":name, "price":price})

  def stock_price(self):
    return sum([item["price"] for item in self.items])

  @classmethod
  def franchise(cls, instance):
    return cls(f"{instance.name} - franchise")

  @staticmethod
  def store_details(store):
    return f"{store.name} has a stock price of {store.stock_price()}"
  


amazon = Store("Amazon")
amazon.add_item("fan", 250)

# print(Store.franchise(amazon).name)
print(Store.store_details(amazon))
