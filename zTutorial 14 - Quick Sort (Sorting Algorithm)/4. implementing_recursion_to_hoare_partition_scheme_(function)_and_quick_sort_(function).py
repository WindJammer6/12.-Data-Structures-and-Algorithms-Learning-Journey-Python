#In this file, we will implement the recursion aspect to allow our program to do multiple recursive loops (checking 
#the left and right side/parts of the pivot recursively) until the unsorted List becomes sorted. To do that, we
#will need to make modifications to our Hoare Partition scheme ('hoare_partition_scheme' function) and Quick Sort 
#Algorithm ('quick_sort' function) 


def swapping_two_elements_in_a_list(a, b, array):
    if array[a] != array[b] and a != b:
        temp = array[a]
        array[a] = array[b]
        array[b] = temp

#Notice that we modified the 'hoare_partition_scheme' function to take in 2 more parameters, 'start_index_of_list' 
#and 'end_index_of_list'. These parameters represents the start and end index boundaries in the unsorted List that 
#we want to sort the unsorted List (E.g. if 'start_index_of_list is 0 and 'end_index_of_list' is 3, we will only 
#be sorting the portion of the unsorted List from elements at index 0 to 3)

#Obviously, we would want to be sorting the full sorted number List input most of the time, so these 2 additional
#parameters are more for getting the recursion loop to work (you'll understand after looking at the code in the 
#'hoare_partition_scheme' function)
def hoare_partition_scheme(number_list, start_index_of_list, end_index_of_list):
    #(Sub-step 1a) 
    #Step 1 of Hoare Partiton scheme
    pivot_index = start_index_of_list
    pivot = number_list[pivot_index]

    #(Sub-step 1b) 
    #Step 2 of Hoare Partiton scheme
    start_pointer = pivot_index + 1
    end_pointer = end_index_of_list

    #Step 6 of Hoare Partiton scheme
    while start_pointer <= end_pointer:

        #Step 3 of Hoare Partiton scheme
        while start_pointer < len(number_list) and number_list[start_pointer] <= pivot:
            start_pointer += 1

        #Step 4 of Hoare Partiton scheme
        while number_list[end_pointer] > pivot:
            end_pointer -= 1

        #Step 5 of Hoare Partiton scheme
        if start_pointer < end_pointer:
            swapping_two_elements_in_a_list(start_pointer, end_pointer, number_list)  
            
    #Step 7 of Hoare Partiton scheme
    swapping_two_elements_in_a_list(pivot_index, end_pointer, number_list)

    #Since during the recursive loops in the Quick Sort Algorithm ('quick_sort' function) (see below), we will need 
    #to return the point of partitioning, which is the point where the pivot will be at after it swaps positions with 
    #the element at the 'end' pointer. It needs to return this so that we will know where to mark out the boundaries 
    #for the smaller left and right sides/parts to do our Quick Sort Algorithm ('quick_sort' function) recursively. 
    
    #However, we cannot be returning the 'pivot_index' since the 'pivot_index' is technically not pointing at the 
    #point of partitioning at the end of one recursive loop of the Hoare Partition scheme after the swap between
    #the pivot and the element at the 'end' pointer
        # Before the swap between the pivot and the element at the 'end' pointer (after 'end' pointer crosses the 'start' 
        # pointer):
        #       ----------                       (Let 'p' be pivot,
        #       |        |                            's' be 'start' pointer,
        #      \ /      \ /                           'e' be 'end' pointer)
        #       0  1  2  3   4   5   6 
        #     [11][9][2][7][29][15][28]
        #       ^        ^   ^ 
        #      (p)      (e) (s)

        # After the swap between the pivot and the element at the 'end' pointer (after 'end' pointer crosses the 'start' 
        # pointer):
        #      0  1  2   3   4   5   6 
        #     [7][9][2][11][29][15][28]
        #      ^         ^   ^ 
        #     (p)       (e) (s)

    #Notice that after the swap between the pivot and the element at the 'end' pointer the pointer at the point of
    #partitioning ('11') is not the pivot pointer (it is still pointing at whatever the first element at index 0 is), but 
    #the 'end' pointer. Hence, we will return the 'end' pointer as the point of partitioning instead of the pivot 
    return end_pointer



