def merge_two_smaller_sorted_lists_to_a_merged_sorted_list(smaller_sorted_list_a,smaller_sorted_list_b):

    merged_sorted_list = []

    i = j = 0

    while i < len(smaller_sorted_list_a) and j < len(smaller_sorted_list_b):
        if smaller_sorted_list_a[i] <= smaller_sorted_list_b[j]:
            merged_sorted_list.append(smaller_sorted_list_a[i])
            i += 1

        else:
            merged_sorted_list.append(smaller_sorted_list_b[j])
            j += 1


    while i < len(smaller_sorted_list_a):
        merged_sorted_list.append(smaller_sorted_list_a[i])
        i += 1

    while j < len(smaller_sorted_list_b):
        merged_sorted_list.append(smaller_sorted_list_b[j])
        j += 1

    return merged_sorted_list


#What this function does is that it implements Merge Sort Algorithm.

#Here are the steps of Merge Sort Algorithm:
# 1. Break down the initial unsorted List by recursively breaking down the initial unsorted List and the 
#    subsequent smaller subarrays by half and half again (if the initial unsorted List/subsequent smaller 
#    subarray is an odd number, then we will just split it into 2 smaller subarrays of different lengths,
#    with the maximum difference in length between these 2 smaller subarrays of different lengths of 1),
#    until we are left with just smaller subarrays of one element each.

#    (Even if a particular subsequent smaller subarray is coincidentally sorted, we will still continue 
#    to break down this coincidentally sorted smaller subarray (the reason why we don't keep this 
#    coincidentally sorted smaller subarray is explained above in the 'What is Merge Sort?' section))

# 2. Now we will merge each of these smaller subarrays of one element each. We will need to merge them
#    (via the merging process on how to create a sorted List from merging 2 smaller, pre-sorted Lists as we 
#    have learnt above) in reverse of the recursive loops was used to break the initial unsorted List down 
#    into smaller subarrays of one element each in step 1, after the recursive loop reaches the base case. 
#    (which is when the length of a smaller subarray is 1 (it only contains one element)).
   
#    The merging process will be what we learnt in the section above, creating a sorted List from 
#    merging 2 smaller, pre-sorted Lists. We will start from the smaller subarrays of one element each.
#    Since these smaller subarrays of one element each can be automatically considered sorted, we can apply
#    this method to merge 2 of these smaller subarrays of one element each into a merged sorted List (which
#    will now contain 2 elements).
   
#    Here are the steps to create a sorted List from merging 2 smaller, pre-sorted Lists:
#    a. First, create a seperate empty array, which will be the Merged Sorted List 
#    b. Then, initiate 2 pointers, with each pointer pointing at the first element in the each of the smaller 
#       sorted List 
#    c. Now we will compare the 2 elements in each respective smaller sorted Lists that their own pointer is 
#       pointing at. Whichever element that each smaller sorted Lists' pointer is pointing at is smaller, will 
#       be appended into the Merged Sorted List (in the case where both elements that each smaller sorted 
#       Lists' pointer is pointing at is equal due to the presence of duplicates in the initial unsorted List, 
#       we can decide to append either of the elements from either of the smaller sorted Lists that their 
#       pointer is pointing at into the Merged Sorted List)
#    d. The smaller sorted List that has its element appended into the Merged Sorted List will then have to 
#       shift its pointer one index to the right, and now should be pointing at the next element in that smaller 
#       sorted List (unless that element being appended into the Merged Sorted List is the last element of that 
#       smaller sorted List, then we will not shift the pointer one index to the right, and we will just keep it 
#       pointing at the last element of that smaller sorted List)
#    e. Repeat steps c and d iteratively until all the elements in the 2 smaller sorted Lists have been appended
#       to the Merged Sorted List
      
