class BookShelf:
  def __init__(self,*books):
    self.books = books
  
  def __str__(self):
    return f"This bookshelf has {len(self.books)} books."

class Book:
  def __init__(self,name):
    self.name = name
  
  def __str__(self):
    return f"Book {self.name}"
  
book1 = Book("Harry Potter")
book2 = Book("Lord of the Ring")

bookshelf = BookShelf(book1,book2)

print(book1)
print(bookshelf)
print(bookshelf.books)
