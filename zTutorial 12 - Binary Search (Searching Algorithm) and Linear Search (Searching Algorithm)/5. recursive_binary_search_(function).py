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


#What this function does is that it implements recursive Binary Search Algorithm

#Notice that compared to the 'iterative_binary_search' function, this 'recursive_binary_search' function takes in
#2 more parameters, 'right_index' and 'left_index'. These parameters represents the right and left index boundaries
#in the sorted number List that we will be searching for the number we are looking for. (E.g. if 'left_index' is 0
#and 'right_index' is 3, we will only be searching for the number we are looking for from index 0 to 3 of the sorted
#number List)

#Obviously, we would want to be searching the full sorted number List input most of the time, so these 2 additional
#parameters are more for getting the recursion loop to work (you'll understand after looking at the code in the 
#'recursive_binary_search' function)

#(Note that this 'time_it' Decorator/'wrapped function' is not made to handle recursive functions like this one
#(see the code in 'time_it.py') so the output for this function will be a bit strange (after testing, the 'time_it'
#Decorator/'wrapped function' prints the runtime for each recursive loop instead of from the start of the first 
#recursive loop until the point a value is returned) Will look into this bug some other time...)
@time_it
def recursive_binary_search(numbers_list, number_to_find, left_index, right_index):

    #This is just a safe-check if statement, in case the provided 'left_index' is larger than the 'right index',
    #which would not make sense
    if right_index < left_index:
        #Note that it is common practice to return the integer '-1' when we cannot find the element we are looking
        #for in Search Algorithms
        return -1

    #Notice that these codes below are all the same as the codes within the while loop in the 'iterative_binary_search'
    #function, this is because the concept of Binary Search will be the same, regardless if we are implementing it
    #iteratively or recursively

    #The only difference is that instead of using a while loop (used in the 'iterative_binary_search' function), here
    #we are using a recursive loop (since this is a recursive function). You can refer to 
    #'3. iterative_binary_search_(function).py' for technical explanation of these codes here
    middle_index = (left_index + right_index) // 2
    #This is another safe-check if statement, to prevent if an input dosent exist as an element in the sorted number 
    #List, then we will have to break the recursive loop when the 'middle_index' starts to go out of the index range
    #of the sorted number List (either 'middle_index' becomes 0 < or >= len(numbers_list))
    if middle_index >= len(numbers_list) or middle_index < 0:
        return -1
    middle_number = numbers_list[middle_index]

    if middle_number == number_to_find:
        return middle_index
    
    if middle_number < number_to_find:
        left_index = middle_index + 1
    else:
        right_index = middle_index - 1

    #Here you call the 'recursive_binary_search' function recursively to initiate the next recursive loop if we have 
    #not already broken out of the function. We will call it recursively with the updated 'left_index' and 'right_index'

    #Note that the 'return' statement is important as, if in one of the recursive loop it returns the 'middle_index',
    #we will need to return that 'middle_index' back to the main code hence this is why you need the 'return' statement
    #here. Otherwise, you'll will not have any return value, and your return value will just be None
    return recursive_binary_search(numbers_list, number_to_find, left_index, right_index)


if __name__ == '__main__':
    nums_list = [4, 9, 11, 17, 21, 25, 29, 32, 38]
    num_to_find = 32

    index = linear_search(nums_list, num_to_find)
    print(f"Number found at index {index} using Linear Search")

    index2 = iterative_binary_search(nums_list, num_to_find)
    print(f"Number found at index {index2} using iterative Binary Search")

    index3 = recursive_binary_search(nums_list, num_to_find, 0, len(nums_list))
    print(f"Number found at index {index3} using recursive Binary Search")


    nums_list2 = [i for i in range(1000001)]
    num_to_find2 = 1000000

    index4 = linear_search(nums_list2, num_to_find2)
    print(f"Number found at index {index4} using Linear Search")

    index5 = iterative_binary_search(nums_list2, num_to_find2)
    print(f"Number found at index {index5} using iterative Binary Search")

    index6 = recursive_binary_search(nums_list2, num_to_find2, 0, len(nums_list2))
    print(f"Number found at index {index6} using recursive Binary Search")