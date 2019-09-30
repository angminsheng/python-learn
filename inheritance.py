class Device:
  def __init__(self, name, connected_by):
    self.name = name
    self.connected_by = connected_by
    self.connected = True
  
  def __str__(self):
    return f"Device {self.name!r} ({self.connected_by})"
  
  def disconnect(self):
    self.connected = False
    print("disconnected")

class Printer(Device):
  def __init__(self, name, connected_by, capacity):
    super().__init__(name, connected_by)
    self.capacity = capacity
    self.remaining_pages = capacity
  
  def print_pages(self, pages):
    if not self.connected:
      print("The printer is not connected.")
    else:
      print(f"printing {pages} pages.")
      self.remaining_pages -= pages
  
  def __str__(self):
    return f"{super().__str__()} with {self.remaining_pages} remaining pages."
  
printer = Printer("Sony", "USB", 500)

print(printer)
printer.print_pages(200)
print(printer)
printer.disconnect()
printer.print_pages(20)


  
