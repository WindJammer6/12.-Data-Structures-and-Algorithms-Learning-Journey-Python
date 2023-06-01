#Here are 2 scenarios:
#Scenario 1: Store Apple's stock prices and answer, what was the price on Day 1 and Day 3? (by indexing)
#Scenario 2: Store Apple's stock prices and answer, what was the price on march 3 and march 7? 
#            (by date)

#In Scenario 1's case, it would make sense for us to use a List Data Structure, as it allows us to 
#quickly find the stock price by finding the index in the list

#However in Scenario 2, a List Data Structure will not work as you need to store data for both the 
#date, and its corresponding price for that date. Hence it would be better for your computer program
#to use a Hash Table (or dictionary in Python) Data Structure

#Scenario 1:
stock_price = [298,305,320,301,292]   #A List Data Structure
print(stock_price[0])                 #Show stock price for Day 1
print(stock_price[2])                 #Show stock price for Day 3

#Scenario 2:
stock_price2 = {                      #A Hash Table (dictionary) Data Structure
    'march 3':298,
    'march 4':305,
    'march 5':320,
    'march 6':301,
    'march 7':292,
}

print(stock_price2['march 3'])        #Show stock price for march 3
print(stock_price2['march 7'])        #Show stock price for march 7