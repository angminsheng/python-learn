class Device:
  def __init__(self, name, connected_by):
    self.name = name
    self.connected_by = connected_by
    self.connected = True
  
  def __str__(self):
    return f"Device {self.name!r} ({self.connected_by})"


printer = Device("printer", "cable")

print(printer)