#Using the range() Function
for value in range(1, 5):
	print(value)


#Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)



#Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
