#This code is a copy from '4.4. measuring_time_taken_by_functions_with_a_decorator_and_explaining_why_
#functions_in_Python_are_considered_first_class_objects' from the folder 
#'Tutorial 12 - Binary Search (Searching Algorithm) and Linear Search (Searching Algorithm)' (when you
#import a name the file's name apparently can't have special characters and must only have alphabets 
#hence I couldn't number it and just gave it the name 'time_it')

#This code is used (through 'import') in the file 
#'3. improving_on_bubble_sort_inefficiency_1.py' and '4. improving_on_bubble_sort_inefficiency_2.py'

import time

def time_it(function):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(function.__name__ + " took " + str((end_time - start_time) * 1000) + " milliseconds")
        return result
    
    return wrapper
