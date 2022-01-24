#4.1

myPizzas = ['Margarita', 'Vegetarian', '4Cheeses']

for pizza in myPizzas:
    print(pizza)

print("\n")

for pizza in myPizzas:
        print(f"I like {pizza} pizza!")

print("\nI really love pizza!")
 


#4.2

animals = ['dog', 'cat', 'rabbit']

for pet in animals:
    print (f"{pet}")


animals = ['dog', 'cat', 'rabbit']

print(f"A {animals[0]} would make a great best friend.")
print("\n")

print(f"A {animals[1]} would make a great mess.")
print("\n")

print(f"A {animals[2]} would make a great day even better!")
print("\n")

print(f"Any of these animals would make a great pet!")
print("\n")


#4.3 Counting to Twenty
numbers = list(range(1, 21))

for number in numbers:
    print(number)

#4.4 One Million: 
numbers = list(range(1, 1000001))

for number in numbers:
    print(number)
# (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

#4.5 Summing a Million: Make a list of the numbers from one to one million, and then use
min() and max() to make sure your list actually starts at one and ends at one million. Also, use
the sum() function to see how quickly Python can add a million numbers.


#4.6. Odd Numbers: Use the third argument of the range() function to make a list of the odd
numbers from 1 to 20. Use a for loop to print each number.


#4.7 Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the
numbers in your list.

#4.8 Cubes: 
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)


#4.9 Cube Comprehension
cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)

#4.10 Slices: Using one of the programs you wrote in this chapter, add several lines to the end
of the program that do the following:
Print the message The first three items in the list are:. Then use a
slice to print the first three items from that program’s list.
Print the message Three items from the middle of the list are:. Use a
slice to print three items from the middle of the list.
Print the message 

print (f"The last three items in the list are:." Use a slice to
print the last three items in the list.

#4.11
myPizzas = ['Margarita', 'Vegetarian', '4Cheeses']
friend_pizzas = myPizzas[:]

myPizzas.append("vegan")
friend_pizzas.append('avo & feta')

print("My favorite pizzas are:")
for pizza in myPizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")


#4.12 More Loops: All versions of foods.py in this section have avoided using for loops when
printing to save space. Choose a version of foods.py, and write two for loops to print each list of
foods.

#4.13 Buffet:

basic_menu = (
    "beyond beef burger", "veggie spring roll", "grilled cheese", "ice-cream sunday", "ice-coffee",
)

print("These are the items you can choose from: ")
for item in basic_menu:
    print(f"- {item}")

print("\nOur menu has been updated.")

# Try to modify one of the items, and make sure that Python rejects
# the change.
# The restaurant changes its menu, replacing two of the items with
# different foods. Add a line that rewrites the tuple, and then use a
# for loop to print each of the items on the revised menu.

#4.14
# PEP 8: Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008/. 

#4.15 Code Review:
# Choose three of the programs you’ve written in this chapter and modify
# each one to comply with PEP 8:
# Use four spaces for each indentation level. Set your text editor to
# insert four spaces every time you press TAB, if you haven’t already
# done so (see Appendix B for instructions on how to do this).
# Use less than 80 characters on each line, and set your editor to
# show a vertical guideline at the 80th character position.
# Don’t use blank lines excessively in your program files.