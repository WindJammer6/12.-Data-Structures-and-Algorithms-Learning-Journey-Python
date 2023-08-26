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
    
    #What this Instance Method does is that it adds a 'key-value' pair in the 'HashTable' object. It does
    #this by first obtaining the hash/index of the inputted key such as 'march 6' and returning the hash,
    #storing the hash in the 'hash' variable, and then, like in an Array Data Structure, assign the key's
    #value to that particular slot in the array using the hash/index obtained from putting the inputted 
    #key through the hash function
    def add_key_value_pair_into_Hash_Table(self, key, value):
        hash = self.get_hash(key)
        self.arr[hash] = value
    

if __name__ == '__main__':
    samplehashtable = HashTable()
    print(samplehashtable.get_hash('march 6'))

    samplehashtable.add_key_value_pair_into_Hash_Table('march 6', 310)
    #To check for changes in the array/list in memory in the 'HashTable' object
    print(samplehashtable.arr)


    

    