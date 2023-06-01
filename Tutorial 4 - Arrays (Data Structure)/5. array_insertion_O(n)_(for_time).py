#Inserting an element at a specific index is Big O Notation of Time Complexity of O(n)

#You would think its O(1), but no, because after inserting that element into the Array at a specific
#index, it has to shift the rest of the Array up to compensate for the insertion (+1 to their indexes) 
#and this varies according to n number of elements in the Array. Hence insertion is Big O Notation of 
#Time Complexity of O(n) for Arrays.

stock_price = [298,305,320,301,292]
stock_price.insert(1, 284)         #'insert()' function takes 2 parameters, first parameter is the index
print(stock_price)                 #to insert the element, second parameter is what you want to insert
                                   #into the Array/List (can be a list/single element)  