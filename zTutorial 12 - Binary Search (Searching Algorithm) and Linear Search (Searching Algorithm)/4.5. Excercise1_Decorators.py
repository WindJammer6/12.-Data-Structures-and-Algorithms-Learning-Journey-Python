#Question 1:

#a. Create a decorator function to check that the argument passed to the function factorial is a non-negative 
#   integer:

#b. Create a factorial function which finds the factorial of a number.

#c. Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.
    #E.g. 
    #    factorial(1.354) : raise Exception or print error message
    #    factorial(-1) : raise Exception or print error message
    #    factorial(5) : 60


#My Solution (Looks similar to provided answer, producing all the desired outputs, so won't be adding the 
#provided answer here):

#a. and c.
#The 'wrapper function'
def is_number_non_negative(function):

    def wrapper(args):
        if args < 0:
            return "Please enter a number larger or equal to zero!"
        elif isinstance(args, int) == False:
            return "Please enter an integer!"
        else:
            result = function(args)
            return result
    
    return wrapper

#b.
#Decorator/'tag'
@is_number_non_negative
#The 'other function' that will be wrapped by the 'wrapper function'
def factorial_function(number):
    factorial_number = 1
    for i in range(1, number + 1):
        factorial_number = factorial_number * i
    return factorial_number


print(factorial_function(1.354))
print(factorial_function(-1))
print(factorial_function(5))