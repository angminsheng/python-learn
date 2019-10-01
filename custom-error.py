class TooManyPagesReadError(ValueError):
  pass

class Book:
  def __init__(self,name,pages):
    self.name = name
    self.pages= pages
    self.read_pages = 0

  def __str__(self):
    return f"This book is titled {self.name}"

  def read_book(self,pages):
    if self.read_pages + pages > self.pages:
      raise TooManyPagesReadError(f"You tried to read {self.read_pages + pages} pages but the book only has {self.pages} pages.")
    self.read_pages+=pages
    return f"you read {self.read_pages} pages out of {self.pages}"
  
harry_potter = Book("Harry Potter", 250)

try:
  print(harry_potter.read_book(350))
except TooManyPagesReadError as e:
  print(e)
  