#    Then, we will need to repeat this same method for the now slightly larger, smaller subarrays of 2 elements,
#    merging 2 such slightly larger, smaller subarrays of 2 elements into a Merged Sorted List (which will now 
#    contain 4 elements) and so on... until we get back a Merged Sorted List, containing all the elements of 
#    the initial unsorted List, except that this List is now sorted

#   (Note: Its too difficult to accurately pinpoint where in the code each step 1 and 2 is being executed in
#          the Merge Sort Algorithm ('merge_sort' function) since the recursion sort of tackles both steps 
#          simultaneously during its recursive loops)

#   The 'array' parameter represents the initial unsorted List, and any subsequent smaller subarrays during the 
#   recursive loops when this function recursively calls itself

def merge_sort(array):

    #When doing recursion, we will always need to create a base case, or the exit/rebound condition, in this case 
    #this will be as we keep halving/breaking down the initial unsorted List into smaller subarrays, until we get 
    #smaller subarrays of only size 1, indicating it contains only one element

    #We will also take into consideration '<= 1' instead of just '== 1' to tell our program that it will also be a 
    #base case, or the exit/rebound condition, if a smaller subarray dosen't exists and we will still just treat
    #it as a base case, or the exit/rebound condition. 

    #Usually we wont hit the base case where a smaller subarray will be size of 0 before hitting the base case 
    #where the smaller subarray will be size of 1, it is just to consider edge cases such as if the input initial
    #unsorted List is already an empty List, '[]' where the initial 'smaller subarray' is immediately already
    #be size of 0.
    if len(array) <= 1:

        #In order to create this 'rebound' effect, in reverse back through the recursion stack, we will return the
        #smaller subarray which will be stored in the 'array' variable from the previous recursive loop in this
        #recursive 'merge_sort' function
        return array
    
    #Here is the code to find the middle element's index. The double backslash '//' is to obtain an integer output
    #to be stored in the 'middle_element_index' variable. 
    
    #For odd number sized smaller subarrays, the code, 'len(array)//2' will return the integer output index for 
    #the middle element's index. For even number sized smaller subarrays, the code, 'len(array)//2' will return the 
    #integer output index for right element among the 2 elements sharing the middle of the smaller subarray. (With
    #a bit of thinking, youll know why, wont explain it here, just note that the '//' will round down the output
    #if that output is a float with decimals to the nearest whole number integer)
    middle_element_index = len(array)//2

    #Here is where we will break down the initial unsorted List/any subsequent smaller subarrays that are the size
    #of '> 1' into smaller subarrays by splitting the initial unsorted List/any subsequent smaller subarrays that 
    #are the size of '> 1' by half in the middle via List indexing ('[:middle_element_index]' and 
    #'[middle_element_index:]) using the 'middle_element_index', assigning them as the left and right smaller
    #subarrays
    left_smaller_subarray = array[:middle_element_index]
    right_smaller_subarray = array[middle_element_index:]

    #Here is where we will recursively call the 'merge_sort' function. But what is the new 'left_smaller_subarray'
    #'right_smaller_subarray' storing exactly? And where is it getting the stored data from?

    #There is 2 possible places where the new 'left_smaller_subarray' and 'right_smaller_subarray' can get the
    #stored data from:
    #-> The first place is from the 'return array' code in the base case earlier in this function, when we hit the 
    #   base case when we broke down the initial unsorted List repeatedly recursively until we obtained smaller
    #   subarrays of size 1, only containing one element each. These smaller subarrays of size 1, only containing
    #   one element each is returned in the base case in the next recursive loop, and the recursion stack 
    #   unwinds/rebounds, and is stored in this new 'left_smaller_subarray' or 'right_smaller_subarray'

    #-> The second place is from the 
    #   'return merge_two_smaller_sorted_lists_to_a_merged_sorted_list(left_smaller_subarray, right_smaller_subarray)'
    #   code at the end of this 'merge_sort' function, when after the base case is hit, and while the recursion stack
    #   unwinds/rebounds, smaller sorted left and right subarrays that were broken down earlier in the recursion loops
    #   are merged back, into a merged sorted List (that was initially unsorted during the breaking down step 1).

    #   'return merge_two_smaller_sorted_lists_to_a_merged_sorted_list(left_smaller_subarray, right_smaller_subarray)'
    #   code is effectively returning a function. But since in the 
    #   'merge_two_smaller_sorted_lists_to_a_merged_sorted_list()', it returns the 'merged_sorted_list' (see in the
    #   'merge_two_smaller_sorted_lists_to_a_merged_sorted_list()' function), what the new 'left_smaller_subarray' 
    #   and 'right_smaller_subarray' are effectively storing in this case will be 'merged_sorted_list' during the 
    #   subsequent unwinds/rebounds of the recursion stack after the recursion hit the base case
    left_smaller_subarray = merge_sort(left_smaller_subarray)
    right_smaller_subarray = merge_sort(right_smaller_subarray)

    return merge_two_smaller_sorted_lists_to_a_merged_sorted_list(left_smaller_subarray, right_smaller_subarray)


    #Here is ChatGPT's attempt to explan all the crazy recursiveness:
    # Certainly! I'll walk you through the recursive steps of the merge_sort function using the input list 
    # [21, 38, 29, 17, 4, 25, 32, 9].

    # 1. Initial Call:
    #    The input list is [21, 38, 29, 17, 4, 25, 32, 9].

    # 2. Splitting:
    #    The middle index is calculated as len(array)//2, which is 4. This means the list is split into two smaller 
    #    subarrays:

    #    - left_smaller_subarray = [21, 38, 29, 17]
    #    - right_smaller_subarray = [4, 25, 32, 9]

    # 3. Recursion:
    #    Both left_smaller_subarray and right_smaller_subarray are recursively passed into the merge_sort function. 
    #    This process continues until the base case is reached, where a subarray with only one element is returned.
    #    -> For left_smaller_subarray:
    #       Middle index: len(array)//2 = 2
    #       left_smaller_subarray = [21, 38]
    #       right_smaller_subarray = [29, 17]
    #       After recursive calls, the subarrays will be further divided until they each contain only one element.

    #    -> For right_smaller_subarray:
    #       Middle index: len(array)//2 = 2
    #       left_smaller_subarray = [4, 25]
    #       right_smaller_subarray = [32, 9]
     
    # 4. Merging:
    #    The recursive calls start to return sorted subarrays. These sorted subarrays are then merged back together 
    #    using the merge_two_smaller_sorted_lists_to_a_merged_sorted_list function. The merging process combines the 
    #    elements in a sorted manner.
    #    -> For left_smaller_subarray and right_smaller_subarray:
    #       left_smaller_subarray after sorting: [21, 38]
    #       right_smaller_subarray after sorting: [17, 29]
         
    #    -> For left_smaller_subarray and right_smaller_subarray:
    #       left_smaller_subarray after sorting: [4, 25]
    #       right_smaller_subarray after sorting: [9, 32]
     
    # 5. Second Last Merging:
    #    The two merged subarrays (left_smaller_subarray and right_smaller_subarray) are merged once again to create 
    #    the second last (largest) sorted smaller arrays.

    #    The result of merging [21, 38] and [17, 29] is [17, 21, 29, 38].
    #    The result of merging [4, 25] and [9, 32] is [4, 9, 25, 32].

    # 6. Final Merging and Result:
    #    Finally, the two merged subarrays [17, 21, 29, 38] and [4, 9, 25, 32] are merged to produce the fully sorted 
    #    array [4, 9, 17, 21, 25, 29, 32, 38].

    # That's the step-by-step explanation of how the merge_sort function works with the given input list. The recursive 
    # nature of the algorithm helps to repeatedly divide and sort the input until the final sorted array is achieved.


if __name__ == '__main__':
    initial_unsorted_List = [21, 38, 29, 17, 4, 25, 32, 9]
    
    print(merge_sort(initial_unsorted_List))