#A Decorator allows you to 'wrap' other functions within a function (this function is also known as a
#'wrapper function').


#To demonstrate how a Decorator does this, lets first remove all the lines of code that is making the
#'time taken logic' work within the functions (by commenting them out), and creating a seperate function,
#which we will name as 'time_it' that stores the 'time taken logic' codes.


#Functions in Python are considered "First-class objects":
#Before we go further, we need to understand that in Python, functions are considered 'First-class 
#objects', which means they are treated as any other data type, such as integers, strings, or lists, 
#and you can treat them just like any other variable and you can pass them as arugument to another
#function or even return them as a return value.

#Note: "First-class objects" refers to the capability of a programming language to treat entities, 
#such as values or data, as first-class citizens or objects


#Coming back to the task, this seperate function will be able to take in functions as an argument, and then 
#after modifying the original function within itself by running additional lines of code along with the 
#original function, it returns that modified version of the original funciton, effectvely replacing the 
#original function with the modified version of the original function (this is such that only the modified 
#version of the original function is being ran, not the original version, as we don't want to accidentally 
#run the original function twice). This seperate function is also known as the 'wrapper function'.

#So when you add a Decorator/'tag' with the name of this seperate function to other functions, 
#(e.g. @seperate_function), you are telling your program, instead of immediately running the original version
#of the other function, run the other function within the aforementioned 'wrapper function' given by the name
#of the Decorator/'tag' (as a modified version of the original function). This is effectively equivalent to
#saying that that Decorator tells your 'wrapper function' to wrap the decorated/tagged other functions.


import time

#Here is our 'wrapper function', 'time_it'. Recall that in Python, since functions are considered 'first-class 
#objects', we will pass a function as an argument in our 'wrapper function'
def time_it(function):

    #Python also allows you to make inner functions like this, a function within a function.
    
    #Why do we need this inner function in our 'wrapper function'?
    #From what I gathered, its less on logic, but its just to get the code to work. Lets say we just have the
    #function without an innter function like so (this function does run without errors btw):

        # def time_it2(function):
        #     start_time = time.time()
        #     result = function
        #     end_time = time.time()
        #     print(function.__name__ + "took" + str((end_time - start_time) * 1000) + "milliseconds")
        #     return result

    #However, this 'wrapper function' would not work as desired. The desired result would be that the line of
    #code 'start_time = time.time()' will be run, before the other function being wrapped being run, then lastly
    #the lines of code 'end_time = time.time()' and the 'print()' function. However, in this code, instead of 
    #the other function being wrapped being run at 'result = function', the function is simply stored in the 
    #'result' variable and only run when the 'result' variable is being returned at the end in 'return result'

    #Hence, in order for our 'wrapper function' to work as desired, we need to have an inner function


    #The inner function 'wrapper' takes in any number of (positional) arguments and keyword arguments (from the
    #function 'function' parameter taken in by the outer 'time_it' function) as its parameters. (it needs to be
    #like that cuz you want this 'wrapper function' to be able to wrap all types of other functions, regardless
    #of the number of arguments these other functions are able to take). To do this, we will need to add 1 
    #asterisk ('*') in front of the (positional) argument, 'args' and 2 asterisk in front of the keyword argument,
    #'kwargs' (for more info about *args, **kwargs, refer to '3.1. explaining_def_function.py' in the 
    #'Tutorial 2 - Big O Notation' folder)
    def wrapper(*args, **kwargs):
        #Codes that will be run before the other function
        start_time = time.time()

        #Here, we will call and run our other function being wrapped within the 'wrapper function'. Any output
        #that this other function has will be stored in the 'result' variable
        result = function(*args, **kwargs)

        #Codes that will be run after the other function
        end_time = time.time()
        #'__name__' returns you the name of the function that is being passed through the 'wrapper 
        #function'
        print(function.__name__ + " took " + str((end_time - start_time) * 1000) + " milliseconds")

        #What this line of code inside the inner function 'wrapper' does is crucial in ensuring the modified
        #version of the other function, now aka the inner function 'wrapper', behaves correctly in terms of its
        #return values, and preventing the 'wrapped function' from interfering with the original other function's
        #return values. In this case, the modified version of the other function is supposed to return the same
        #values as the original function, so we saved the return values of the original other function in the 
        #variable 'result' and we return that here. Without it, you will just get an output of 'None' when you
        #run all the other functions with this 'wrapped function' as a Decorator
        return result
    
    #What this line of code does is that when the other function is being wrapped and modified by this inner 
    #function ('wrapper') of the 'wrapper function', and you 'return' the modified version of the original 
    #function, now also known as the inner function 'wrapper' (this is another property of Python's functions as
    #'First-class objects', that they are 'returnable'),  it allows the 'wrapper function' (as a whole) 
    #to effectively replace the modified version of the original function, now aka the inner function 'wrapper'
    #with the original function (to prevent the original function from running again, cause it to sort of 
    #'double-run')
    return wrapper

#Once you have your 'wrapper function' (in this case its 'time_it'), you can add it as a Decorator/'tag' like so
#at the beginning of the other functions you want it to wrap
@time_it
def calc_square(numbers):
    # start_time = time.time()

    result = []
    for number in numbers:
        result.append(number*number)
    
    # end_time = time.time()
    # print("'calc_square()' took " + str((end_time - start_time) * 1000) + "milliseconds")
    return result

#Once you have your 'wrapper function' (in this case its 'time_it'), you can add it as a 
#Decorator/'tag' like so at the beginning of the other functions you want it to wrap
@time_it
def calc_cube(numbers):
    # start_time = time.time()

    result = []
    for number in numbers:
        result.append(number*number*number)
        
    # end_time = time.time()
    # print("'calc_cube()' took " + str((end_time - start_time) * 1000) + "milliseconds")
    return result


#When you do debugging of these codes, you will notice that when the code reaches 
#'output_square = calc_square(array)' and 'output_cube = calc_cube(array)', the program dosen't jump
#straight into the 'calc_square' and 'calc_cube' functions above, but it will first notice the 
#'@time_it' Decorator/'tag' at the top of the 'calc_square' and 'calc_cube' functions and run the
#'time_it' 'wrapper function' first instead, before jumping back into the respective functions in the
#line of code in the 'time_it' 'wrapper function', 'result = function(*args, **kwargs)'
array = range(1,100001)
output_square = calc_square(array)
output_cube = calc_cube(array)

print(output_square)
print(output_cube)
