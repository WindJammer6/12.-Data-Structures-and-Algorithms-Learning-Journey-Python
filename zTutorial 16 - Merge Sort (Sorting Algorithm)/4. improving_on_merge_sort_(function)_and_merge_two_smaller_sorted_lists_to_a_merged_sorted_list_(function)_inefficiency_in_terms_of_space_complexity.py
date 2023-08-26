#(I was kinda tired doing this tutorial... The contents may not be a very good/easy to understand explanation)


#What is the inefficiency in terms of space complexity of this implementation of Merge Sort Algorithm?
#We know that the Big O Notation of Space Complexity of an optimised Merge Sort Algorithm should be O(n) (I know its
#not good, but O(n) is already the most optimised Merge Sort Algorithm can be due to the nature of the Algorithm)

#The inefficiency arises when in the 'merge_two_smaller_sorted_lists_to_a_merged_sorted_list' function, we allocated
#new memory space when we created the 'merged_sorted_list' Python List and returned that 'merged_sorted_list' to the
#'merge_sort' function during its recursive loops in the Merge Sort Algorithm

#Hence, to tackle this inefficiency, it will be better if we modify the initial unsorted List in-place/itself 
#(original copy itself) instead

#To do this, we will need to not return anything from the 'merge_two_smaller_sorted_lists_to_a_merged_sorted_list'
#to the 'merge_sort' function, and not return anything from the 'merge_sort' function back to the main code

#So how can we do this? Here, we will modify both of these functions to remove the need for us to return anything
#in order to tackle to space complexity inefficiency in our Merge Sort Algorithm implementation


#Most of the modifications in the code to get this implementation of Merge Sort Algorithm to only modify the
#original copy of the initial unsorted List instead of creating new copies of the initial unsorted List and modifying
#them happens in this function

#We introduce a new parameter, 'array' to store our merged sorted List elements since after removing the 
#'merged_sorted_list' Python List, we have nowhere else to store our merged sorted List elements
def merge_two_smaller_sorted_lists_to_a_merged_sorted_list(smaller_sorted_list_a, smaller_sorted_list_b, array):

    #Removing the need for us to allocate new memory to store our merged sorted Lists, as we will just merge the 
    #smaller sorted Lists in-place
    # merged_sorted_list = []

    # i = j = 0
    i = j = k = 0

    while i < len(smaller_sorted_list_a) and j < len(smaller_sorted_list_b):
        if smaller_sorted_list_a[i] <= smaller_sorted_list_b[j]:
            #Modifying the in-place 'array' using the new pointer, 'k', instead of the previous 'merged_sorted_list'
            # merged_sorted_list.append(smaller_sorted_list_a[i])
            array[k] = smaller_sorted_list_a[i]
            i += 1

        else:
            #Modifying the in-place 'array' using the new pointer, 'k', instead of the previous 'merged_sorted_list'
            # merged_sorted_list.append(smaller_sorted_list_b[j])
            array[k] = smaller_sorted_list_b[j]
            j += 1
            
        #Incrementing the pointer 'k' in the 'array' after a new element has been added/changed in the 'array'
        k += 1


    while i < len(smaller_sorted_list_a):
        #Modifying the in-place 'array' using the new pointer, 'k', instead of the previous 'merged_sorted_list'
        # merged_sorted_list.append(smaller_sorted_list_a[i])
        array[k] = smaller_sorted_list_a[i]
        i += 1

        #Incrementing the pointer 'k' in the 'array' after a new element has been added/changed in the 'array'
        k += 1

    while j < len(smaller_sorted_list_b):
        #Modifying the in-place 'array' using the new pointer, 'k', instead of the previous 'merged_sorted_list'
        # merged_sorted_list.append(smaller_sorted_list_b[j])
        array[k] = smaller_sorted_list_b[j]
        j += 1

        #Incrementing the pointer 'k' in the 'array' after a new element has been added/changed in the 'array'
        k += 1


#Less of the important modifications in the code to get this implementation of Merge Sort Algorithm to only modify the
#original copy of the initial unsorted List instead of creating new copies of the initial unsorted List and modifying
#them is in this function
def merge_sort(array):

    if len(array) <= 1:
        return array
    
    middle_element_index = len(array)//2
    
    left_smaller_subarray = array[:middle_element_index]
    right_smaller_subarray = array[middle_element_index:]

    #We will remove the need to store anything from the recursive calls of the 'merge_sort' function since we will want to
    #modify this 'merge_sort' function such that it does not return anything. Since we will not be returning anything in the
    #'merge_sort' function, there is nothing for us to store in this recursive call of the 'merge_sort' function
    # left_smaller_subarray = merge_sort(left_smaller_subarray)
    # right_smaller_subarray = merge_sort(right_smaller_subarray)
    merge_sort(left_smaller_subarray)
    merge_sort(right_smaller_subarray)

    #Removing the need for us the return anything in this 'merge_sort' function, since there is nothing to return from the
    #'merge_two_smaller_sorted_lists_to_a_merged_sorted_list' function since this function will not be returning anything
    # return merge_two_smaller_sorted_lists_to_a_merged_sorted_list(left_smaller_subarray, right_smaller_subarray, array)
    merge_two_smaller_sorted_lists_to_a_merged_sorted_list(left_smaller_subarray, right_smaller_subarray, array)


