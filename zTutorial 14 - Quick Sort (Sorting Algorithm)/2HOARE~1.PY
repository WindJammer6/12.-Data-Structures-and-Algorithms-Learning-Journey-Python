#What this function does is that it swaps the position of 2 elements in an array/Python List

#It takes in 'a' and 'b' parameters, representing the indexes of the 2 elements in the List to be swapped in their
#positions. (parameters are not taking the element's data/value since you might accidentally swap the wrong 2 elements 
#(swapping an elements at that another index that has the same data/value) if there are duplicates in said Array/Python 
#List)

#Note: The code logic below is a standard way of swapping 2 elements in an Array Data Structure in any programming 
#language
def swapping_two_elements_in_a_list(a, b, array):

    #This if statement checks if 'a' and 'b' the same index, or if the elements are both storing the same data/value, 
    #then we will not swap them, to save running time since there is no point in doing so if both elements are the same 
    #anyway. Only if both elements are not the same then we will do the swapping process of the 2 elements
    if array[a] != array[b] and a != b:
        temp = array[a]
        array[a] = array[b]
        array[b] = temp

        #Note: Python allows you to use this one-liner code to swap the positions of 2 elements in a List too, but it 
        #may be abit more sophisticated, so lets just stick to the more primitive way of implementing swapping of 2 elements 
        #in a List as shown above
            #array[a], array[b] = array[b], array[a]


#What this function does is that it implements Hoare Partition scheme, which is used for Partitioning in the
#Quick Sort Algorithm (see the 'quick_sort' function below)

#From '1. What_is_Quick_Sort.txt', for reference,
    # Here are the steps of Hoare Partition scheme:
    #(Sub-step 1a)
    # 1. Selecting a pivot. 

    #    Generally, you will want to pick the first element as your pivots for the Hoare Parititon scheme to 
    #    reduce any error even though technically selecting any element in your unsorted List can still work.

    #(Sub-step 1b)
    # 2. Introduce a 'start' and 'end' pointer where the first element is the 'start' pointer (since the first 
    #    element is the pivot in our example below, our 'start' pointer will be at the second element instead)
    #    and the last element is the 'end' pointer (in the case where we chose our pivots to be the last element,
    #    then the 'end' pointer will be at the second last element instead)

    # 3. We will start moving, and keep moving the 'start' pointer down the unsorted List until we find an 
    #    element that is strictly larger than the pivot and stop there ('strictly' because even if there is 
    #    duplicates, with a element equal to the pivot, we still will not stop there, in order for the 'start'
    #    pointer to stop, the element must be strictly larger). We will need to also include comparing if the 
    #    initial element position the 'start' pointer is at is larger than the pivot during the first iteration
    #    only (subsequent iteration there is no need to do so)

    # 4. Then, we will start moving, and keep moving the 'end' pointer up the unsorted List until we find an
    #    element that is smaller or equal to the pivot and stop there ('equal' as if there is duplicates, with 
    #    an element equal to the pivot, we will also stop there). We will need to also include comparing if the 
    #    initial element position the 'end' pointer is at is smaller than the pivot during the first iteration
    #    only (subsequent iteration there is no need to do so)

    # 5. Once both the 'start' and 'end' pointer has stopped, as they have found an element that is strictly 
    #    larger than pivot and an element smaller or equal to the pivot respectively, we will swap the positions 
    #    of the element that the 'start' pointer is currently at and the element the 'end' pointer is currently at
    #    (Unless the 'end' pointer has crossed the 'start' pointer, then this step will not run, and will jump to
    #    step 7 instead)

    # 6. Keep repeating steps 3 to 5 until the 'end' pointer crosses the 'start' pointer. 

    # 7. Once the 'end' pointer crosses the 'start' pointer (it will be at the element one index in front of 
    #    the 'start' pointer), do a swap in positions of the pivot and the element where the 'end' pointer 
    #    is currently at. After doing this, the pivot will automatically fall into the right position, with 
    #    all the remaining unsorted elements falling in the correct side with respect to the pivot (despite 
    #    that they may or may not become sorted with respect to the other elements at that same side)

