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
Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five
names, and use them as keys in your dictionary. Think of a favorite number for each person,
and store each as a value in your dictionary. Print each person’s name and their favorite
number. For even more fun, poll a few friends and get some actual data for your program.


#6.3 Glossary 1
Glossary: A Python dictionary can be used to model an actual dictionary. However, to
avoid confusion, let’s call it a glossary.
Think of five programming words you’ve learned about in the
previous chapters. Use these words as the keys in your glossary,
and store their meanings as values.
Print each word and its meaning as neatly formatted output. You
might print the word followed by a colon and then its meaning, or
print the word on one line and then print its meaning indented on
a second line. Use the newline character (\n) to insert a blank line
between each word-meaning pair in your output.


#6.4 Glossary 2
Now that you know how to loop through a dictionary, clean up the code from
Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through
the dictionary’s keys and values. When you’re sure that your loop works, add five more Python
terms to your glossary. When you run your program again, these new words and meanings
should automatically be included in the output.


#6.5 
Rivers: Make a dictionary containing three major rivers and the country each river runs
through. One key-value pair might be 'nile': 'egypt'.
Use a loop to print a sentence about each river, such as The Nile
runs through Egypt.
Use a loop to print the name of each river included in the
dictionary.
Use a loop to print the name of each country included in the
dictionary.


#6.6 Poll
 Polling: Use the code in favorite_languages.py (page 97).
Make a list of people who should take the favorite languages poll.
Include some names that are already in the dictionary and some
that are not.
Loop through the list of people who should take the poll. If they
have already taken the poll, print a message thanking them for
responding. If they have not yet taken the poll, print a message
inviting them to take the poll.

#6.7
 People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new
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
    "": []
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
        ''
    }
    'mumbai': {
        'country': 'india',
        ''
    }
    ''
}
Create a dictionary of information about each city and include the country that the
city is in, its approximate population, and one fact about that city. The keys for each city’s
dictionary should be something like country, population, and fact. Print the name of each
city and all of the information you have stored about it.


#6.12 Extensions: 
# Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.



