class HashTable:
    def __init__(self):
        #From this file onwards, we will be using a smaller array size in our Hash Tables to demonstrate 
        #Hash Table Collision Handling (from 100 to 10)
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    #The hash function
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        self.arr[hash] = value

    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None
    

if __name__ == '__main__':
    samplehashtable = HashTable()

    #As we can see from here, both 'march 6' and 'march 17' keys have the same hash/index of 9
    print(samplehashtable.get_hash('march 6'))
    print(samplehashtable.get_hash('march 17'))

    samplehashtable['march 6'] = 310
    samplehashtable['march 8'] = 380
    samplehashtable['march 9'] = 302
    samplehashtable['march 17'] = 450

    #Now lets printing the value of 'march 6' key. You should see 450 instead of 310. What happened here?
    #What heppened is that since 'march 6' and 'march 17' share the same hash/index (index 9), when 
    #'march 17' is appended, it's value overrided the existing 'march 6''s value (310) that was already 
    #currently in the memory array (since it was appended first before 'march 17''s key-value pair), and 
    #when we try to look into the hash/index of 'march 6' (index 9), we will see 'march 17''s value
    #of 'march 6''s own (310)
    print(samplehashtable['march 6'])



    

    