#What this function does is that it implements Quick Sort Algorithm.

#From '1. What_is_Quick_Sort.txt', for reference,
    # Here are the steps of Quick Sort Algorithm:
    # 1. During the first recursive loop of Partitioning on the initial unsorted List. 

    #    There are 2 ways of doing this step, via the Hoare Partition scheme (which is more commonly
    #    used, and is the scheme we will be using to implement the process of Partitioning in this 
    #    tutorial) or the Lomuto Parititon scheme. We will look at these 2 Partitioning schemes later.

    #    These are the general sub-steps on how the process of Partitioning is done (these sub-steps are
    #    are common steps shared between the Hoare Partition scheme and Lomuto Partition scheme):
    #    a. Selecting a pivot
    #    b. Put the pivot in the correct position while in the process, re-shuffle the remaining unsorted 
    #       elements such that they fall in the correct side with respect to the pivot (but they may or may 
    #       not become sorted with respect to the other elements at that same side)

    # 2. After the first loop of partioning on the initial unsorted List, we will be left with 2 parts, the 
    #    left side of the pivot and right side of the pivot. For each individual side,
    #    -> If that side has 0 or 1 elements, then that side is considered 'sorted' and there is no need 
    #       to do further partitioning on that side, and we can stop the recursive loop for that side
    #    -> Else if that side has more than 1 element, then we will recursively repeat more loops of the same
    #       partioning process (Hoare Partition scheme or Lomuto Partition scheme, repeating step 1a and 1b) 
    #       on that side

#Here we will make our Quick Sort Algorithm ('quick_sort' function) recursive. 

#Notice that we will have to take in the same 2 more parameters as the 'hoare_partition_scheme' function, 
#'start_index_of_list' and 'end_index_of_list' in order to get the recursion loop to work 
def quick_sort(number_list, start_index_of_list, end_index_of_list):
    
    # 2. -> If that side has 0 or 1 elements, then that side is considered 'sorted' and there is no need 
    #       to do further partitioning on that side, and we can stop the recursive loop for that side

    #       When doing recursion, we will always need to create a base case, in this case it is if a unsorted List part has only 
    #       one element where 'start_index_of_list == end_index_of_list' or is empty, which may cause 
    #       'start_index_of_list >= end_index_of_list' so there's no need to sort these unsorted List parts. The 'quick_sort' 
    #       function simply returns without doing anything during those recursive loops
    if start_index_of_list >= end_index_of_list:
        return

    else:
        #(Steps 1 and 2)
        #    Here, will run our each recursive loop of Partitioning (Hoare Parititon scheme), then storing the returned point of
        #    partitioning (see hoare_partition_scheme' function above on its return value) in the variable 'partitioning_point'
        partitioning_point = hoare_partition_scheme(number_list, start_index_of_list, end_index_of_list)


        # 2. -> Else if that side has more than 1 element, then we will recursively repeat more loops of the same
        #       partioning process (Hoare Partition scheme or Lomuto Partition scheme, repeating step 1a and 1b) 
        #       on that side

        #       We will then recursively call the 'quick_sort' function on the left partition and right partition with respect
        #       to the 'partitioning_point'. 
        
        #We recursively call the left partition by letting the 'end_index_of_list' be 'partitioning_point - 1' instead, while 
        #keeping the 'start_index_of_list'
        quick_sort(number_list, start_index_of_list, partitioning_point - 1)
        
        #We recursively call the right partition by letting the 'start_index_of_list' be 'partitioning_point + 1' instead, while 
        #keeping the 'end_index_of_list'
        quick_sort(number_list, partitioning_point + 1, end_index_of_list)


if __name__ == '__main__':
    #We will try to run different testcases through our Quick Sort Algorithm to check if your program work for all these 
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

    #Running each testcases with our Quick Sort Algorithm to see if they work
    for elements in tests:
        #Here use 'len(numbers_list) - 1' cuz Python Lists start with index 0,
        #so the last element in the List will have the index of 'len(numbers_list) - 1')    
        quick_sort(elements, 0, len(elements) - 1)
        print(elements)

