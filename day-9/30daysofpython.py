# conditionals 
# GRADING USING IF CONDITION

# result = 20

# if result > 85:
#          print('A')
# elif result > 70 and result < 90:
#         print('B') 
# elif result > 60 and result < 70:
#         print('C')
# elif result > 50 and result < 60:
#         print('Accepting oneself is sometimes the key to success')
# else:
#         print('God damn maybe accepting oneself may not be a solution for you')


fruits = ['banana', 'orange', 'mango', 'lemon']

item_to_check = 'avocado'

if item_to_check in fruits:
        print('Fruits is already in cart')
else:
        fruits.append(item_to_check)
        
print('Updated fruits list',fruits)