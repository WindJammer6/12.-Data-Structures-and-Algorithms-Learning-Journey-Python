#This computer program is in the Big O Notation of O(1)

#This is because in order to find a specific 'pe' for a specific 'price' and its corresponding 'eps', 
#regardless of the size, n of the List (for 'price_list' and 'eps_list'), the order of operation to find
#that 'pe' will always be 1 due to the indexing as the code just needs to run once according to the
#provided index to obtain the output

#time = a

#By the 2 steps, 
#    1. Keep fastest growing term, which is a
#    2. Drop constants, which gives you a/a = 1
#It is Big O Notation O(1)

def main():
    price_list = [100,200,300,400,500,600]             
    eps_list = [2,4,6,8,10,12]
    print(find_first_eps(price_list, eps_list, 2))

#In this self-made function it takes 2 Lists Data Structure as its parameter, 'prices' and 'eps', 
#as well as 1 index parameter, 'index' (theres no such thing as an index parameter, the argument 'index' 
#becomes an index parameter as defined by the code inside the function)

def find_first_eps(prices, eps, index):                 #List Data Structure have indexing btw, hence
    pe = prices[index]/eps[index]                       #you can throw the index argument in the self-made
    return pe                                           #function

main()
