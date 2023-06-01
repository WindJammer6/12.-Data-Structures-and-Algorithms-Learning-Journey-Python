#This is using the recursion approach (function defined by itself) to solve our real life problem 
#explained in '1. What_is_Recursion_(explained_with_real_life_problem).txt'
def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)

if __name__ == '__main__':
    print(find_sum(5))

#Recall the 3 steps to making a recursive function:
    #In a recursive approach/function, you are need do these 3 steps:
    #1. Divide a bigger problem into smaller and simpler problems
    #2. Find a base condition with a simple answer. (This base condition is a criteria for recursion 
    #   to happen btw, as you need the base condition to tell the program when to stop the recursive 
    #   loops and arrive at a final output)
    #3. Return or roll back base condition answer to solve all sub problems

#How the recursive function 'find_sum(n)' works is that the line 'return n + find_sum(n-1)' sets the
#recursive loop as when its called, the 'find_sum(n-1)' will loop its own function (without returning
#anything yet out of the function since the line forces the code to loop again as 'find_sum(n-1)' is
#still unknown) again and again until it hits the base condition. This creates a stack (Data Structure)
#which we will learn later but in short follows the LIFO (Last-In-First-Out) principle.

#This shows the importance of the base condition as without it, the recursive loop will loop forever
#without a trigger to stop the loop. 

#Once the base condition is hit (n == 1), the 'find_sum(n-1)' a the top of thestack (Data Structure)
#will return 1 which returns to the top 'find_sum(n-1)/find_sum(2-1)' and the recursive function will
#cause a stack unwind back to 'find_sum(n)' and will return the overall output for the recursive function
#'find_sum(n)'