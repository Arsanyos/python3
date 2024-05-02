import math

#1.Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.


print(type(1))
print(type(3.14))
print(type(2+4j))
print(type('30 Days of Python'))
print(type(False))
print(type(['1','2','4']))
print(type({"name":"Arsanyos"}))
print(type((1,"asd")))
print(type({1,3,"4"}))

#2.Find an Euclidian distance between (2, 3) and (10, 8)

coordinate_1 = (2,3)
coordinate_2 = (10,8)

euclidian_distance = math.sqrt((coordinate_2[1]-coordinate_1[1])**2 + (coordinate_2[0]-coordinate_2[0])**2)

print('The Euclidian Distance is',euclidian_distance )