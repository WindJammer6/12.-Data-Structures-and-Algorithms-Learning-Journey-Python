#Printing out the number at an index in the Fibonacci Series with Recursion (basically a series of 
#numbers where each number is the sum of the 2 preceding ones) 

#Fibonacci Series: 0,1,1,2,3,5,8,13,21,34...
#Indexing:         0,1,2,3,4,5,6,7 ,8 ,9 ...

def fib(n):
    if n == 0 or n == 1:               #First, taking care of the base condition for this recursive 
        return n                       #function to print out the Fibonacci Series, which is if n == 0,
    return fib(n-1) + fib(n-2)         #number at index 0 is 0 and if n == 1, number at index 1 is 1

if __name__ == '__main__':
    print(fib(6))