if __name__ == '__main__':
    initial_unsorted_List = [21, 38, 29, 17, 4, 25, 32, 9]

    #Since the 'merge_sort' function is modifying the initial unsorted List in-place and is not returning anything,
    #there is no more need for us to check if the initial unsorted List has been sorted using the 'print()' function, but 
    #we can simply just call the 'merge_sort' function, then only use the 'print()' function on just the initial unsorted 
    #List afterwards to see that the original copy of the initial unsorted List has been modified/sorted

    # print(merge_sort(initial_unsorted_List))
    merge_sort(initial_unsorted_List)

    print(initial_unsorted_List)

    #We will try to run different testcases through our Merge Sort Algorithm to check if your program work for all these 
    #testcases to find any edge cases and cover/deal any details you may have missed if you do encounter any erorrs/bugs 
    #in one of these edge cases/testcases 
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)




#Previous idea explanation...

#For reference, from '1. What_is_Merge_Sort.txt',
    # For Big O Notation of Space Complexity of Merge Sort:
    # During step 2 of the Merge Sort Algorithm, during each stage of the merging process, temporary Lists/memory 
    # are allocated to hold the smaller subarrays being merged, which should be, in total, be the same size as the
    # initial unsorted List, n.

    # In between stages of the merging process, a new set of temporary Lists/memory of size n are allocated. But 
    # after every stage of the merging process, these temporary Lists/memory of size n, are freed/released and not 
    # used before moving on to the next stage of the merging process. Hence the overall space/memory required for 
    # the Merge Sort Algorithm throughout the stages of the merging process will remain stagnant at n, hence 
    # Big O Notation of Space Complexity of Merge Sort is O(n)

#However, up till now this implementation of Merge Sort Algorithm has a Big O Notation of Space Complexity even
#worse than O(n). This is because during each recursive loop in the merging process, when you are merging 2 sorted 
#smaller subarrays to create a merged sorted List in the 'merge_two_smaller_sorted_lists_to_a_merged_sorted_list' 
#function, you created a seperate List of size equal to the sum of the 2 sorted smaller subarrays, 
#'merged_sorted_list', allocating more memory space to store that merged sorted List. 

#Visualisation of memory space used in the space complexity inefficient Merge Sort Algorithm:
#1. During the breaking down of the initial unsorted List into smaller subarrays of one element each,
#               [21][38][29][17][4][25][32][9]
#                     /                 \
#       [21][38][29][17]               [4][25][32][9]
#         /          \                  /          \
#  [21][38]          [29][17]     [4][25]          [32][9]
#    /  \              /  \        /  \              /  \
# [21]  [38]        [29]  [17]   [4]  [25]        [32]  [9]

#2. During the merging process to create the sorted List,
# [21]  [38]        [29]  [17]   [4]  [25]        [32]  [9]
#    \  /              \  /        \  /              \  /
#  [21][38]          [17][29]     [4][25]          [9][32]
#        \            /                \            /
#       [17][21][29][38]               [4][9][25][32]
#                     \                 /
#               [4][9][17][21][25][29][32][38]

#Technically, this space complexity inefficient Merge Sort Algorithm has another flaw as during the breaking down 
#of the initial unsorted List in step 1, this space complexity inefficient Merge Sort Algorithm already made a full
#copy of this 'Merge Sort-Tree', which is already larger than the initial unsorted List (of size n), hence, even if
#we solve the space complexity inefficiency in the merging process in step 2, we will still have a implementation of
#Merge Sort Algorithm of a Big O Notation of Space Complexity worse than O(n), though improved. But in this
#tutorial, we will only solve the space complexity inefficiency in the merging process in step 2

#During the merging process, the space complexity inefficient Merge Sort Algorithm we implemented so far, allocated 
#new memory equal to this 'Merge Sort-Tree' (minus the top row, of smaller subarrays of one element each) as whenever 
#we run a recursive loop during the merging process, we allocated new memory space, when we created the 
#'merged_sorted_list' Python List variable, of size equal to the sum of the 2 sorted smaller subarrays. In this 
#example, that would be new memory space of 24 elements, even though the size of the initial unsorted List is just 8 
#elements.


#Hence, in order to prevent this, we can actually just reuse the memory space of the slightly larger, smaller 
#unsorted subarrays from the previous recursive loop during the breaking down of the initial unsorted List in step 1, 
#which we already created a full 'Merge Sort-Tree' of memory space (consisting of the unsorted smaller subarrays), as 
#we recursively rebound from the base case during recursionduring the merging process. E.g. Immediately after we 
#reached the base case for the smaller subarrays of one element each, one storing only the element '29' and the other 
#only storing the element '17', since during the breaking down stage in step 1, we actually already have the smaller 
#unsorted subarray of 2 elements, '[29,17]', we can instead of creating new memory space for this 'merged_sorted_list'
#in the 'merge_two_smaller_sorted_lists_to_a_merged_sorted_list' function, we can just reuse this smaller unsorted 
#subarray of 2 elements, '[29,17]', memory space, and just modify this memory space as we do the merging process 
#(creating a sorted List from merging 2 smaller, pre-sorted Lists) instead

#So, in order to do this, we need to try to do our merging process on any previous memory space created 
