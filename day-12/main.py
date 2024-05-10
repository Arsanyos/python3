# import myModules

# myModules.say_hi()

# in-built modules

from statistics import *
import string
# collection = [1,2,3,4]
# print(mean(collection))

import random
import string

# def random_user_id(k,itr):
#     user_ids =[]
#     for i in range(itr):
#         user_id ="".join(random.choices(string.ascii_lowercase + string.digits, k=k))
#         user_ids.append( user_id)
#         print()
#     return user_ids

# print(random_user_id(6,2))

def generate_colors(type,k):
    color = "#" + "".join(random.choices(string.ascii_lowercase + string.digits , k=k))
    print(color)

generate_colors('#', 5) #