person1 = {
   'first_name': 'romina', 'last_name': 'lodolo', 'age': 27, 'city': 'johannesburg'
   }

person2 ={
   'first_name': 'jess', 'last_name': 'latley', 'age': 29, 'city': 'pretoria'
}

details = person1['first_name'].title()
print(f"Persons name is {details}")


details2 = person2.get('age', 'UNDIFINED')
print(details2)


details3 = person2.get('zodiac', 'UNDIFINED')
print(details3) 

# print('\nKey-Value Pairs:')
# for k, v in person1.items():
#	print(f"\t{k}: {v}")

# print('\nValues:')
# for v in person1.values():
#	print(f"\t {v}")

# print('\nKeys:')
# for k in person1.keys():
#	print(f"\t {k}")
