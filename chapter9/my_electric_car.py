#Inheritance
	
	#The __init__() Method for a Child Class

#Storing Multiple Classes in a Module

# class Car:
# #A simple attempt to represent a car.
# 	def __init__(self, make, model, year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		long_name = f"{self.year} {self.make} {self.model}"
# 		return long_name.title()

# 	def read_odometer(self):
# 		print(f"This car has {self.odometer_reading} miles on it.")

# 	def update_odometer(self, mileage):
	
# 		if mileage >= self.odometer_reading:
# 			self.odometer_reading = mileage
# 		else:
# 			print("You can't roll back an odometer!")

# 	def increment_odometer(self, miles):
# 		self.odometer_reading += miles

class ElectricCar(Car):
	#Represent aspects of a car, specific to electric vehicles.
	def __init__(self, make, model, year):
	#Initialize attributes of the parent class.
		super().__init__(make, model, year)



#in a different doc
# from car import ElectricCar
# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

#results
# 2019 Tesla Model S
# This car has a 75-kWh battery.
# This car can go about 260 miles on a full charge.



	#Overriding Methods from the Parent Class

# class ElectricCar(Car):
# --snip--
	# def fill_gas_tank(self):
		#Electric cars don't have gas tanks.
		# print("This car doesn't need a gas tank!")


	#Instances as Attributes

# class Car:
# --snip--
# class Battery:
# """A simple attempt to model a battery for an electric car."""
# 	def __init__(self, battery_size=75):
# 	"""Initialize the battery's attributes."""
# 		self.battery_size = battery_size

# 	def describe_battery(self):
# 	"""Print a statement describing the battery size."""
# 		print(f"This car has a {self.battery_size}-kWh battery.")

# 	class ElectricCar(Car):
# 	"""Represent aspects of a car, specific to electric vehicles."""
	
# 	def __init__(self, make, model, year):
# 		
# 		#Initialize attributes of the parent class.
# 		#Then initialize attributes specific to an electric car.
# 		
# 		super().__init__(make, model, year)
# 		self.battery = Battery()

# my_tesla = ElectricCar('tesla', 'model s', 2019)

# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()



#Get Range and init


# class Car:
# 	def __init__(self, make, model, year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# class Battery:
# 	def __init__(self, battery_size=75):
# 		self.battery_size = battery_size

# 	def get_range(self):
# 		if self.battery_size == 75:
# 			range = 260
# 		elif self.battery_size == 100:
# 			range = 315
# 		print(f"This car can go about {range} miles on a full charge.")

# class ElectricCar(Car):
# 	def __init__(self, make, model, year):
#  		super().__init__(make, model, year)
#  		self.battery = Battery()

# my_tesla = ElectricCar('tesla', 'models', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


