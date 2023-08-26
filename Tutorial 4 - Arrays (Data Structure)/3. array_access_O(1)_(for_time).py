#Accessing a element is Big O Notation of Time Complexity of O(1)

#This is because in memory, 'stock_prices' points to the beginning element's address of the array, 
#and the data structure then apply the indexed number to a function that multiplies it by the byte
#size of the data type inside to instantly get the desired element based on the given index hence
#accessing an element is Big O Notation of Time Complexity of O(1) for Arrays.

stock_price = [298,305,320,301,292]
print(stock_price[0])
print(stock_price[2])