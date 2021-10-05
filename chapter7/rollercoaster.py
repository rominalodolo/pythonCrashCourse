#Using int() to Accept Numerical Input
#On consle

# age = input("How old are you? ")
# How old are you? 21

# age
# '21'

# >>> age = input("How old are you? ")
# How old are you? 21
# ➊ >>> age >= 18
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ➋ TypeError: unorderable types: str() >= int()

# age = input("How old are you? ")
# How old are you? 21
# ➊ >>> age = int(age)
# >>> age >= 18
# True

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

# How tall are you, in inches? 71
# You're tall enough to ride!



