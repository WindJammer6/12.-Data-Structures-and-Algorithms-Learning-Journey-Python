#Question 4:
#Implement hash table where collisions are handled using Linear Probing. We learnt about Linear Probing 
#in the video tutorial. Take the hash table implementation that uses chaining and modify methods to use 
#Linear Probing. Keep MAX size of arr in hashtable as 10.

#ALOT of changes in code. I'll try my best to explain. My implementation of the Linear Probing is quite
#different. I did not try to understand the solution, but I did my best to fulfill all the requirements
#and characteristics of a Linear Probing (way-of-Collision-Handling)
#In memory:
#                                                                           Index:    
#march 6 (key) -> [hash function] -------       ---> [   ("march 2",400)  ]   1
#                                        |     | --> [("december 17", 300)]   2
#march 2 (key) -> [hash function] -------|----- /    [                    ]   3                                         
#                                        |  ----     [                    ]   4
#march 7 (key) -> [hash function] --     | /         [                    ]   5
#                                   \    |/          [                    ]   6
#                                    \   /\          [                    ]   7
#december 17 (key) -> [hash function] ---   -------> [   ("march 2",310)  ]   8
#                          (10)        \             [                    ]   9 
#                                       -----------> [   ("march 7",340)  ]   10
#for stock_prices["december 17"] = 300

#Notice that at each hash/index of the memory array of the Linear Probing Hash Table, a Tuple is stored
#consisting of the value and also its key (for accessing purposes (since the hashes are all messed up
#due to random slotting based on availability of memory slot in the memory array)) instead of just the
#key-value pair's value

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    #The hash function (no modifications needed here)
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    #Majority of the modifications falls under the '__setitem__' Special Method.
    def __setitem__(self, key, value):
        hash = self.get_hash(key)

        #First, I considered the case for a providing item to be set already exists in the Linear Probing
        #Hash Table. If it already does, it will replace the whole Tuple (with the same key, but different
        #value)

        #I had a major issue initially since initially I had it as:
            # for element in self.arr:
                # if element is not None and element[0] == key:
                #     element = (key, value)
                #     found = True
                #     break
        #which looks deceivingly correct. But it is not as it keeps giving the error:

            #     if element[0] == key:
            #     ~~~~~~~^^^
            # TypeError: 'NoneType' object is not subscriptable
        #which I understood as the elements that were None in the memory array of my Linear Probing Hash
        #Table do not have index hence the error

        #I knew I had to somehow take an index such that (in 3rd line) 'element[index] = (key, value)'and
        #solve this NoneType error. It took me an awfully long time to testing random functions until I 
        #tried the 'enumerate()' function (which we used a lot in the Seperate Chaining Hash Table
        #as well) that somehow solved both problems! Looks like I still don't know 'enumerate()' well 
        #enough.
        
        while True:
            found = False
            for index, element in enumerate(self.arr):
                if element is not None and element[0] == key:
                    self.arr[index] = (key, value)
                    found = True
                    break
            
            #Here I considered the case that the provided item to be set does not yet exist and hence
            #needed to be added into the Linear Probing Hash Table Data Structure.

            #The idea of Linear Probing is that if the slot provided by the hash/index is unavailable,
            #we will search the next if the next hash/index is available. If it is, then we will put the
            #new key-value pair in there. If it is not, we will search again to the next hash/index and
            #the cycle repeats.

            #We have 2 other scenarios to consider:
            #1. What happens if we reach the end of the memory array?
            #2. What if the memory array is full? We will need to terminate the program to prevent
            #   infinite looping at some point.

            if found == False:
                count = 0
                while True:
                    if self.arr[hash] is None:
                        self.arr[hash] = (key, value)
                        break
                    else:
                        
                        hash = hash + 1
                        count += 1
                        #Scenario 1: When we reach the end of the memory array, we will need to recycle
                        #back to the start of the memory array, and continue searching index by index
                        #for available memory slots from there. I did this by resetting the hash/index to
                        #0 if we reach the end of the memory array (hash/index == 10) which will slowly 
                        #increment again back to 10 
                        if hash == self.MAX:
                            hash = 0
                        #Scenario 2: When we searched the full memory array (which occurs when we have
                        #done the number of memory location searches equal to the size of the memory array.
                        #Hence the need for a counter, to check the number of memory location searches 
                        #iterations done. When it is equal to the size of the memory array with 
                        #'if count == self.MAX', we will feedback that the Linear Probing Hash Table is
                        #full, and break out of the while loop
                        if count == self.MAX:
                            print('This Hash Table is full!')
                            break
            else:
                break
            break

    #Changes fairly straightforward for '__getitem__', taking the code from '__setitem__' in the
    #Seperate Chaining Hash Table Data Structure          
    def __getitem__(self, key):
        for index, element in enumerate(self.arr):
            if element is not None and element[0] == key:
                return self.arr[index][1]
    
    #Changes fairly straightforward for '__delitem__', taking the code from '__setitem__' in the
    #Seperate Chaining Hash Table Data Structure    
    def __delitem__(self, key):
        for index, element in enumerate(self.arr):
            if element is not None and element[0] == key:
                self.arr[index] = None
                break
    

if __name__ == '__main__':
    samplehashtable = HashTable()

    #All 3 of these are the same index, 9
    #print(samplehashtable.get_hash('march 6'))
    # print(samplehashtable.get_hash('march 17'))
    # print(samplehashtable.get_hash('march 26'))

    # #All 3 of these are the same index, 1
    # print(samplehashtable.get_hash('march 19'))
    # print(samplehashtable.get_hash('march 8'))
    # print(samplehashtable.get_hash('march 28'))

    #Adding the data
    samplehashtable['march 6'] = 310
    samplehashtable['march 17'] = 450

    samplehashtable['march 19'] = 302
    samplehashtable['march 8'] = 380
    samplehashtable['march 28'] = 110

    samplehashtable['march 26'] = 350
    
    #Adding these random key-value pairs in to overflow the Hash Table Data Structure and to shows that
    #this program handles it by providing a feedback for every new attempt to store a key-value pair
    #after the Linear Probing Data Structure is full
    samplehashtable['march 13'] = 356
    samplehashtable['march 14'] = 413
    samplehashtable['march 15'] = 356
    samplehashtable['march 16'] = 334
    samplehashtable['march 20'] = 143
    samplehashtable['march 21'] = 321

    #Attempting to add in values that already exists in the Linear Probing Hash Table. The goal is for
    #these new values to replace the initial values in that key that already exists in the memory instead
    #of taking up a new spot in memory
    samplehashtable['march 6'] = 130
    samplehashtable['march 19'] = 800

    #Trying to use the '__getitem__' Special Method to check for changes in after attempting to replacing
    #'march 6' and 'march 19''s value in memory
    print(samplehashtable['march 6'])
    print(samplehashtable['march 19'])

    #Attempting to delete a key-value pair in the Linear Probing Hash Table
    del samplehashtable['march 6']

    print(samplehashtable.arr)