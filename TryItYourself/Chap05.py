#5.1 Conditional Tests
Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
Look closely at your results, and make sure you understand why
each line evaluates to True or False.
Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False.

#5.2 
More Conditional Tests: You don’t have to limit the number of tests you create to ten.
If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have
at least one True and one False result for each of the following:
Tests for equality and inequality with strings
Tests using the lower() method
Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
Tests using the and keyword and the or keyword
Test whether an item is in a list
Test whether an item is not in a list


#5.3 Alien Colors 
# Imagine an alien was just shot down in a game.

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")


# no output version 
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")



#5.4 
# if 
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

# else 
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")



#5.5
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
If the alien is green, print a message that the player earned 5
points.
If the alien is yellow, print a message that the player earned 10
points.
If the alien is red, print a message that the player earned 15 points.
Write three versions of this program, making sure each message is
printed for the appropriate color alien.

#5.6

age = 27

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")


#5.7 Favorite Fruit
favorite_fruits = ['blueberries', 'mangos', 'strawberries']

if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'strawberries' in favorite_fruits:
    print("You really like strawberries!")


#5.8 Hello Admin: 

usernames = ['romi', 'sally', 'admin', 'tay', 'john']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

#5.9 No Users
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for loggin in again!")
else:
    print("We need to find some users!")


#5.10 Checking Usernames

current_users = ['romi', 'sally', 'admin', 'tay', 'John']
new_users = ['Bianca', 'Johah', 'Sally', 'kate', 'Irana']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")


#5.11 Ordinal Numbers
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")



#5.12 Styling if statements: 
# Review the programs you wrote in this chapter

#5.13 My Ideas:
# Think of some problems you could solve with your own programs.
# Record any new ideas you have about problems you might want to solve as your programming
# skills continue to improve. Consider games you might want to write, data sets you might want
# to explore, and web applications you’d like to create.