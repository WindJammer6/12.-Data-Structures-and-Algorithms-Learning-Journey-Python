#2D arrays (or even 3D, 4D arrays and above exists)

#This is how a 2D array look like, arrays within an array
stock_prices = [
    [2,3,5,6],
    [40,42,38,44],
    [78,89,71,66]
]

#This is how you access a specific element in the 2D array (row 1/array1, index 1 in that row/array),
#gives you the element '42' in this 2D array
print(stock_prices[1][1])