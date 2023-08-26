#What this function does is that it implements Selection Sort Algorithm.

#From '1. What_is_Selection_Sort.txt', for reference,
# Here are the steps of Selection Sort Algorithm:
# 1. Split the unsorted array/List into 2 subarrays, the sorted subarray and unsorted subarray. We can do this by 
#    creating a pointer pointing to the first element of the unsorted List like so (during Insertion Sort, 
#    this pointer will be created pointing to the second element instead). 
   
#    The elements on the left side of the element that this pointer is pointing at is part of the sorted subarray 
#    (excluding the element that this pointer is pointing at), while the elements on the right side of the element 
#    that this pointer is pointing at is part of the unsorted subarray (including the element that this pointer is 
#    pointing at)

#    Note: - During the starting iteration, for the first element's iteration in the initial unsorted List, there is 
#            no elements in the sorted subarray

# 2. Within the unsorted subarray of the initial unsorted List, we will find and identify the smallest element
#    (lets assume we have an algorithm that will allows us to find the minimum element in a List, which is quite 
#    simple to implement actually which we will look at in the '2. selection_sort_(function).py' file)

# 3. We will then do a swap in the positions of the element that the pointer is pointing at, and the minimum element 
#    identified by the seperate algorithm that finds the minimum element in a List.

#    This is unless, if the identified minimum element happens to also be the element that the pointer is pointing 
#    at (or that there is a duplicate of the element that the pointer is pointing at in the unsorted subarray, and 
#    both of which also happens to be the identified minimum element), then we will not do this swap, and hence not 
#    execute anything in step 3.

# 4. Now we will move the pointer down the unsorted List, to the next index/element (unless you've reached the last
#    element of the unsorted List)

# 5. Repeat steps 2 to 4 iteratively until we reach the last element. There is no need to repeat step 2 to 4 for
#    the last element as it is the only element left in the unsorted subarray. And since the last element is
#    the only element in the initial unsorted List yet to be sorted while all the other elements are already 
#    sorted/in the correct position, this last element must also already be pre-sorted/in its correct position 
#    without having to go through the sorting process that is step 2 to 4


