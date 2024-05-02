# escaping sequences

# \n --- new line
# \\ --- backslash
# \t --- tab (8 character space)
# \' --- single quote
# \"" --- double quote


# print('he said \'hey julian\'')


# STRING FORMATTING

# %s ---- for string
# %d ---- for decimal


# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)

radius = 10
pi = 3.14
area = pi * radius ** 2

# formatted_string = 'Circle with  %d gives of an area of %f' %(radius,area)
# print(formatted_string)

#in PYTHON 3.x
# formatted_string = f"A circle with {radius} give of a circle with {area}"
# print(formatted_string)
language = 'Python'

# print(len(language))
# print(language[-1])
# print(language[5])
# print(language[0:3])
# print(language[-3:])  # the last three characters
# print(language[3:])  # the last three characters

name = "arsanyos"
# skipping characters while slicing
# print(name[0:len(name):4])
# reversing a string
# print(name[-2:])
# capitalize
# print(name.capitalize())
# count the number of characters existing within a string
# print(name.count('a'))
# endswith(): Checks if a string ends with a specified ending
# print(name.endswith('ui'),'ui')
# print(name.endswith('os'),'os')
# find(): Returns the index of the first occurrence of a substring, if not found returns -1
print(name.find('s'))
# rfind() : Returns the index of the last occurrence of a string, if not found returns -1
print(name.rfind('s'))
#index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
print(name.index('yos'))
#rIndex() : Returns the highest index of the substring





