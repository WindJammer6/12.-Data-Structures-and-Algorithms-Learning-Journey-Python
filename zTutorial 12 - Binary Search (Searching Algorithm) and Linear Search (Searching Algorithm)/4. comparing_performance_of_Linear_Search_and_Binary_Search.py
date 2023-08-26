#To understand about Decorators and 'wrapped functions' that we will be using in this file,  please refer to the files
#'4.1. What_are_Decorators.txt' to '4.5. Excercise1_Decorators.py'

#Importing the 'wrapped function' 'time_it' from 'time_it.py' (you can find this file in this tutorial's directory),
#so that we can add a Decorator (with the 'wrapped function''s name as the Decorator/'tag' ('@time_it')) to the 
#'linear_search' and 'iterative_binary_search' functions to add/modify the functionalities of these functions to be 
#able to measure/track their own respective runtimes 

from time_it import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
        
    return -1

@time_it
def iterative_binary_search(numbers_list, number_to_find):

    left_index = 0
    right_index = len(numbers_list) - 1
    middle_index = 0

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_number = numbers_list[middle_index]

        if middle_number == number_to_find:
            return middle_index
        
        if middle_number < number_to_find:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

    return -1


if __name__ == '__main__':
    #When you measure the runtimes of the 'linear_search' and 'iterative_binary_search' functions, you will realise 
    #that you don't see a noticeable difference in runtime, and will both have a runtime almost close to 0.0 
    #milliseconds. This is because the sorted number List ('nums_list') is too small, hence in order to really see 
    #the effectiveness of Binary Search Algorithm in terms of Time Complexity, we will need to increase the size of 
    #our sorted number List ('nums_list')
    nums_list = [4, 9, 11, 17, 21, 25, 29, 32, 38]
    num_to_find = 32

    index = linear_search(nums_list, num_to_find)
    print(f"Number found at index {index} using Linear Search")

    index2 = iterative_binary_search(nums_list, num_to_find)
    print(f"Number found at index {index2} using iterative Binary Search")


    #Here we create a much bigger sorted number List ('nums_list2'), of 1000000 elements. When we try to find the 
    #last element using the Linear Search Algorithm, 'linear_search' and Binary Search Algorithm, 
    #'iterative_binary_search' we can see that 'linear_search' took about 35.6 milliseconds, while 
    #'iterative_binary_search' still took a runtime that is close to 0.0 milliseconds, proving that the Binary Search
    #Algorithm will be more efficient in this situation compared to the Linear Search Algorithm
    nums_list2 = [i for i in range(1000001)]
    num_to_find2 = 1000000

    index3 = linear_search(nums_list2, num_to_find2)
    print(f"Number found at index {index3} using Linear Search")

    index4 = iterative_binary_search(nums_list2, num_to_find2)
    print(f"Number found at index {index4} using iterative Binary Search")
