#CLASSES

		#Creating and Using a Class

	#Creating the Dog Class

class Dog:
#A simple attempt to model a dog.

	def __init__(self, name, age, breed): #init means initialize 
		#Initialize name and age attributes.
		self.name = name
		self.age = age
		self.breed = breed
	def sit(self): #def means definition
		#Simulate a dog sitting in response to a command.
		print(f"{self.name} is now sitting.")
	def roll_over(self):
		#Simulate rolling over in response to a command.
		print(f"{self.name} rolled over!") 

#follow code at line 35 


# class Dog:
# --snip--
# ➊ my_dog = Dog('Willie', 6)
# ➋ print(f"My dog's name is {my_dog.name}.")
# ➌ print(f"My dog is {my_dog.age} years old.")



#Making an Instance from a Class

my_dog = Dog('Sweetie', 6, 'Husky')

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

	#Accessing Attributes

	#Calling Methods
my_dog.sit()



#Creating Multiple Instances

# class Dog:

# 	def __init__(self, name, age): #init means initialize 
# 		#Initialize name and age attributes.
# 		self.name = name
# 		self.age = age
# 	def sit(self): #def means definition
# 		#Simulate a dog sitting in response to a command.
# 		print(f"{self.name} is now sitting.")
# 	def roll_over(self):
# 		#Simulate rolling over in response to a command.
# 		print(f"{self.name} rolled over!") 

# my_dog = Dog('Sweetie', 6)
# your_dog = Dog('Lucy', 3)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
# my_dog.roll_over()

# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()
# your_dog.roll_over()
