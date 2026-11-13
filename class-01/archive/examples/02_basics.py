# 02_basics.py — The building blocks of Python

# ---- 1. Data types --------------------------------------------------
score = 42            # int   (whole number)
height = 1.45         # float (decimal number)
pet = "cat"           # str   (text)
is_happy = True       # bool  (True / False)

print(type(score), type(height), type(pet), type(is_happy))

# ---- 2. Maths --------------------------------------------------------
print(7 + 3, 7 - 3, 7 * 3, 7 / 3)   # 10 4 21 2.333...
print(7 // 3, 7 % 3, 2 ** 5)        # 2 1 32  (floor-divide, remainder, power)

# ---- 3. Lists --------------------------------------------------------
fruits = ["apple", "banana", "mango"]
print(fruits[0])        # first item -> apple  (counting starts at 0!)
fruits.append("kiwi")
print(fruits, "has", len(fruits), "items")

# ---- 4. if / elif / else --------------------------------------------
temperature = 31
if temperature > 30:
    print("It's hot! 🥵")
elif temperature > 15:
    print("Nice weather 😎")
else:
    print("Brr, cold! 🥶")

# ---- 5. Loops --------------------------------------------------------
for fruit in fruits:
    print("I like", fruit)

for i in range(1, 6):          # 1, 2, 3, 4, 5
    print(i, "x 7 =", i * 7)

count = 3
while count > 0:
    print(count, "...")
    count -= 1
print("Blast off! 🚀")

# ---- 6. Functions ----------------------------------------------------
def area_of_rectangle(width, height):
    """Return the area of a rectangle."""
    return width * height

print("Area:", area_of_rectangle(4, 5))
