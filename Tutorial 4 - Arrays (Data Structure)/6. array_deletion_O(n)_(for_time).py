#Deleting an element at a specific index is Big O Notation of Time Complexity of O(n)
#Similar to how insertion works, because after deleting that element from the Array at a specific
#index, it has to shift the rest of the Array down to compensate for the deletion (-1 to their indexes) 
#and this varies according to n number of elements in the Array.

stock_price = [298,305,320,301,292]
#del stock_prices[1]               #'del()', 'pop()' both also works to delete an element from the array
#stock_prices.pop(1)               #they take index as input instead of the element as input
stock_price.remove(305)
print(stock_price)