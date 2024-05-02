import math
# x = 12
# name = 'arslan'
# # ----------------------------------------
# # OR bit wise operator
# print(x | 6,"The OR bit wise operation")
# print(x & 6,"The AND bit wise operation")

# # AND bit wise operator
# # ----------------------------------------
# print(name is 1,"The is operator") # False
# print('a' in name,"The in operator") # True
# print(name is not 'arslan', 'The is not operator') # False
# print('k' not in name, 'The not in operator') # True
# # ----------------------------------------
# print(not( 2 > 1) or (3 == 5),"The not operator")

# # Exercise

# my_age = 24
# my_height = 1.85
# the_complex_number = 3 + 9j

# # Rectangle

# # width_of_rectangle = input('Enter the base: ')
# # height_of_rectangle  = input('Enter the height: ')

# # area_of_rectangle = int(width_of_rectangle) * int(height_of_rectangle)
# # print(area_of_rectangle,'area_of_rectangle')

# # Triangle Perimeter

# # side_a = input('Enter side a: ')
# # side_b = input('Enter side b: ')
# # side_c = input('Enter side c: ')

# # triangle_perimeter = int(side_a) + int(side_b) + int(side_c)
# # print(triangle_perimeter,"triangle_perimeter")

# # slope

# x1 = 2
# y1 = 2

# x2 = 6
# y2 = 10



# slope = (y2-y1) / (x2-x1)
# print(slope,"Slope of coordinates (2,2) , (6,10) ")

# # Falsy comparison

# print(len('python') > len('dragon'),'The Falsy comparison')

# # in and AND

# print('on' in 'python' and 'on' in 'dragon','on in python and dragon')
# print('jargon' in 'I hope this course is not full of jargon',"I do HOPE this course is not full of jargon")

# python_length = len('python')
# print(float(python_length),"To float")
# print(str(python_length),"To string")


# print(int(7 // 3) ==  int(2.7))

# print((math.ceil(float('9.8'))) == 10)

# print(float('9.8'))

# print(math.floor(9.8))

# year to seconds


def years_to_seconds(age):
    year_to_day = 365
    day_to_hour = 24
    hour_to_minute = 60
    minute_to_second = 60
    seconds_per_year = year_to_day * day_to_hour * hour_to_minute * minute_to_second
    return age*seconds_per_year

#
age = int(input('Enter the number of years you have lived'))
age_in_second = years_to_seconds(age)
print(age_in_second)
