#What does Python's 'enumerate()' function do?
#The enumerate function in Python converts a data collection object into an enumerate object. Enumerate 
#returns an object that contains a counter as a key for each value within an object, making items within 
#the collection easier to access.

#Definition and Usage:
#-> The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
#-> The enumerate() function adds a counter as the key of the enumerate object.

#Syntax:
#enumerate(iterable, start)

#-> 'iterable'	parameter - An iterable object
#-> 'start' parameter - A Number. Defining the start number of the enumerate object. Default 0

#This file is just a messy attempt to understand Python's 'enumerate()' function. You can run this file to
#see the output of the code
#1. 
my_list = ["apples", "pears", "orange", "apples", "watermelon", "apples", None, "apples"]

for count, element in enumerate(my_list, 100):
    print(count, element)

#2.
my_list2 = ('apple', 'banana', 'cherry')
y = enumerate(my_list2)
for count, element in enumerate(my_list2, 100):
    print(count, element)

print(list(y))

#3.
z = 'geek'
a = list(z)
b = enumerate(z)
c = enumerate(a)
print(list(b))
print(list(c))

#4.
elephant = 'elephant'
list = []
for char in elephant:
    list.append(char)

print(list)

for count, element in enumerate(list):
    print(count, element)
