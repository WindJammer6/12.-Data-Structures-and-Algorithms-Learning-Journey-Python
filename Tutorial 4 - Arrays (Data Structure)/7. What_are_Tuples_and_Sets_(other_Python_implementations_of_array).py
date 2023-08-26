#A Set is another Python's implementation of a Dynamic array, but with some differences with Lists 
#(the more commonly used Python's implementation of a Dynamic array).

#A Tuple is Python's implementation of a Static array.


#/////////////////////////////////


#Lists VS Sets VS Tuples:

#Dynamic Array or Static Array/Mutable or Immutable (Dynamic/Mutable means size of Data Structure can 
#grow/shrink, Static/Immutable means size of the Data Structure is fixed):
#Lists is Dynamic/Mutable
#Set is Dynamic/Mutable
#Tuple is Static/Immutable

#Changing items in the Data Structure:
#Items in a List can be replaced or changed
#Items in a Set cannot be changed or replaced
#Items in a Tuple cannot be changed or replaced

#Duplicate elements/items:
#List allows duplicates
#Set dosen't allow duplicates
#Tuple allows duplicates

#Allow or dosen't allow Indexing/Slicing (when you do the '[ : ]' operator, its called 
#slicing) / Ordered or Unordered:
#List allows indexing/slicing / is an Ordered collection of items
#Set dosen't allow indexing/slicing / is an Unordered collection of items
#Tuple allows indexing/slicing / is an Ordered collection of items


#/////////////////////////////////


#This is how you define/declare a List (using square brackets '[]')
this_is_a_list = ['tom', 'jerry', 'billy']
print(this_is_a_list)

#This is how you define/declare a Set (using curly brackets '{}' (same symbol as Dictionaries))
this_is_a_set = {'tom', 'jerry', 'billy'}
print(this_is_a_set)                    #Order of items printed in a Set may vary everytime you run the code
                                        #since a Set Data Structure stores unordered items/elements/data

#This is how you define/declare a Tuple (using parenthesis '()')
this_is_a_tuple = ('tom', 'jerry', 'billy')
print(this_is_a_tuple)


#Proof if the Lists and Sets are Dynamic/Mutable, and Tuples are Static/Immutable:
#(you can play around using various Python functions to verify the properties of the List/Set/Tuple Data Structures
#listed above, such as trying to add duplicates into a Set to see if it accepts duplicates (which it shouldn't))
this_is_a_list.append("sam")
this_is_a_list.insert(1, "jimmy")
print(this_is_a_list)

this_is_a_set.add("sam")
print(this_is_a_set)

#mytuple.insert(1, 'sam')               #If you try to grow the Tuple by inserting an element,
                                        #the computer program will give you an error since a Tuple is
                                        #static/immutable