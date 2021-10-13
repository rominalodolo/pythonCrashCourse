#3.1
names = ['Jane', 'Anne', 'Romi', 'Sally', 'Jess' ]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

#3.2
greetings = f"Seasons greeting to {names[0].title()}."
print(greetings)


#3.3
cars = ['Ferrari', 'BMW', 'Fiat', 'Bently', 'Jeep', 'MINI', 'Rolls-Royce']
oneDay = f"One day I would like to own a {cars[3].title()}."
print(oneDay)


#3.4
guestList = ['jesus', 'lord', 'kanye']
message = f"Our Saviour, {guestList[0].title()}, has been formally invited to last supper."
print(f"\n{message}")

message = f"{guestList[1].title()}, find it in your heart to entertain your people at dinner which you have been formally invited to."
print(f"\n{message}")

message = f"Yeezys and a mirror will be at the dinner table {guestList[2].title()}. Please come."
print(f"\n{message}")


#3.5
guestList = ['jesus', 'ouma', 'jasmine']
guestList[0] = 'satan'
guestList[1] = 'kimk'
guestList[2] = 'mother teresa'
print(guestList)


#3.6 More Guests: 
guestList = ['jesus', 'lord', 'kanye']

guestList.insert(0, 'trump',)
guestList.insert(2,'bo jack')
guestList.append('mary')

print(guestList)

message = f"The party just got bigger, we have found a larger Last Supper table."
print(f"\n{message}")

message = f"{guestList[0].title()}, you are invited to have dinner with Kanye and Jesus."
print(f"\n{message}")

message = f"Our Saviour, {guestList[1].title()}, has been formally invited to last supper."
print(f"\n{message}")

message = f"We all know you have better things to do {guestList[2].title()} but there will be drugs and alcohol. RSVP, or don't. See you there."
print(f"\n{message}")

message = f"{guestList[3].title()}, find it in your heart to entertain your people at dinner which you have been formally invited to."
print(f"\n{message}")

message = f"Yeezys and a mirror will be at the dinner table {guestList[4].title()}. Please come."
print(f"\n{message}")

message = f"Come see your son one last time {guestList[5].title()} and ask the {guestList[3].title()} why He killed your boy."
print(f"\n{message}")



#3.7

guestList = ['trump', 'jesus', 'bo jack', 'lord', 'kanye', 'mary']

message = f"Sorry for the mess up but I have space for only two guests for the Last Supper."
print(f"\n{message}")

# Shrinking Guest List: You just found out that your new dinner table won’t arrive in time
# for the dinner, and you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that
# prints a message saying that you can invite only two people for
# dinner.

# Use pop() to remove guests from your list one at a time until only
# two names remain in your list. Each time you pop a name from
# your list, print a message to that person letting them know you’re
# sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting
# them know they’re still invited.
# Use del to remove the last two names from your list, so you have
# an empty list. Print your list to make sure you actually have an
# empty list at the end of your program.


#3.8 
guestList = ['trump', 'jesus', 'bo jack', 'lord', 'kanye', 'mary']

print(f"\nOriginal guest list: {guestList}")


print("\nHere is the sorted list:")
print(sorted(guestList))

print(f"\nOriginal guest list: {guestList}")

print(f"Sorted List: {sorted(guestList, reverse=True)}")

print(f"\nOriginal guest list again: {guestList}")


#3.9

# Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page
# 42), use len() to print a message indicating the number of people you are inviting to dinner.



#3.10

# Every Function: Think of something you could store in a list. For example, you could
# make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a
# program that creates a list containing these items and then uses each function introduced in this
# chapter at least once.



#3.11 Intentional Error: 

# If you haven’t received an index error in one of your programs yet,
# try to make one happen. Change an index in one of your programs to produce an index error.
# Make sure you correct the error before closing the program.