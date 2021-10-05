#The Modulo Operator

# >>> 4 % 3
# 1
# >>> 5 % 3
# 2
# >>> 6 % 3
# 0
# >>> 7 % 3
# 1

#how many times does it go into the number 
# don't actually divide 


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print(f"\nThe number {number} is even.")
else:
	print(f"\nThe number {number} is odd.")