def selection_sort(number_list):

    # 4. Now we will move the pointer down the unsorted List, to the next index/element (unless you've reached the 
    #    last element of the unsorted List)

    # 5. Repeat steps 2 to 4 iteratively until we reach the last element. There is no need to repeat step 2 to 4 for
    #    the last element as it is the only element left in the unsorted subarray. And since the last element is
    #    the only element in the initial unsorted List yet to be sorted while all the other elements are already 
    #    sorted/in the correct position, this last element must also already be pre-sorted/in its correct position 
    #    without having to go through the sorting process that is step 2 to 4

    #    Steps 4 and 5 of Selection Sort Algorithm is done by this for loop, which will 'loop' steps 1, 2 and 3 (it 
    #    technically doesnt really loop step 1, even though the line of code that implements step 1 is within this 
    #    for loop, you can look at the explanation for the line of code implementing step 1 below) 

    #    (Explanation for how this for loop does step 4)
    #    It does step 4 because after every loop, it shifts the pointer one index to the right in the initial 
    #    unsorted List to iterate through the elements starting from the first element in the initial unsorted List
    #    until the second last element of the initial unsorted List (indicated by the 'len(number_list) - 1' 
    #    parameter in the 'range()' function in the for loop)

    #    (Explanation for how this for loop does step 5)
    #    It does step 5 because within this for loop, it contains the codes that implements steps 2 and 3, and this 
    #    code itself does step 4 after every loop (see above 'Explanation for how this for loop does step 4'). Also, 
    #    it tells the program to start at the first element in the initial unsorted List (the default behaviour of 
    #    the 'range()' function if there is only one parameter given) and stop at the second last element of the 
    #    initial unsorted List (from the only one parameter, 'len(number_list) - 1')
    for i in range(len(number_list) - 1):

        # 1. Split the unsorted array/List into 2 subarrays, the sorted subarray and unsorted subarray. We can do this by 
        #    creating a pointer pointing to the first element of the unsorted List like so (during Insertion Sort, 
        #    this pointer will be created pointing to the second element instead). 
        
        #    The elements on the left side of the element that this pointer is pointing at is part of the sorted subarray 
        #    (excluding the element that this pointer is pointing at), while the elements on the right side of the element 
        #    that this pointer is pointing at is part of the unsorted subarray (including the element that this pointer is 
        #    pointing at)

        #    Note: - During the starting iteration, for the first element's iteration in the initial unsorted List, there is 
        #            no elements in the sorted subarray


        #    During the first loop of the for loop, this line of code executes step 1, which is initiating a pointer
        #    pointing at the first element in the initial unsorted List, since during the first loop of the for loop, 
        #    variable 'i' is the first element's index (0). It then stores the element the pointer is pointing at 
        #    into the 'minimum_element_index' variable

        #    However, for subsequent loops, this line of code is not running step 1, but is just storing the element
        #    the pointer is pointing at (of the index stored in variable 'i') into the 'minimum_element_index' 
        #    variable


        #    As we create this pointer, we are simultaneously declaring the element this pointer is pointing at as
        #    currently the minimum element in the unsorted subarray (it is not confirmed to be the minimum element,
        #    but we will put this element this pointer is pointing at as 'minimum_element_index' variable as a 
        #    placeholder). We will see how we will be using this 'minimum_element_index' variable to find the 
        #    minimum element in the unsorted subarray using the seperate algorithm that finds the minimum element
        #    in a List in step 2 below
        minimum_element_index = i

        # 2. Within the unsorted subarray of the initial unsorted List, we will find and identify the smallest element
        #    (lets assume we have an algorithm that will allows us to find the minimum element in a List, which is quite 
        #    simple to implement actually which we will look at in the '2. selection_sort_(function).py' file)

        #    Here is the seperate algorithm that allows us to find the minimum element in a List.

        #    How this seperate algorithm finds and identify the minimum in a List in Selection Sort is,
        #    a. First, by traversing through the entire unsorted subarray, starting with the second element of the 
        #       unsorted subarray ('i + 1'), where the 'i' variable represents the index of the first element in the 
        #       unsorted subarray (which the pointer is pointing at). 

        #       Note: The reason why we didn't include traversing through the first element in the unsorted subarray 
        #       ('i') (which the pointer is pointing at) is because we technically already 'traversed' through it when 
        #       we put the first element in the sorted subarray ('i') (which the pointer is pointing at) as the 
        #       'minimum_element_index' before the start of this seperate algorithm

        #    b. Then, we will compare each element that this seperate algorithm has traversed through in the unsorted 
        #       subarray with the currently minimum element found so far by the seperate algorithm that is stored in 
        #       the 'minimum_element_index' variable.
        #       -> If the element that the seperate algorithm is currently at during its traversal through in the 
        #          unsorted subarray is even smaller than the minimum element found so far by the seperate algorithm 
        #          that is stored in the 'minimum_element_index' variable, we will then replace this element with the
        #          minimum element found so far by the seperate algorithm in the 'minimum_element_index' variable. We
        #          will then continue the traversal of the seperate algorithm through the unsorted subarray
        #       -> Else, if the element that the seperate algorithm is currently at during its traversal through in the 
        #          unsorted subarray is larger or equal to the minimum element found so far by the seperate algorithm 
        #          that is stored in the 'minimum_element_index' variable, we will not do anything and continue the 
        #          traversal of the seperate algorithm through the unsorted subarray
        for j in range(i + 1, len(number_list)):
            if number_list[j] < number_list[minimum_element_index]:
                minimum_element_index = j

        # 3. We will then do a swap in the positions of the element that the pointer is pointing at, and the minimum element 
        #    identified by the seperate algorithm that finds the minimum element in a List.

        #    This is unless, if the identified minimum element happens to also be the element that the pointer is pointing 
        #    at (or that there is a duplicate of the element that the pointer is pointing at in the unsorted subarray, and 
        #    both of which also happens to be the identified minimum element), then we will not do this swap, and hence not 
        #    execute anything in step 3

        #    This if statement checks for the aforementioned conditions above. It does this by checking if the element that
        #    the pointer is pointing at/the first element in the unsorted subarray ('i') is not equal to the 
        #    'minimum_element_index' after the seperate algorithm that finds and identify the smallest element in the
        #    unsorted List. If this is the case, then the minimum element found by this seperate algorithm is not the 
        #    the element that the pointer is pointing at/the first element in the unsorted subarray ('i'). We wil then execute
        #    the swapping process

        #    Conversely, if the element that the pointer is pointing at/the first element in the unsorted subarray ('i') is 
        #    equal to the 'minimum_element_index' even after the seperate algorithm that finds and identify the smallest 
        #    element in the unsorted List, then this means that the element the pointer is pointing at/the first element in 
        #    the unsorted subarray ('i') is the minimum element in the unsorted subarray as well. Hence we will not want to
        #    waste time carrying out the swap of the in the positions of the element that the pointer is pointing at, and 
        #    the minimum element identified by the seperate algorithm that finds the minimum element in a List, since they
        #    are the same element, and it is a waste of time to try to swap the position of an element with itself
        if number_list[i] != number_list[minimum_element_index]:

            #Note: Python allows you to use this one-liner code to swap the positions of 2 elements in a List too, but it 
            #may be abit more sophisticated. Here is the more primitive way of swapping the positions of 2 elements in a
            #List, using an extra 'temp' variable:
                # temp = number_list[i]
                # number_list[i] = number_list[minimum_element_index]
                # number_list[minimum_element_index] = temp
            number_list[i], number_list[minimum_element_index] = number_list[minimum_element_index], number_list[i]


if __name__ == '__main__':
    nums_list = [21, 38, 29, 17, 4, 25, 11]

    selection_sort(nums_list)

    print(nums_list)

    #We will try to run different testcases through our Selection Sort Algorithm to check if your program work for all these 
    #testcases to find any edge cases and cover/deal any details you may have missed if you do encounter any erorrs/bugs 
    #in one of these edge cases/testcases 
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [11, 2, 4, 7, 6],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [9, 11],
        [],
        [6]
    ]

    for elements in tests: 
        selection_sort(elements)
        print(elements)