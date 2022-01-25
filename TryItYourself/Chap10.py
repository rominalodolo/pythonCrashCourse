#10.3 Guest
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)


#10.4 Guest Book
Write a while loop that prompts users for their name. When they enter
their name, print a greeting to the screen and add a line recording their visit in a file called
guest_book.txt. Make sure each entry appears on a new line in the file.


#10.5 Programming Poll

Write a while loop that asks people why they like programming.
Each time someone enters a reason, add their reason to a file that stores all the responses.

10-6. Addition: One common problem when prompting for numerical input occurs when
people provide text instead of numbers. When you try to convert the input to an int, you’ll get
a ValueError. Write a program that prompts for two numbers. Add them together and print
the result. Catch the ValueError if either input value is not a number, and print a friendly error
message. Test your program by entering two numbers and then by entering some text instead
of a number.
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user
can continue entering numbers even if they make a mistake and enter text instead of a number.
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in
the first file and three names of dogs in the second file. Write a program that tries to read these
files and print the contents of the file to the screen. Wrap your code in a try-except block to
catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the
files to a different location on your system, and make sure the code in the except block
executes properly.
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if
either file is missing.
10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/) and find a few texts
you’d like to analyze. Download the text files for these works, or copy the raw text from your
browser into a text file on your computer.
You can use the count() method to find out how many times a word or phrase appears in a
string. For example, the following code counts the number of times 'row' appears in a string:
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches all appearances of the
word you’re looking for, regardless of how it’s formatted.
Write a program that reads the files you found at Project Gutenberg and determines how
many times the word 'the' appears in each text. This will be an approximation because it will
also count words such as 'then' and 'there'. Try counting 'the ', with a space in the string,
and see how much lower your count is.


10-11. Favorite Number: Write a program that prompts for the user’s favorite number. Use
json.dump() to store this number in a file. Write a separate program that reads in this value
and prints the message, “I know your favorite number! It’s _____.”

#10.12 Favorite Number Remembered: Combine the two programs from Exercise 10-11
into one file. If the number is already stored, report the favorite number to the user. If not,
prompt for the user’s favorite number and store it in a file. Run the program twice to see that it
works.


# 10.13 Verify User: 

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return
            
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")

greet_user()

The final listing for remember_me.py assumes either that the user has
already entered their username or that the program is running for the first time. We should
modify it in case the current user is not the person who last used the program.
Before printing a welcome back message in greet_user(), ask the user if this is the correct
username. If it’s not, call get_new_username() to get the correct username.

