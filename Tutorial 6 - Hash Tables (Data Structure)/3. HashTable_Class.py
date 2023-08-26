#The 'HashTable' object represents the overall Hash Table Data Structure. 

#It has 2 attributes:
#'MAX', which sets the size of the array/list being created in contiguous memory (though the order which
#the values in our 'key-value' pairs are stored may not be continuous, based on the index produced by the
#hash function for each key in our 'key-pair' values, which determines the location where the value will
#be stored in the memory in the array/list) which serves as the database where all our values in the 
#'key-value' pairs will be stored

#'arr', which is the array/list itself being created in contiguous memory which serves as the database 
#where all our values in the 'key-value' pairs will be stored in our 'HashTable' object. 

class HashTable:
    def __init__(self):
        self.MAX = 100
        #This attribute is impemented via this code, which creates an array of size given by the first 
        #attribute, 'MAX' which in this case, is 100. Hence 'HashTable' objects created in this class
        #will be allocated contiguous memory size (filled with None at first) of 100.
        self.arr = [None for i in range(self.MAX)]
