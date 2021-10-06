#Working with Classes and Instances

	#The Car Class

# class Car:
# 	#A simple attempt to represent a car.

# 	def __init__(self, make, model, year):
# 	#Initialize attributes to describe a car.
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 	def get_descriptive_name(self):
# 	#Return a neatly formatted descriptive name.
# 		long_name = f"{self.year} {self.make} {self.model}"
# 		return long_name.title()

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())



class Car:
#A simple attempt to represent a car.
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
	
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles



#Modifying Attribute Values

	#Modifying an Attribute’s Value Directly

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()


	#Modifying an Attribute’s Value Through a Method

#class Car:
# --snip--
#	def update_odometer(self, mileage):
# 		Set the odometer reading to the given value.
# 		self.odometer_reading = mileage

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(23)
# my_new_car.read_odometer()



# class Car:
# --snip--
# def update_odometer(self, mileage):

# Set the odometer reading to the given value.
# Reject the change if it attempts to roll the odometer back.

# 	if mileage >= self.odometer_reading:
# 		self.odometer_reading = mileage
# 	else:
# 		print("You can't roll back an odometer!")



	#Incrementing an Attribute’s Value Through a Method

# 	class Car:
# --snip--
# 	def update_odometer(self, mileage):
# --snip--
# 	def increment_odometer(self, miles):
		#Add the given amount to the odometer reading.
# 		self.odometer_reading += miles

# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()



