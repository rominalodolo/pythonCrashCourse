from random import randint 

print("Welcome to the Guessing Game...")
print("I have selected a number between 1 and 5.")

number = randint(1,5) 
guess = attempts = 0
while attempts < 2:
    guess = int(input("Enter a guess: "))
    if guess == number: 
        break
    attempts += 1

if guess != number:
    print(f"Original number was {number}")
else:
    print("You Win!")
