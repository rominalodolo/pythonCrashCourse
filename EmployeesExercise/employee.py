class Employee:
	def __init__(self, firstName, lastName, ID, email, address):
		self.firstName = firstName
		self.lastName = lastName
		self.ID = ID
		self.email = email
		self.address = address

	def displayInfo(self):
		if (self.department):
			print (f"\n Name: {self.firstName} {self.lastName}")
			print (f"\n ID Number: {self.ID}")
			print (f"\n Email: {self.email}")
			print (f"\n Address: {self.address}")
		else:
			print (f"\n Name: {self.firstName} {self.lastName}")
			print (f"\n ID Number: {self.ID}")
			print (f"\n Email: {self.email}")
			print (f"\n Department: Unknown")

	def changeEmail(self,newEmail):
		self.email = newEmail