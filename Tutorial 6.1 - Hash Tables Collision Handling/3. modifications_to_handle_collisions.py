#I know that theoretically we should be using Linked Lists as our Data Structure to store multiple
#key-value pairs of the same hash/index, but in this tutorial, we will be using Array/Lists Data
#Structures instead (cuz laze to re-implement the full Linked List Data Structure for this Hash Table
#Collision Handling tutorial)

class HashTable:
    def __init__(self):
        self.MAX = 10
        #Instead of initialising each element as 'None', we need to initialise each element as an
        #empty array/list '[]' (we will use an array/list for this tutorial instead of a Linked List at 
        #each index for this tutorial (it works too so we don't have to re-implement Linked Lists))
        self.arr = [[] for i in range(self.MAX)]

    #The hash function (no modifications needed here)
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    

    #Before:
    # def __setitem__(self, key, value):
    #     hash = self.get_hash(key)
    #     self.arr[hash] = value

    #With modifications in the '__setitem__' function:
    def __setitem__(self, key, value):
        hash = self.get_hash(key)

        found = False

        #About Python's 'enumerate()' function: 
        #Refer to '3.5 explaining_enumerate_function.py'

        #I believe we need to add 'enumerate()' here not because of its counter function, but so we can
        #access both the Tuple element index location (with 'index' parameter), as well as each index 
        #(with 'element' parameter) within the Tuple element
        for index, element in enumerate(self.arr[hash]):
            
            #We first need to check and consider the case if the item you want to set (effectively edit/change) 
            #already exists in the Hash Table. If it exists, we simply reset that Tuple's (that contains the key 
            #of the key-value pair we want to edit) value (but since its a Tuple we need to reset the whole Tuple
            #even though the key is the same)
            if len(element) == 2 and element[0] == key:

                #At that particular index in the list in the particular hash/index memory array of the
                #Hash Table, set the new key-value pair as a Tuple. Since Tuples are immutable, you can't
                #just solely reset the value (element[1] = value), you need to replace the whole Tuple (with 
                #the same key but different value)
                self.arr[hash][index] = (key, value)
                found = True
                break

        #If the key-value pair you want to set is new (dosen't yet exist in the Hash Table), we append a new
        #key-value pair Tuple to the array/list at its particular hash/index
        if not found:
            self.arr[hash].append((key, value))


    #Before:
    #def __getitem__(self, key):
    #    hash = self.get_hash(key)
    #    return self.arr[hash]

    #With modifications in the '__getitem__' function:
    #What we're trying to do here is to get an item we need to first find the hash/index of the key-value
    #pair from its key in the Hash Table's memory array, then, of the hash/index's list at its location, 
    #Linearly Search through that list to find the key in that list (which will always be the first
    #element of the Tuple elements)
    def __getitem__(self, key):
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if len(element) == 2 and element[0] == key:
                return element[1]
        return 'There is no such key-value pair!'
    

    #Before:
    #def __delitem__(self, key):
    #    hash = self.get_hash(key)
    #    self.arr[hash] = None

    #With modifications in the '__delitem__' function:
    #What we're trying to do here is to delete an item we need to similarly first find the hash/index of
    #the key-value pair from its key in the Hash Table's memory array, then, of the hash/index's list at
    #its location, Linearly Search through that list to find the key in that list (which will always be 
    #the first element of the Tuple elements), then delete the Tuple that contains that key
    def __delitem__(self, key):
        hash = self.get_hash(key)
        for index, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                del self.arr[hash][index]
                return True 
        return 'There is no such key-value pair!'
    

if __name__ == '__main__':
    samplehashtable = HashTable()

    print(samplehashtable.get_hash('march 6'))
    print(samplehashtable.get_hash('march 17'))

    #__setitem__
    samplehashtable['march 6'] = 310
    samplehashtable['march 6'] = 110
    samplehashtable['march 8'] = 380
    samplehashtable['march 9'] = 302
    samplehashtable['march 17'] = 450

    #__getitem__
    print(samplehashtable['march 79'])
    print(samplehashtable['march 6'])
    print(samplehashtable['march 17'])

    #__delitem__
    # del samplehashtable['march 9']
    # del samplehashtable['march 6']
    print(samplehashtable.arr)



    

    