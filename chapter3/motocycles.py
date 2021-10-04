#Changing, Adding, and Removing Elements

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)


#Append adds it to the back of the list
motorcycles.append('ducati')
print(motorcycles)


motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Insert adds a new element at any position in your list using index
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'bmw')
print(motorcycles)


#Removing Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#delets everything
del motorcycles[:]
print(motorcycles)



#Pop Method - removes the last item in a list, but it lets you work with
#that item after removing it

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)



#Removing an item by value

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)




#Avoiding Index Errors w/lists
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles[3])

#Traceback (most recent call last):
#File "motorcycles.py", line 2, in <module>
#print(motorcycles[3])
#IndexError: list index out of range




