#15
class Person:
	def __init__(self, firstName, lastName, age, email, middleName=''):
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.email = email
		self.middleName = middleName

	def displayInfo(self):
		if (self.middleName):
			print (f"\n Name: {self.firstName} {self.middleName} {self.lastName}")
			print (f"\n Age: {self.age}")
			print (f"\n Email: {self.email}")
		else:
			print (f"\n Name: {self.firstName} {self.lastName}")
			print (f"\n Age: {self.age}")
			print (f"\n Email: {self.email}")



#16
personOne = Person('Romina', 'Lodolo', 27, 'lodoloromina@gmail.com', 'Bianca')
personTwo = Person('Sally', 'Door', 30, 'sallydoor@hotmail.com')

personOne.displayInfo()
personTwo.displayInfo()