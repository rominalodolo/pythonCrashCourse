#Slicing a List

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])


#omit
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])


#Looping Through a Slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

#Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


#append
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

