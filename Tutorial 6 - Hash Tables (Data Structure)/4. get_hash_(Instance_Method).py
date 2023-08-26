class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    #This is the hash function code.

    #Here's how it works:
    #It produces an index by taking the sum of the each character's ASCII values in the date string such 
    #as 'march 6', which gives us 609, and then put that number through Python's Modulo Operator (modding
    #(not dividing!)) by 100, the size of our array) which gives us the remainder of 609 % 100 = 9, 9 
    #being the index location in the array/list in memory of where our value, 310 is stored. 

    #Note that this Instance Method of a hash function returns the hash (aka the index) in the memory 
    #array of size 100 (from self.MAX) of the inputted string/key where the string/key's value will be 
    #placed inside (this does not include insertion/creation of the string/key's value)
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX


if __name__ == '__main__':
    samplehashtable = HashTable()
    print(samplehashtable.get_hash('march 6'))

    

    