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

    def add_key_value_pair_into_Hash_Table(self, key, value):
        hash = self.get_hash(key)
        self.arr[hash] = value

    #What this Instance Method does is that it gets and returns the value based on the key inputted into
    #the function/instance method in the 'HashTable' object by again, first obtaining the hash/index of 
    #the inputted key such as 'march 6' and returning the hash, storing the hash in the 'hash' variable,
    #and then, like in an Array Data Structure, return the value using the index in the Array 
    def get_value_from_key(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]
    

if __name__ == '__main__':
    samplehashtable = HashTable()
    print(samplehashtable.get_hash('march 6'))

    samplehashtable.add_key_value_pair_into_Hash_Table('march 6', 310)
    #To check for changes in the array/list in memory in the 'HashTable' object
    print(samplehashtable.arr)

    print(samplehashtable.get_value_from_key('march 6'))


    

    