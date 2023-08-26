#Question 8: Draw the stairs in the Mario game (CS50) using hashtags using a recursive function

#Not super sure why this works... but I think may have something to do with the LIFO stack 
#(Data Structure) idea on how recurive function works that its able to print the Mario stairs.

#I believe at whichever point where it hits the duplicate function in the function itself, 
#after checking base condition, the code after that will not run, and store that loop (stairs(n)) in a 
#stack (Data Structure) at the bottom and it will loop back to the top, check base condition again, 
#if False, then continue down until it reaches the duplicate function, store that recursive loop 
#(stairs(n-1)) at the second bottom of the stack.

#If one of the loops the base condition is met, then the stack unwinds, with the top of the stack (Data
#Structure) being stairs(0), where n=1, will run through the code after the duplicate function followed by
#stairs(1) where n=2, until the bottom of the stack where stairs(n-1), where n=n. This will result in
#output being the mario stairs shape.

def stairs(n):
    if n == 0 or n < 0:               #This is the base condition, where there is no more of the pyramid/
        return                        #stairs left to draw out.
    else:                             #The 'return' function is to cut out of the recursive loop
        stairs(n-1)

    for i in range(n):               
        print('#', end="")


stairs(5)