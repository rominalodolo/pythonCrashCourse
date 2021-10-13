#Reading from a File

	#remove the extra blank line, you can use rstrip() in the call to print()
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents.rstrip())

