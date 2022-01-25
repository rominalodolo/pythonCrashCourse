#8.1 Message: 

from pydoc import text


def display_message():
    msg = "I'm learning about functions."
    print(msg)

display_message()


#8.2 Favorite Book: 

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")



#8.3 T-Shirt: 

def make_shirt(size, text):
    print(f"\nThe size of the shirt is {size}.")
    print(f"Message on the shirt, '{text}'.")

make_shirt('medium', 'Coding is fun!')
make_shirt(text="Blue Light Glasses are COOL", size='small')


#8.4 Large Shirts: 

def make_shirt(size='large', text='I love Python'):
    print(f"\nThe size of the T-shirt is {size}.")
    print(f'Message on the shirt, "{text}"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Coding is fun!')


#8.5 Cities: 

def describe_city(city, country='malta'):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('selima')
describe_city('reykjavik', 'iceland')
describe_city('birgu')


#8.6 City Names: 

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chile')
print(city)

city = city_country('pretoria', 'south africa')
print(city)

city = city_country('kolkata', 'india')
print(city)


#8.7 Album: 

Use None to add an optional parameter to make_album() that allows you to store the number
of songs on an album. If the calling line includes a value for the number of songs, add that value
to the album’s dictionary. Make at least one new function call that includes the number of
songs on an album.

def make_album(artist, title):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('nothing,nowhere.', 'trauma factory')
print(album)

album = make_album('jutes', 'careful what you wish for')
print(album)

album = make_album('vanessa hudgens', 'v')
print(album)


#8.8 User Albums
# Start with your program from Exercise 8-7. Write a while loop that allows
# users to enter an album’s artist and title. Once you have that information, call make_album()
# with the user’s input and print the dictionary that’s created. Be sure to include a quit value in
# the while loop.

def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")


#8.9 Messages: 
def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)
Make a list containing a series of short text messages. Pass the list to a function
called show_messages(), which prints each text message.


#8.10 Sending Messages: 
def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)

# Start with a copy of your program from Exercise 8-9. Write a
# function called send_messages() that prints each text message and moves each message to a
# new list called sent_messages as it’s printed. After calling the function, print both of your lists
# to make sure the messages were moved correctly.


#8.11 Archived Messages: 
# Start with your work from Exercise 8-10. Call the function
# send_messages() with a copy of the list of messages. After calling the function, print both of
# your lists to show that the original list has retained its messages.

def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)


#8.12 Sandwiches: 
# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call
# provides, and it should print a summary of the sandwich that’s being ordered. Call the function
# three times, using a different number of arguments each time.

def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')


# 8.13 User Profile 
# Start with a copy of user_profile.py from page 149. Build a profile of
# yourself by calling build_profile(), using your first and last names and three other key-value
# pairs that describe you.


# 8.14 Cars: 
# Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. It should then accept an arbitrary
# number of keyword arguments. Call the function with the required information and two other
# name-value pairs, such as a color or an optional feature. Your function should work for a call
# like this one:

# car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary that’s returned to make sure all the information was stored correctly.

def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)

# 8.15 Printing Models: 
# Put the functions for the example printing_models.py in a separate file
# called printing_functions.py. Write an import statement at the top of printing_models.py, and
# modify the file to use the imported functions.

printing_functions.py:

"""Functions related to printing 3d models."""

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
    
        # Simulate creating a 3d print from the design.
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
printing_models.py:

import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)



#8.16 Imports: 
Using a program you wrote that has one function in it, store that function in a
separate file. Import the function into your main program file, and call the function using each
of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *

# 8.17 Styling Functions: 
# Choose any three programs you wrote for this chapter
# make sure they follow the styling guidelines described in this section

