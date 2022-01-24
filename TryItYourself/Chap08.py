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
Start with your program from Exercise 8-7. Write a while loop that allows
users to enter an album’s artist and title. Once you have that information, call make_album()
with the user’s input and print the dictionary that’s created. Be sure to include a quit value in
the while loop.


#8.9 Messages: 
Make a list containing a series of short text messages. Pass the list to a function
called show_messages(), which prints each text message.


#8.10 Sending Messages: 
Start with a copy of your program from Exercise 8-9. Write a
function called send_messages() that prints each text message and moves each message to a
new list called sent_messages as it’s printed. After calling the function, print both of your lists
to make sure the messages were moved correctly.


#8.11 Archived Messages: Start with your work from Exercise 8-10. Call the function
send_messages() with a copy of the list of messages. After calling the function, print both of
your lists to show that the original list has retained its messages.


#8.12 Sandwiches: 
Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call
provides, and it should print a summary of the sandwich that’s being ordered. Call the function
three times, using a different number of arguments each time.


8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a profile of
yourself by calling build_profile(), using your first and last names and three other key-value
pairs that describe you.


# 8.14 Cars: 
Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. It should then accept an arbitrary
number of keyword arguments. Call the function with the required information and two other
name-value pairs, such as a color or an optional feature. Your function should work for a call
like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that’s returned to make sure all the information was stored correctly.


8-15. Printing Models: Put the functions for the example printing_models.py in a separate file
called printing_functions.py. Write an import statement at the top of printing_models.py, and
modify the file to use the imported functions.

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

