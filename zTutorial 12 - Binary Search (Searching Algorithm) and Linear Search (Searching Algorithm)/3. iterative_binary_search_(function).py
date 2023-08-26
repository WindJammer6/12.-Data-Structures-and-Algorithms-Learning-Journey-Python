def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
        
    return -1

#What this function does is that it implements iterative Binary Search Algorithm
def iterative_binary_search(numbers_list, number_to_find):

    #Before we enter the while loop to do our Binary Search, we need to first define our 'left_index',
    #'right_index' and 'middle_index'.

    #-> 'left_index' represents the most left element's index in the remaining sorted List (it might not be 
    #   constant as the sorted List will be sort of 'cut in half' every iteration, and the left index of the 
    #   remaining sorted List might not be the same element if the left half of the sorted List is sort of 
    #   'cut away' (further explanation below))

    #-> 'right_index' represents the most right element's index in the remaining sorted List (it might not be 
    #   constant as the sorted List will be sort of 'cut in half' every iteration, and the right index of the 
    #   remaining sorted List might not be the same element if the right half of the sorted List is sort of 
    #   'cut away' (further explanation below))

    #-> 'middle_index' represents the most middle element's index in the remaining sorted List (it will not be 
    #   constant as the sorted List will be sort of 'cut in half' every iteration, and the middle index of the 
    #   remaining sorted List will not be the same element and relocated to be the middle element of the 
    #   remaining sorted list after either right or left half of the sorted List is sort of 'cut away' (further
    #   explanation below))
    left_index = 0
    right_index = len(numbers_list) - 1
    middle_index = 0


    #To understand how the while loop's condition works, we need to understand how whole Binary Search Algorithm is
    #implemented within the while loop and how the 'left_index', 'right_index' and 'middle_index' variables are used. 

#       Visualisation of how Binary Search Algorithm works:
#       In the case where the number we are looking for is '32' in the sorted List:
#        0  1   2   3   4   5   6   7   8               left_index == 0
#       [4][9][11][17][21][25][29][32][38]              right_index == 8
#                       ^                               middle_index == 4

#       //////////////////  5   6   7   8               left_index == 4 (previous middle index) + 1 == 5
#       [4][9][11][17][21][25][29][32][38]              right_index == 8
#       //////////////////      ^                       middle_index == (4 (left_index) + 8 (right_index)) // 2 == 6

#       //////////////////////////  7   8               left_index == 6 (previous middle index) + 1 == 7
#       [4][9][11][17][21][25][29][32][38]              right_index == 8
#       //////////////////////////  ^                   middle_index == (7 (left_index) + 8 (right_index)) // 2 == 7

#       In the case where the number we are looking for is '4' in the sorted List:
#        0  1   2   3   4   5   6   7   8               left_index == 0
#       [4][9][11][17][21][25][29][32][38]              right_index == 8
#                       ^                               middle_index == 4

#        0  1   2   3 ////////////////////              left_index == 0
#       [4][9][11][17][21][25][29][32][38]              right_index == 4 (previous middle index) - 1 == 3
#           ^         ////////////////////              middle_index == (0 (left_index) + 3 (right_index)) // 2 == 1

#        0 ///////////////////////////////              left_index == 0
#       [4][9][11][17][21][25][29][32][38]              right_index == 1 (previous middle index) - 1 == 0
#        ^ ///////////////////////////////              middle_index == (0 (left_index) + 0 (right_index)) // 2 == 0

    #From the above representation, we can now see that this condition checks if the case that if the 'left_index' 
    #is smaller or equal the 'right_index'. If this condition is not met, where 'left_index' is larger or equal 
    #to 'right_index', this indicates that the whole sorted List has been searched, signalling the program to cut 
    #the while loop 
    while left_index <= right_index:
        
        #By setting 'middle_index = (left_index + right_index) // 2', together with the 
        #'left_index = middle_index + 1'/'right_index = middle_index - 1' from the previous while loop iteration,
        #you are essentially setting the new left/right half of the new remaining sorted List to search the number
        #you are looking for. The current while loop iteration's 'middle_index = (left_index + right_index) // 2'
        #sets the new 'middle_index' in the new remaining sorted List 

        #Notice here the code uses '//' instead of '/' to divide by 2. So what the '//' does is that
        #it is to ensure the result is an integer instead of a float. For example if the Array has size 
        #9, the '/' will return you a float, 4.0 (not 4.5, as Python automatically rounds down the 
        #decimal place to give the nearest whole number by default unless you specifically tell the program 
        #to return the number result with a certain number of decimal places). But if you use '//', the '//' 
        #will return you an integer, 4 instead, which is the ideal data type you want in your function
        middle_index = (left_index + right_index) // 2
        middle_number = numbers_list[middle_index]

        #If 'middle_number' is the number you are looking for then you return that 'middle_number''s index, 
        #'middle_index'
        if middle_number == number_to_find:
            return middle_index
        
        #If middle number is smaller than the number we are looking for, we will then search the right half of the
        #sorted List in the next iteration. This code allows us to do this by setting the new 'left_index' to be the
        #one index above the 'middle_index' in the next iteration
        if middle_number < number_to_find:
            left_index = middle_index + 1
        #If middle number is larger than the number we are looking for, we will then search the left half of the
        #sorted List in the next iteration. This code allows us to do this by setting the new 'right_index' to be the
        #one index below the 'middle_index' in the next iteration
        else:
            right_index = middle_index - 1

    #After using Binary Search to search through the whole List, if the element we are looking for cannot be found, 
    #we will return '-1' to show False output (number you are looking for is not found in List)

    #Note that it is common practice to return the integer '-1' when we cannot find the element we are looking
    #for in Search Algorithms
    return -1


if __name__ == '__main__':
    #In Linear Search, the List does not necessarily need to be sorted. But we are using a sorted List in 
    #this case so we can use the same sorted List to compare Linear Search and Binary Search (see 
    #'3. iterative_binary_search_(function).py'). Note that for Binary Search, in order to use it to search 
    #for an element, Binary Search requires that List to be sorted for it to work, otherwise, Binary Search 
    #will fail if the List is unsorted (unlike for Linear Search, which will still be able to work for unsorted
    #List)
    nums_list = [4, 9, 11, 17, 21, 25, 29, 32, 38]
    num_to_find = 32

    index = linear_search(nums_list, num_to_find)
    print(f"Number found at index {index} using Linear Search")

    index2 = iterative_binary_search(nums_list, num_to_find)
    print(f"Number found at index {index2} using iterative Binary Search")