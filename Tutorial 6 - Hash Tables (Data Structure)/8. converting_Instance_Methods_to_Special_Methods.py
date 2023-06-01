class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    #The hash function
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    #Here are the renaming changes made to these Instance Methods. Initially they were:
    #-> add_key_value_pair_into_Hash_Table(self, key, value)
    #-> get_value_from_key(self, key)
    #-> delete_key_value_pair_from_Hash_Table(self, key)

    #Recall from the OOP Learning, Special Methods are:
    #Special Methods are a set of predefined methods you can use to enrich your classes. They let you 
    #emulate the behavior of built-in (existing) types in your own-made Classes and to implement Operator
    #Overloading. Here are some examples:
    #-> __init__
    #-> __repr__
    #-> __str__ 
    #-> __add__

    #In this tutorial, we will be making use of 3 other Special Methods which can be found in the Python
    #Documentations. They are:
    #-> __setitem__: this is a method used for assigning a value to an item. It is implicitly invoked
    #                when we set a value to an item of a list, dictionary, etc. 
    #-> __getitem__: this is a method used for getting the value of an item. It is implicitly invoked 
    #                when we access the items of a list, dictionary, etc. 
    #-> __delitem__: this is a method used for the deletion of self[key]. When you call del self[key], 
    #                Python will call self.__delitem__(key).

    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        self.arr[hash] = value

    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None
    

#Now that we have made the changes to our above code and did Operator Overloading to pre-existing built-in
#functions in Python by explicitly defining them in the above Special Methods, we can call these Operator
#like as they are in Python instead of calling them like lengthy self-defined functions
if __name__ == '__main__':
    samplehashtable = HashTable()
    print(samplehashtable.get_hash('march 6'))
    print(samplehashtable.get_hash('march 17'))
    print(samplehashtable.get_hash('december 17'))

    #Before (to add a key value pair):
    #samplehashtable.add_key_value_pair_into_Hash_Table('march 6', 310)

    #Now:
    samplehashtable['march 6'] = 310
    samplehashtable['march 1'] = 20
    samplehashtable['december 17'] = 300

    
    print(samplehashtable.arr)


    #Before (to get a value of a key when providing the key):
    #print(samplehashtable.get_value_from_key('march 6'))

    #Now:
    print(samplehashtable['march 1'])
    print(samplehashtable['march 20'])      #Error proof to make sure it shows none since this key dosen't
                                            #exist


    #Before (to delete a key-value pair):
    #samplehashtable.delete_key_value_pair_from_Hash_Table('march 6')

    #Now:
    del samplehashtable['march 6']
    print(samplehashtable.arr)
    



    

    