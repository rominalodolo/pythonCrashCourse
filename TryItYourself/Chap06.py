#6-1 
person1 = {'first_name': 'romina', 'last_name': 'lodolo', 'age': 27, 'city': 'Johannesburg'}

print(f"Name: {person1['first_name'].title()}, Surmame: {person1['last_name'].title()}, Age: {person1['age'].title()}, City: {person1['city'].title()}.")

#OR 
#person1 = {'first_name': 'romina', 'last_name': 'lodolo', 'age': 27, 'city': 'Johannesburg'}
#print(f"NAME: {person1['first_name'].title()},")
#print(f"SURNAME: {person1['last_name'].title()},")
#print(f"AGE: {person1['age'].title()},")
#print(f"CITY: {person1['city'].title()},")

#OR

#person1 = {'first_name': 'romina', 'last_name': 'lodolo', 'age': 27, 'city': 'Johannesburg'}

#print(f"NAME: {person1['first_name'].title()},")
#print(f"SURNAME: {person1['last_name'].title()},")
#print(f"AGE: {person1['age'].title()},")
#print(f"CITY: {person1['city'].title()},")

#person1['email'] = 'jwiky@yahoo.com'
#person1['male'] = True

#print(f"EMAIL: {person1['email']}")
#print(f"MALE: {person1['male']}")

#person1['age'] = 30

#print(person1)


# Another Example 

#people = {
#   'first_name': 'romina', 'last_name': 'lodolo', 'age': 27, 'city': 'johannesburg'
#   'first_name': 'jess', 'last_name': 'latley', 'age': 29, 'city': 'pretoria'
#}

#person1 = details['romina'].title()
#print(f"Name: {person1['first_name'].title()}, Surmame: {person1['last_name'].title()}, Age: {person1['age'].title()}, City: {person1['city'].title()},)
#print(f"Name: {person1['first_name'].title()}, Surmame: {person1['last_name'].title()}, Age: {person1['age'].title()}, City: {person1['city'].title()},)


#6.2 Favorite Numbers

favorite_numbers = {
    'romi': 6,
    'ky': 40,
    'sal': 1,
    'dan': 200_192,
    'fran': -1,
    }

num = favorite_numbers['romi']
print(f"Romi's favorite number is {num}.")

num = favorite_numbers['ky']
print(f"Ky's favorite number is {num}.")

num = favorite_numbers['sal']
print(f"Sal's favorite number is {num}.")

num = favorite_numbers['dan']
print(f"Dan's favorite number is {num}.")

num = favorite_numbers['fran']
print(f"Fran's favorite number is {num}.")


#6.3 Glossary 1
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")



#6.4 Glossary 2
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")



#6.5 Rivers
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")


#6.6 Poll
favorite_languages = {
    'romi': 'react',
    'kay': 'java',
    'eli': 'c#',
    'craig': 'sql',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

coders = ['craig', 'josh', 'david', 'becca', 'romi', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"{coder.title()}, what's your favorite programming language?")


#6.7 People
Start with the program you wrote for Exercise 6-1 (page 99). Make two new
dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people. As you loop through the list, print everything you know
about each person.


#6.8 Pets
Make several dictionaries, where each dictionary represents a different pet. In each
dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list
called pets. Next, loop through your list and as you do, print everything you know about each
pet.


#6.9 Favorite Places: 
favorite_places = {
    "romi": ["hydrabad", "gozo", "mykonos"],
    "sally": ["paris", "cape town"],
    "john": ["new york", "jburg"]
    }
for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")


#6.10 Favorite Numbers: 
Modify your program from Exercise 6-2 (page 99) so each person
can have more than one favorite number. Then print each person’s name along with their
favorite numbers.

 
#6.11 Cities: 
cities = {
    'jefferys bay': {
        'country': 'south africa',
        'population': '27 thousand',
        'fact': 'it is the best surfing destination',
    },
    'mumbai': {
        'country': 'india',
        'population': '20.4 million',
        'fact': 'it is also known as bombay',
    },
    'selima': {
        'country': 'malta',
        'population': '22 thousand',
        'fact': 'it is known as a resort town',
    }
}
for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    facts = city_info['fact'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population} people.")
    print(f"  A fun fact is that {facts}.")

#6.12 Extensions: 
# Use one of the example programs from this chapter
# extend it by adding new keys and values, changing the context of the program 
# or improving the formatting of the output.



