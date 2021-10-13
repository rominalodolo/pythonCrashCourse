from employee import Employee

class Sales(Employee):
	def __init__(self, firstName, lastName, ID, email, role, salary, address):
		super().__init__(firstName, lastName, ID, email, address)
		self.role = role 
		self.salary = salary

	def displayInfo(self):
		if (self.address): 
			print(f"Name: {self.firstName} {self.lastName}")
			print(f"ID: {self.ID}")
			print(f"Email: {self.email}")
			print(f"Address: {self.address}")
			print(f"Role: {self.role}")
			print(f"Salary: {self.salary}\n")
		else:
			print(f"Name: {self.firstName} {self.lastName}")
			print(f"ID: {self.ID}")
			print(f"Email: {self.email}")
			print(f"Role: {self.role}")
			print(f"Salary: {self.salary}\n")