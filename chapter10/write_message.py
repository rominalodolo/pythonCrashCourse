#Writing to an Empty File

filename = 'programming.txt'

with open(filename, 'a') as file_object:
	file_object.write("I love programming.")
	file_object.write("Yolo.")


	#read mode ('r'), write mode ('w'), append mode ('a')
	#build command and watch the programing.txt grow 