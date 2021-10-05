#The if-elif-else Chain

age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission cost is $40.")


#IDLE console 
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
print(f"Your admission cost is ${price}.")

#OR
age = 12
price = 0

if age < 4:
	price = 0 
	print(f"Your admission cost is ${price}.")
elif age < 18:
	price = 25
	print(f"Your admission cost is  ${price}.")
else:
	price = 40
	print(f"Your admission cost is ${price}.")




#Using Multiple elif Blocks in Console IDLE

age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20
print(f"Your admission cost is ${price}.")


#Omitting the else Block

age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20
print(f"Your admission cost is ${price}.")
