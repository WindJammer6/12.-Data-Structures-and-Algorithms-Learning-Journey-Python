#Draw the 2 dimensional array data strucutre in memory

#Real life scenario:
#Lets say we have some stock prices data in a csv file that looks like this: 
#(in 'stock_prices_data.csv')
#   march 6,310
#   march 7,340
#   march 8,380
#   march 9,302
#   march 10,297
#   march 11,323

#Your task is to write a program that can give you a price based on the date given.

#There are 2 approaches to tackle this problem. The first approach is by storing the data in a 2D 
#Array Data Structure while the second approach is by storing the data in a Hash Table Data Structure
#(or a Dictionary (Python's implementation of a Hash Table))


#///////////////////////////////


#The first approach, using a 2D Array Data Structure:

#Creation of the 2D Array Data Structure:
stock_prices = []
with open("stock_prices_data.csv", "r") as file:
    for line in file:
        #This gives a list of 2 elements, for each seperated part of each line in the csv file after
        #splitting the line at the ',' character. So for 'march 6,310' it will give a list of
        #[march 6, 310]
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])

print(stock_prices)

#Output (2D Array Data Structure):
#    [['march 6', 310.0], 
#     ['march 7', 340.0], 
#     ['march 8', 380.0], 
#     ['march 9', 302.0], 
#     ['march 10', 297.0], 
#     ['march 11', 323.0]]


#Finding a price based on a given date:
date_to_find = 'march 9'
for element in stock_prices:
    if element[0] == date_to_find:
        print(int(element[1]))

#Output
#   302

#Whats wrong here?

#As we can see, using an Array Data Strucutre does work, however it is not very efficient when we take
#a look at its Big O Notation. Imagine if you have a database the size of a million rows and the data
#you want to find is near the end, then you'll need to run a million operations which makes the program
#not very efficient. (Big O Notation of Time Complexity of O(n))


#///////////////////////////////


#The second approach, using a Hash Table Data Structure:

#Creation of the Hash Table (or Dictionary) Data Structure:
stock_prices = {}
with open("stock_prices_data.csv", "r") as file:
    for line in file:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        #Note this key difference, on how you can set the key-value pair of the 2 elements that you get
        #after splitting each row in the csv file into 2 seperate elements
        stock_prices[day] = price

print(stock_prices)

#Output:
#   {'march 6': 310.0, 
#    'march 7': 340.0, 
#    'march 8': 380.0, 
#    'march 9': 302.0, 
#    'march 10': 297.0, 
#    'march 11': 323.0}

#Finding a price based on a given date:
print(int(stock_prices['march 9']))

#Output
#   302


#////////////////////////////////


#Comparison of Big O Notation of Time and Space Complexity for Array and Linked List Data Structures:
#Data Structures	|  S pace Complexity  |	           Average Case Time Complexity
#                   |                     |    Access	  Search	 Insertion 	  Deletion
#    Array	        |         O(n)	      |     O(1)	   O(n)	       O(n)	        O(n)
#  Hash Table	    |         O(n)	      |     N/A	       O(1)	       O(1)	        O(1)

#In this scenario it makes more sense to use a Hash Table Data Structure as to attain a certain stock 
#price from a date is of Big O Notation of Time Complexity of O(1) instead of O(n) in the first approach
#in 'print(int(stock_prices['march 9']))' as you can access the stock price's row directly based on the
#given string 'march 9' index'key instead of having to loop through every row in an Array Data Strucuture
#to find the matching date, and then getting the stock price.


#///////////////////////////////


#A look into internal memory of Array, 2D Array and Hash Table Data Structures:
#Visual representation on how it looks like:
#Array Data Structure in memory:                    Hash Table Data Structure in memory:     
#          Index:                                             Index:                              
#[       ]   1                                      [       ]   
#[       ]   2                                      [       ]   
#[  380  ]   3    stock_prices[3]                   [       ]                                
#[       ]   4                                      [       ]   
#[       ]   5                                      [       ]   
#[       ]   6                                      [       ]   
#[  310  ]   7    stock_prices[7]                   [       ]
#[       ]   8                                      [       ]
#[       ]   9                                      [  310  ]   march 6  stock_prices['march 6'] 
#[       ]   10                                     [  340  ]   march 7  stock_prices['march 7']

#2D Array Data Structure in memory:                  
#[march 6]
#[  310  ]
#[march 7]                         
#[  340  ]
#[march 8]
#[  380  ]
#[march 9]
#[  302  ]
#   ...
#[march11]
#[  323  ]