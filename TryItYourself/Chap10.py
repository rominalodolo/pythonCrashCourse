#10.3 Guest
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)


#10.4 Guest Book
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name}, you've been added to the guest book.")



#10.5 Programming Poll

filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")

#10.6 Addition

try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("Sorry, I really needed a number.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")
    
One common problem when prompting for numerical input occurs when
people provide text instead of numbers. When you try to convert the input to an int, you’ll get
a ValueError. Write a program that prompts for two numbers. Add them together and print
the result. Catch the ValueError if either input value is not a number, and print a friendly error
message. Test your program by entering two numbers and then by entering some text instead
of a number.

#10.7 Addition Calculator: 
Wrap your code from Exercise 10-6 in a while loop so the user
can continue entering numbers even if they make a mistake and enter text instead of a number.
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in
the first file and three names of dogs in the second file. Write a program that tries to read these
files and print the contents of the file to the screen. Wrap your code in a try-except block to
catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the
files to a different location on your system, and make sure the code in the except block
executes properly.


#10.9 Silent Cats and Dogs
Modify your except block in Exercise 10-8 to fail silently if
either file is missing.


#10.10 Common Words
 Visit Project Gutenberg (https://gutenberg.org/) and find a few texts
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


#10.11 Favorite Number
Write a program that prompts for the user’s favorite number. Use
json.dump() to store this number in a file. Write a separate program that reads in this value
and prints the message, “I know your favorite number! It’s _____.”


#10.12 Favorite Number Remembered
Combine the two programs from Exercise 10-11
into one file. If the number is already stored, report the favorite number to the user. If not,
prompt for the user’s favorite number and store it in a file. Run the program twice to see that it
works.


# 10.13 Verify User: 
The final listing for remember_me.py assumes either that the user has
already entered their username or that the program is running for the first time. We should
modify it in case the current user is not the person who last used the program.
Before printing a welcome back message in greet_user(), ask the user if this is the correct
username. If it’s not, call get_new_username() to get the correct username.

