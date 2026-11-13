# 01_hello.py — Your very first Python program!
# Run it with:  python class-01/examples/01_hello.py

print("Hello, world!")

# Variables are labelled boxes that hold a value
name = input("What is your name? ")
age = int(input("How old are you? "))

print("Nice to meet you,", name)
print("In 10 years you will be", age + 10)

# f-strings let you put variables right inside text
print(f"{name} has been alive for about {age * 365} days!")
