#What this function does is that it creates a sorted List from merging 2 smaller, pre-sorted Lists, which are
#passed as arguments 'smaller_sorted_list_a' and 'smaller_sorted_list_b'. This function is created to carry 
#out each of the merging process in each stage in step 2 of the Merge Sort Algorithm 

#From '1. What_is_Merge_Sort.txt', for reference,
#Here are the steps to create a sorted List from merging 2 smaller, pre-sorted Lists:
# a. First, create a seperate empty array, which will be the merged sorted List 
# b. Then, initiate 2 pointers, with each pointer pointing at the first element in the each of the smaller 
#    sorted List 
# c. Now we will compare the 2 elements in each respective smaller sorted Lists that their own pointer is 
#    pointing at. Whichever element that each smaller sorted Lists' pointer is pointing at is smaller, will 
#    be appended into the Merged Sorted List (in the case where both elements that each smaller sorted 
#    Lists' pointer is pointing at is equal due to the presence of duplicates in the initial unsorted List, 
#    we can decide to append either of the elements from either of the smaller sorted Lists that their 
#    pointer is pointing at into the Merged Sorted List)
# d. The smaller sorted List that has its element appended into the Merged Sorted List will then have to 
#    shift its pointer one index to the right, and now should be pointing at the next element in that smaller 
#    sorted List (unless that element being appended into the Merged Sorted List is the last element of that 
#    smaller sorted List, then we will not shift the pointer one index to the right, and we will just keep it 
#    pointing at the last element of that smaller sorted List)
# e. Repeat steps c and d iteratively until all the elements in the 2 smaller sorted Lists have been appended
#    to the merged sorted List

