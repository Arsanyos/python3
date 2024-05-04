# Dictionary 

mua ={
    'first_name':'Arsanyos',
    'last_name':'Asrat',
    'age':'24',
    'height':'185',
    'skills':['react','materialUI','typescript'],
    'address':{
        'country':'ethiopia',
        'city':'addis ababa'
    }
}

print((mua['first_name'])) # accessing a dictionary field
print(len(mua)) # length of dictionary
mua['key5'] = 'value5'

print('updated dictionary', mua)

# to remove an item
mua.pop('age') # remove a specific field from dictionary
mua.popitem() # remove the last element from the dictionary

# del mua # del removes the whole dictionary
# del mua
print(mua)
print(mua.clear())
mua['gender']='Male'
print((mua))
dct_copy = mua.copy()  # copy of a dictionary