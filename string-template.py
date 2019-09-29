x = 15
price = 9.99
result = price * x

# two ways of creating dynamic String template
name = "Bob"
greeting = f"Hello,{name}"
name = "John"

longer_phrase = "Hello {} and {}"
greet = longer_phrase.format("rolf", "sally")

# user input
size_input = input("How long is your ruler (m)?")
size_m = float(size_input)
size_cm = size_m / 1.87
print(f"The ruler is {size_input}m or {size_cm:.2f}cm long.")
