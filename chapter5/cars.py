#if Statements 

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

car = 'bmw'
print(car == 'bmw')

#OR 

car = 'Bmw' #casing matters
result = (car == 'bmw')
print(result)

#Ignoring Case When Checking for Equality 
car = 'Audi'
car.lower() == 'audi'


cars = ['audi', 'Bmw', 'subaru', 'toyota']

for car in cars:
	if (car.lower() == 'bmw'):
		print(car.upper())
	else:
		print(car.title())

	
cars = ['audi', 'Bmw', 'subaru', 'toyota']

for car in cars:
	if (car.lower() == 'bmw') and (len(car) < 5):
		print(car.upper())
	else:
		print(car.title())

print("\n") #skip line 

car = 'bmw'
result = (car == 'bmw')
print(result)




