#Positional Arguments

def describe_pet(animal_type, pet_name):
#Display information about a pet.
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') #order of positional arguments is NB 


#Multiple Function Calls

def describe_pet(animal_type, pet_name):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'sweetie')



def describe_pet(animal_type, pet_name):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')


#Keyword Arguments

def describe_pet(animal_type, pet_name):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

#the order doesnt matter it will still assign the right values 



#Default Values

def describe_pet(pet_name, animal_type='dog'): #defult value is always last
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')



#Equivalent Function Calls

def describe_pet(pet_name, animal_type='dog'):

	# A dog named Willie. equivelint values are the same result 
describe_pet('willie')
#OR
describe_pet(pet_name='willie') 

# A hamster named Harry.
describe_pet('harry', 'hamster')
#OR 
describe_pet(pet_name='harry', animal_type='hamster')
#OR
describe_pet(animal_type='hamster', pet_name='harry')
#order doesnt matter


#Avoiding Argument Errors
def describe_pet(animal_type, pet_name):
"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()