def merge_two_smaller_sorted_lists_to_a_merged_sorted_list(smaller_sorted_list_a,smaller_sorted_list_b):

    #a. First, create a seperate empty array, which will be the merged sorted List 
    merged_sorted_list = []

    #b. Then, initiate 2 pointers, with each pointer pointing at the first element in the each of the smaller 
    #   sorted List, which will have an index of 0 in their own respective smaller sorted List

    #   In this code, 'i' will be the pointer in 'smaller_sorted_list_a' and 'j' will be the pointer in 
    #   'smaller_sorted_list_b'
    i = j = 0


    # e. Repeat steps c and d iteratively until all the elements in the 2 smaller sorted Lists have been appended
    #    to the merged sorted List

    #    In order to do this, we will create a while loop, which will keep looping while both the pointers 'i' and
    #    'j' remain within the index range of 'smaller_sorted_list_a' and 'smaller_sorted_list_b' respectively.

    #    There is a bug in this logic however. Using the example from the main code, where,
    #       'smaller_sorted_list_a' being '[17, 21, 29, 38]'
    #       'smaller_sorted_list_b' being '[4, 9, 25, 32]'

    #    if this function only contains this while loop, it will return an output of,
    #       'merged_sorted_list' being '[4, 9, 17, 21, 25, 29, 32]'

    #    Notice that it is missing the element '38'. The bug here is during the iteration where the else statament 
    #    was ran, where pointer 'j' in 'smaller_sorted_list_b' was already at its last element, which was appended 
    #    into the 'merged_sorted_list', and the pointer 'j' was subsequently shifted one index to the right in the
    #    code 'j += 1', shifting it out of the index range of 'smaller_sorted_list_b'. 

    #    When this occured, this prevented the next while loop iteration from running and the while loop will 
    #    terminate here, without appending the last element in 'smaller_sorted_list_a', '38', that pointer 'i' in 
    #    the 'smaller_sorted_list_a' is currently at in the next while loop iteration. Hence, in order to solve 
    #    this bug, we need to add the 2 other while loops after this while loop (see the 2 other while loops
    #    further below in this function)
    while i < len(smaller_sorted_list_a) and j < len(smaller_sorted_list_b):

        # c. Now we will compare the 2 elements in each respective smaller sorted Lists that their own pointer is 
        #    pointing at. Whichever element that each smaller sorted Lists' pointer is pointing at is smaller, will 
        #    be appended into the Merged Sorted List (in the case where both elements that each smaller sorted 
        #    Lists' pointer is pointing at is equal due to the presence of duplicates in the initial unsorted List, 
        #    we can decide to append either of the elements from either of the smaller sorted Lists that their 
        #    pointer is pointing at into the Merged Sorted List)
        
        #    In the case where both elements that each smaller sorted Lists' pointer is pointing at is equal due to 
        #    the presence of duplicates in the initial unsorted List, we have decided upon appending the element
        #    from 'smaller_sorted_list_a' that its pointer 'i' is pointing at into the 'merged_sorted_list'

        #    In this if statement, we will check if the element in 'smaller_sorted_list_a' that its pointer 'i' is 
        #    pointing at smaller than or equal to the element in 'smaller_sorted_list_b' that its pointer 'j' is
        #    is pointing at. If it is, then we will append the element in 'smaller_sorted_list_a' that its pointer 
        #    'i' is pointing at into the 'merged_sorted_list'
        if smaller_sorted_list_a[i] <= smaller_sorted_list_b[j]:
            merged_sorted_list.append(smaller_sorted_list_a[i])

            # d. The smaller sorted List that has its element appended into the Merged Sorted List will then have to 
            #    shift its pointer one index to the right, and now should be pointing at the next element in that smaller 
            #    sorted List (unless that element being appended into the Merged Sorted List is the last element of that 
            #    smaller sorted List, then we will not shift the pointer one index to the right, and we will just keep it 
            #    pointing at the last element of that smaller sorted List)

            #    In this if statement, since the element in 'smaller_sorted_list_a' that its pointer 'i' is pointing 
            #    at is the one being appended into the 'merged_sorted_list', we will only shift the pointer 'i' in the
            #    'smaller_sorted_list_a' one index to the right, while keeping the pointer 'j' in the 
            #    'smaller_sorted_list_b' static in its position
            i += 1

        # c. Now we will compare the 2 elements in each respective smaller sorted Lists that their own pointer is 
        #    pointing at. Whichever element that each smaller sorted Lists' pointer is pointing at is smaller, will 
        #    be appended into the Merged Sorted List (in the case where both elements that each smaller sorted 
        #    Lists' pointer is pointing at is equal due to the presence of duplicates in the initial unsorted List, 
        #    we can decide to append either of the elements from either of the smaller sorted Lists that their 
        #    pointer is pointing at into the Merged Sorted List)

        #    In the case where both elements that each smaller sorted Lists' pointer is pointing at is equal due to 
        #    the presence of duplicates in the initial unsorted List, we have decided upon appending the element
        #    from 'smaller_sorted_list_a' that its pointer 'i' is pointing at into the 'merged_sorted_list'

        #    In this else statement, we will check if the element in 'smaller_sorted_list_a' that its pointer 'i' is 
        #    pointing at larger than the element in 'smaller_sorted_list_b' that its pointer 'j' is pointing at. If 
        #    it is, then we will append the element in 'smaller_sorted_list_b' that its pointer 'j' is pointing at 
        #    into the 'merged_sorted_list'
        else:
            merged_sorted_list.append(smaller_sorted_list_b[j])

            # d. The smaller sorted List that has its element appended into the Merged Sorted List will then have to 
            #    shift its pointer one index to the right, and now should be pointing at the next element in that smaller 
            #    sorted List (unless that element being appended into the Merged Sorted List is the last element of that 
            #    smaller sorted List, then we will not shift the pointer one index to the right, and we will just keep it 
            #    pointing at the last element of that smaller sorted List)

            #    In this if statement, since the element in 'smaller_sorted_list_b' that its pointer 'j' is pointing 
            #    at is the one being appended into the 'merged_sorted_list', we will only shift the pointer 'j' in the
            #    'smaller_sorted_list_a' one index to the right, while keeping the pointer 'i' in the 
            #    'smaller_sorted_list_a' static in its position
            j += 1


    #These 2 while loops solve the bug in the code/while loop that implements step e of 'creating a sorted List from 
    #merging 2 smaller, pre-sorted Lists' above

    #They solve this by, 
    #-> if the pointer 'j' in 'smaller_sorted_list_b' is the one that went out of index range first after its last 
    #   element is appended into the 'merged_sorted_list' before the pointer 'i' in 'smaller_sorted_list_a' goes out
    #   of index range, without being able to append all its remaining elements into the 'merged_sorted_list', then 
    #   we will manually append all the remaining elements in the 'smaller_sorted_list_a' into the 'merged_sorted_list'
    #   in this while loop, and incrementing the pointer 'i' in the process in 'smaller_sorted_list_a' until the pointer
    #   'i' goes out of index range before breaking out of this while loop
    while i < len(smaller_sorted_list_a):
        merged_sorted_list.append(smaller_sorted_list_a[i])
        i += 1

    #-> if the pointer 'i' in 'smaller_sorted_list_a' is the one that went out of index range first after its last 
    #   element is appended into the 'merged_sorted_list' before the pointer 'j' in 'smaller_sorted_list_b' goes out
    #   of index range, without being able to append all its remaining elements into the 'merged_sorted_list', then 
    #   we will manually append all the remaining elements in the 'smaller_sorted_list_b' into the 'merged_sorted_list'
    #   in this while loop, and incrementing the pointer 'j' in the process in 'smaller_sorted_list_b' until the pointer
    #   'j' goes out of index range before breaking out of this while loop
    while j < len(smaller_sorted_list_b):
        merged_sorted_list.append(smaller_sorted_list_b[j])
        j += 1


    #Returning the 'merged_sorted_list' at the end of this function of the 2 smaller sorted Lists, 'smaller_sorted_list_a'
    #and 'smaller_sorted_list_b'
    return merged_sorted_list


if __name__ == '__main__':
    #Here, we will just create 2 pre-sorted smaller sorted Lists 1 and 2 as inputs to test out our 
    #'merge_two_smaller_sorted_lists_to_a_merged_sorted_list' function. When we implement Merge Sort Algorithm later in
    #'3. merge_sort_(function)_(incomplete)_(inefficient_in_terms_of_space_complexity).py' then we will create an initial 
    #unsorted List as input into our Merge Sort Algorithm ('merge_sort' function) in the main code here
    smaller_sorted_list_1 = [17, 21, 29, 38]
    smaller_sorted_list_2 = [4, 9, 25, 32]
    
    print(merge_two_smaller_sorted_lists_to_a_merged_sorted_list(smaller_sorted_list_1, smaller_sorted_list_2))