def hoare_partition_scheme(number_list):

    #(Sub-step 1a)
    #1. Selecting the pivots (which will be the first element of every unsorted List)
    pivot_index = 0
    pivot = number_list[pivot_index]

    #(Sub-step 1b)
    #2. Introduce a 'start' and 'end' pointer where the first element is the 'start' pointer (since the first 
    #   element are the pivots, our 'start' pointer will be at the second element instead) and the last element 
    #   is the 'end' pointer

    #   In 'end_pointer = len(number_list) - 1' we use 'len(numbers_list) - 1' cuz Python Lists start with index 0,
    #   so the last element in the List will have the index of 'len(numbers_list) - 1')
    start_pointer = pivot_index + 1 
    end_pointer = len(number_list) - 1


    #6. Keep repeating steps 3 to 5 until the 'end' pointer crosses the 'start' pointer.
     
    #   The 2 inner while loops are only used to keep the 'start' pointer and  'end' pointer moving down the unsorted List until
    #   it finds an element that is strictly larger than the pivot and up the unsorted List until it finds an element that is 
    #   smaller or equal to the pivot respectively.

    #   We will need this outer while loop because during each recursive loop of Hoare Partition scheme, the 'start' pointer
    #   and 'end' pointer may stop at multiple elements, and do multiple swaps between the elements the 'start' pointer
    #   and 'end' pointer is pointing at when they stop until the 'end' pointer crosses the 'start' pointer. Hence this 
    #   outer while loop will allow to repeat the process of the step 3 to 5 (see above) until the 'end' pointer crosses the 
    #   'start' pointer, and is only then this while loop will break (so we can run the swap between the pivot and the element
    #   the 'end' pointer is pointing at in step 7)

    
    #   Regarding why we use '<=' instead of '<' is to consider edge cases where the List is sorted, with only has 2 elements. 
    #   You might think that using '<=' may mess up the case if 'start' pointer and 'end' pointer is pointing at the same element
    #   at the end of the 2 inner while loops, then the 'end' pointer wont be considered to have crossed the 'start' pointer
    #   but the swapping of pivot and the 'end' element (step 7) will still be executed regardless which shouldnt happen.
     
    #   But in cases where the unsorted List has more than 2 elements, after the 2 inner while loop, there shouldnt be a case
    #   of the 'start' pointer and 'end' pointers pointing at the same element anyway. At most the 'start' pointer may move 
    #   to point at the same element after the 'start' pointer's while loop, but the 'end' pointer's while loop will cause
    #   the 'end' pointer to cross the 'start' pointer after, and 'start' pointer and 'end' pointer will no longer point to
    #   the same element at the end of the outer while loop

    #   Using visualisation to demonstrate why we need the '<=' and not '<' for edge cases where the List is sorted, with only  
    #   2 elements,
    #   If we used the '<' operator,
        #   Initial pointer positions, and the List that is sorted, with only 2 elements at the start of Hoare Partition scheme:
        #       [9][11]             (Let 'p' be pivot,
        #        ^  /\                   's' be 'start' pointer,
        #      (p)(s)(e)                 'e' be 'end' pointer)

        #   Since 'start_pointer' == 'end'pointer', if we are using the '<' operator, the condition is not fulfilled, and the
        #   outer while loop will break immediately without running the code inside, and code to swap the pivot and the element
        #   at the 'end' pointer will run immediately, causing the the List to become unsorted instead

        #   List that is sorted, with only 2 elements at the end of Hoare Partition scheme:
        #       [11][9]        
        #        ^  /\                 
        #      (p)(s)(e)           

    #   If we used the '<=' operator,
        #   Initial pointer positions, and the List that is sorted, with only 2 elements at the start of Hoare Partition scheme:
        #       [9][11]             (Let 'p' be pivot,
        #        ^  /\                   's' be 'start' pointer,
        #      (p)(s)(e)                 'e' be 'end' pointer)

        #   Since 'start_pointer' == 'end_pointer', if we are using the '<=' operator, the condition is still fulfilled, and the
        #   outer while loop will not break, and the code inside will run. The 'start' pointer while loop will cause it to go 
        #   one index out of the List's index range, but that is fine (it wont cause any error). The 'end' pointer while loop
        #   will cause it to stop at the same element as the pivot.
        #   Pointer positions, and the List that is sorted, with only 2 elements during Hoare Partition scheme:
        #       [9][11]             (Let 'p' be pivot,
        #       / \     |                's' be 'start' pointer,
        #     (p) (e)  (s)               'e' be 'end' pointer)


        #   After one loop of the outer while loop, the outer while loop will break since now 'start_pointer' > 'end_pointer',
        #   and the code to swap the pivot and the element at the 'end' pointer will run, but since the pivot and 'end' pointer
        #   is pointing at the same element, there will be no changes to the List that is sorted of 2 elements despite after 
        #   the swapping process, which is ideal since no changes should be done to this List that is sorted of 2 elements since
        #   its already sorted
        #   List that is sorted, with only 2 elements at the end of Hoare Partition scheme:
        #       [9][11]             (Let 'p' be pivot,
        #       / \     |                's' be 'start' pointer,
        #     (p) (e)  (s)               'e' be 'end' pointer)

        #(refer to the 'sorted_list_of_two_elements' in the main code below, '[9, 11]')
    while start_pointer <= end_pointer:


        #3. We will start moving, and keep moving the 'start' pointer down the unsorted List until we find an 
        #   element that is strictly larger than the pivot and stop there ('strictly' because even if there is 
        #   duplicates, with a element equal to the pivot, we still will not stop there, in order for the 'start'
        #   pointer to stop, the element must be strictly larger). We will need to also include comparing if the 
        #   initial element position the 'start' pointer is at is larger than the pivot during the first iteration
        #   only (subsequent iteration there is no need to do so)

        #   So we used the '<=' operator in 'while number_list[start_pointer] <= pivot' so that only if when the 
        #   element the 'start' pointer is pointing is strictly larger than pivot then the while loop will be 
        #   broken


        #   Regarding why do we need to check the condition if 'start_pointer < len(number_list)', is to consider
        #   edge cases like the 'testcase_nums_list' unsorted List in the main code '[11, 2, 4, 7, 6]', since all the 
        #   elements in the unsorted List is smaller than the pivot, during the first recursive loop of Hoare Parititon 
        #   scheme, the 'start' pointer does not stop at any of the elements, and the 'start_pointer += 1' in this inner 
        #   while loop may cause the 'start' pointer to go our of the unsorted List's index range, creating an error 
        #   (since in this testcase, if 'start_pointer' == 6, 'number_list[6]' does not exist, and when you try to compare 
        #   'number_list[start_pointer] <= pivot', youll get an error). 

        #   However, in this testcase, at the end of this inner while loop, the 'start_pointer' will end up with an
        #   index of 5, which is also not an index that exist in the testcase's unsorted List. But why does it work? You
        #   can see this during debugging, at the second last loop, 'start_pointer' has an index of 4, which still 
        #   satisfies the condition of 'start_pointer < len(number_list)', and the code inside ('start_pointer += 1') runs,
        #   incrementing 'start_pointer' by 1, increasing to have an index of 5. It is only in the next loop, the condition
        #   'start_pointer < len(number_list)' is not met, and this while loop is broken. We will need the 'start_pointer'
        #   to have an index that is one index larger than the last element's index so that the 'end' pointer is considered 
        #   to have crossed the 'start' pointer, then we can carry out step 7, which is swap the pivot and the element the 
        #   'end' pointer is pointing at. If the 'start_pointer' only stops at index 4, which is the same index the 'end'
        #   pointer is pointing at, the 'end' pointer is not considered to have crossed the 'start' pointer, and we cannot
        #   carry out the last step 7.
        while start_pointer < len(number_list) and number_list[start_pointer] <= pivot:
            #The 'start' pointer will gradually go down the unsorted List, pointing at each element one index at a time 
            #down the unsorted List
            start_pointer += 1


        #4. Then, we will start moving, and keep moving the 'end' pointer up the unsorted List until we find an
        #   element that is smaller or equal to the pivot and stop there ('equal' as if there is duplicates, with 
        #   an element equal to the pivot, we will also stop there). We will need to also include comparing if the 
        #   initial element position the 'end' pointer is at is smaller than the pivot during the first iteration
        #   only (subsequent iteration there is no need to do so)

        #   So we used the '>' operator in 'while number_list[start_pointer] > pivot' so that if when the 
        #   element the 'start' pointer is pointing is smaller or equal to the pivot the while loop will be 
        #   broken
        while number_list[end_pointer] > pivot:
            #The 'end' pointer will gradually go up the unsorted List, pointing at each element one index at a time 
            #down the unsorted List
            end_pointer -= 1

        
        # 5. Once both the 'start' and 'end' pointer has stopped, as they have found an element that is strictly 
        #    larger than pivot and an element smaller or equal to the pivot respectively, we will swap the positions 
        #    of the element that the 'start' pointer is currently at and the element the 'end' pointer is currently at
        #    (Unless the 'end' pointer has crossed the 'start' pointer, then this step will not run, and will jump to
        #    step 7 instead)

        #   This if statement checks if, after the 2 while loops above (which moves the 'start' pointer and 'end' pointer) 
        #   only if the 'start' pointer is still in front of 'end' pointer, then we will run this swapping 
        #   process when both pointer has stopped. This is important as we don't want to do any swap between the elements
        #   the 'start' pointer and 'end' pointer is pointing at when 'end' pointer goes in front/crosses of the 
        #   'start' pointer, after the 2 while loops above (which moves the 'start' pointer and 'end' pointer) (after which 
        #   will break the outer while loop, where this will be the last loop). Which will be right before the last step 7 
        #   of one recursive loop of the Hoare Partition scheme when the element at the 'end' pointer swaps position with 
        #   the pivot. 

        #   Also note that here technically both the '<' and '<=' should work fine since even if after the 2 while loops
        #   above (which moves the 'start' pointer and 'end' pointer), the 'start' pointer and 'end' pointer end up 
        #   pointing at the same element (where 'start_pointer' == 'end_pointer'), the swap will not do anything. But 
        #   it'll save time to put '<' since it'll save time, removing the obsolete need for the program to run the swap 
        #   function when 'start_pointer' == 'end_pointer'
        if start_pointer < end_pointer:
            #Here we implemented seperately the 'swapping_two_elements_in_a_list' function to handle to code of swapping
            #of 2 elements in a List (see the 'swapping_two_elements_in_a_list' function above) (in this case its the
            #element that the 'start' pointer is currently at and the element the 'end' pointer is currently at when both
            #of them has stopped)
            swapping_two_elements_in_a_list(start_pointer, end_pointer, number_list) 


    #7. Once the 'end' pointer crosses the 'start' pointer (it will be at the element one index in front of 
    #   the 'start' pointer), do a swap in positions of the pivot and the element where the 'end' pointer 
    #   is currently at. After doing this, the pivot will automatically fall into the right position, with 
    #   all the remaining unsorted elements falling in the correct side with respect to the pivot (despite 
    #   that they may or may not become sorted with respect to the other elements at that same side) 

    #   Here we reused the 'swapping_two_elements_in_a_list' function to do the swap between the pivot and
    #   the the element the 'end' pointer is currently at after the 'end' pointer crosses the 'start' pointer
    swapping_two_elements_in_a_list(pivot_index, end_pointer, number_list)


#What this function does is that it implements Quick Sort Algorithm, but we will elaborate more about it 
#in this next file, '3. quick_sort_(function)_(incomplete)_(recursion_not_yet_implemented).py'
def quick_sort(number_list):
    hoare_partition_scheme(number_list)


if __name__ == '__main__':
    nums_list = [11, 9, 29, 7, 2, 15, 28]
    testcase_nums_list = [11, 2, 4, 7, 6]
    sorted_list_of_two_elements = [9, 11]

    quick_sort(nums_list)
    quick_sort(testcase_nums_list)
    quick_sort(sorted_list_of_two_elements)

    print(nums_list)
    print(testcase_nums_list)
    print(sorted_list_of_two_elements)

