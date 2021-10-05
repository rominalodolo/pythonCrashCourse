#A Dictionary in a Dictionary

users = {
'aeinstein': {
	'first': 'albert',
	'last': 'einstein',
	'location': 'princeton',
	},
'mcurie': {
	'first': 'marie',
	'last': 'curie',
	'location': 'paris',
	},
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")


#Another example 

cars = {
'BMW': {
	'type': 'convertable',
	'model': 'M4',
	'year': 2016,
	},
'JEEP': {
	'type': 'wrangler',
	'model': 'sport',
	'year': 2015,
	},
}

for carBrand, car_info in cars.items():
	print(f"\ncarBrand: {carBrand}")
	specs = f"{car_info['type']} {car_info['model']}"
	year = car_info['year']
	print(f"\tSpecs: {specs.title()}")
	print(f"\tYear: {year}")
