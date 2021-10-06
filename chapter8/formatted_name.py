#Return Values 

	#Returning a Simple Value

def get_formatted_name(first_name, last_name):
#Return a full name, neatly formatted.
	full_name = f"{first_name} {last_name}"
	return full_name.title()
	
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


#Making an Argument Optional

def get_formatted_name(first_name, middle_name, last_name):
#Return a full name, neatly formatted.
	full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)



def get_formatted_name(first_name, last_name, middle_name=''):
#Return a full name, neatly formatted.
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
 #if you want to make one of the parameteres optional make it last
