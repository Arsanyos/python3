
# list  : collection of ordered (modifiable) items
# tuple : collection of ordered (unmodifiable) items
# set   : collection of unordered , unindexed and unmodifiable items
# dictionary : just like objects in javascript



# weird how we can access the opposite side of LIST using negative indices 
# ------------
# lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] 
# print(type(lst[-1]))
# ------------
# lst.pop()   ------ removes the last item from the list and returns the popped item
# print(lst.pop())
# print(lst)
# lst.clear() clears a list

positive_number = [1,2,3]
zero = [0]
negative_number = [-1,-2,-3]

print(positive_number.count(8))

# negative_number.extend(zero)
# negative_number.extend(positive_number)
# print(negative_number)