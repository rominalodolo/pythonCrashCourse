#Tuples

dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

#what not to do 
#dimensions = (200, 50)
#dimensions[0] = 250


#Writing over a Tuple

dimensions = (200, 50)

print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

#treats it like a new tuple 
dimensions = (400, 100)
print("\nModified dimensions:")

for dimension in dimensions:
	print(dimension)

