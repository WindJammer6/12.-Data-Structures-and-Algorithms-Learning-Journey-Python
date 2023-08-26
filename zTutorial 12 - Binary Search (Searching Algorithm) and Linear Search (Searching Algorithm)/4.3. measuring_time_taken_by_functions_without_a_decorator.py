#Now, lets say we want to check how much time it takes to run each function. So we will need to use Python's 
#'time' library's 'time()' function

#Note that the 'time()' function returns you the number of seconds passed since epoch. (There are different 
#epoch time for different computers, but for the Unix system, January 1, 1970, 00:00:00, at UTC is epoch)

#We can calculate the time taken for each function to run by creating a 'start_time' variable as the first 
#line of code in the function, to take the start time since epoch when the function starts running, and
#creating an 'end_time' variable as the last line of code in the function (before returning or right before
#we exit the function), to take the end time since epoch when the function stops running. We will then
#find the difference between 'end_time' and 'start_time' variables to find the time taken for that particular
#function to run


#The Problem with 'checking how much time it takes to run each function' in this manner:
#Lets say we have a big project, which is storing hundreds of functions, if we want to measure the time taken
#to run each and every function, you will need to add the same few lines of code (marked out by an '***') in 
#every function, making it very repetitive to see these few same lines of code. 

#Hence, here is where Decorators come in to solve this problem.

import time

def calc_square(numbers):
    start_time = time.time()                                                                    #***

    result = []
    for number in numbers:
        result.append(number*number)
    
    end_time = time.time()                                                                      #***
    #Note that we multiply by 1000 here because the differences between time taken to run functions are very
    #short (milliseconds), and that since the 'time()' function only returns a number in terms of seconds, we
    #need to multiply the result of 'end_time - start_time' by 1000 to get a whole number/integer else if 
    #displayed in seconds, the result of 'end_time - start_time' will contain a lot of decimal places
    print("'calc_square()' took " + str((end_time - start_time) * 1000) + "milliseconds")       #***
    return result

def calc_cube(numbers):
    start_time = time.time()                                                                    #***

    result = []
    for number in numbers:
        result.append(number*number*number)
        
    end_time = time.time()                                                                      #***
    print("'calc_cube()' took " + str((end_time - start_time) * 1000) + "milliseconds")         #***
    return result


array = range(1,100001)
output_square = calc_square(array)
output_cube = calc_cube(array)

print(output_square)
print(output_cube)