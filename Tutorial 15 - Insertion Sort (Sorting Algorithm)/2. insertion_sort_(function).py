#What this function does is that it implements Insertion Sort Algorithm.

#From '1. What_is_Insertion_Sort.txt', for reference,
# Here are the steps of Insertion Sort Algorithm:
# 1. Split the unsorted array/List into 2 subarrays, the sorted subarray and unsorted subarray. We will do this 
#    by creating a pointer pointing to the second element of the unsorted List. 

#    (Note: Why didn't we create the pointer pointing at the first element of the unsorted List? There is no nned
#    to do this since we would want to start the Insertion Sort Algorithm with at least an element in the sorted
#    subarray (elements at the left side of the pointer). We don't have to worry about trying to sort the first 
#    element being inserted/transferred to the sorted subarray since it will be empty initially, and when there
#    is only one element in a List, that List is automatically considered sorted without having to try to sort it)

#    This pointer acts as as a divider, where,
#    -> the elements on the left side of the pointer is part of the sorted subarray
#    -> the elements on the right side of the pointer is part of the unsorted subarray
#    -> the element the pointer is pointing at will be the element we want to insert/transfer over from the 
#       unsorted subarray to the sorted subarray. 
#       => before it is inserted/transferred over from the unsorted subarray to the sorted subarray, it will be 
#          considered part of the unsorted subarray
#       => after it is inserted/transferred over from the unsorted subarray to the sorted subarray, it will be 
#          considered part of the sorted subarray

# 2. Compare the element that the pointer is pointing at with the existing elements in the sorted subarray to find 
#    the correct position in the sorted subarray for the inserted element such that the sorted subarray remains 
#    sorted. 
#    (Before the element that the pointer is pointing at is inserted/transferred over from the unsorted subarray 
#    to the sorted subarray, it will be considered part of the unsorted subarray)
         
#    Insert/Transfer the over the element that the pointer is pointing at from the unsorted subarray to 
#    the sorted subarray. 
#    (After the element that the pointer is pointing at is inserted/transferred over from the unsorted subarray 
#    to the sorted subarray, it will be considered part of the sorted subarray)

#    Note: - How exactly (the exact algorithmic steps) we will be finding the correct position for the inserted 
#            element in the sorted aubarray such that the sorted subarray remains sorted will be further 
#            discussed when we are implementing the Insertion Sort Algorithm in code in 
#            '2. insertion_sort_(function).py'
#          - You can think of it as at the end of step 2, the size of the sorted subarray will increase by 1, 
#            while the size of the unsorted subarray will decrease by 1

# 3. Move the pointer down the unsorted List, to the next index/element (unless you've reached the end of the
#    unsorted List)

# 4. Repeat steps 2 and 3 iteratively for each element in the unsorted List


def insertion_sort(number_list):

    # 4. Repeat steps 2 and 3 iteratively for each element in the unsorted List

    #    Here we will iterate through each element in the unsorted List
    for i in range(1, len(number_list)):

        #(Steps 1 and 3)
        # 1. Split the unsorted array/List into 2 subarrays, the sorted subarray and unsorted subarray. We will do this 
        #    by creating a pointer pointing to the second element of the unsorted List. 
        
        #    During the starting iteration for the second element, we created the pointer, which we will called an
        #    'anchor', which will be pointing at the second element, which will be stored in this 'anchor' variable

        #    Also note that we were able to create the pointer pointing at the second element by in the line of code
        #    above 'for i in range(1, len(number_list))', the 'range()' function has the starting index of 1 (second 
        #    element instead of 0 (first element)


        # 3. Move the pointer down the unsorted List, to the next index/element

        #    At the start of every iteration after the starting iteration, the element the pointer is pointing at
        #    will be shifted to the next element in the unsorted List from the previous element during the previous
        #    iteration
        anchor = number_list[i]


        # 2. Compare the element that the pointer is pointing at with the existing elements in the sorted subarray to find 
        #    the correct position in the sorted subarray for the inserted element such that the sorted subarray remains 
        #    sorted. 
                
        #    Insert/Transfer the over the element that the pointer is pointing at from the unsorted subarray to 
        #    the sorted subarray. 


        #    We didn't cover exactly how to do this step 2 of Insertion Sort algorithmically in 
        #    '1. What_is_Insertion_Sort.txt'. So here we will cover this,

        #Here are the steps:
        #   2a. Introduce a pointer pointing at the element one index to the left of the inserted element (which will
        #       be in the sorted subarray)

        #   2b. This pointer will be traversing in reverse down the sorted subarray, and comparing each element in the
        #       sorted subarray to the inserted element in order to find the correct position in the sorted subarray 
        #       for the inserted element such that the sorted subarray remains sorted. 
        #         b(i) If the element in the sorted subarray that this pointer is pointing at is larger than 
        #              the inserted element, we will first need to sort of 'shift' the element this pointer is pointing 
        #              at to the right to sort of 'make space' to insert/transfer the inserted element from the 
        #              unsorted subarray to the sorted subarray when we do find a correct position for it. We will do
        #              this by copy-pasting the element this pointer is pointing at to also be the element on the 
        #              right (such as there is now a duplicate of the element this pointer is pointing at on the index 
        #              at the right). After which, we will shift the pointer to point at the previous element (the 
        #              element one index to the left) in the sorted subarray (reverse traversing), and repeat step b.
        # 
        #              (Note: During the first time (for each inserted element) if this sub-step b(i) is run, the element
        #              on the right of the element this pointer is pointing at is coincidentally also the inserted 
        #              element. By copy-pasting the element this pointer is pointing at to this right element 
        #              (inserted element), we are effectively deleting the inserted element from the unsorted List. 
        #              then we will sort of continue reverse traversing and comparing elements to the inserted element 
        #              down the sorted subarray. You might be wondering how can we retrieve the inserted element now 
        #              that you have deleted it from the unsorted List. Not to worry since your 'anchor' variable from
        #              the code above will be holding onto the inserted element so you don't have to worry about the 
        #              inserted element being lost.)

        #         b(ii)If,
        #              -> the element in the sorted subarray that this pointer is pointing at is, smaller or equal to 
        #                 ('equal' so if there are duplicates, with the element in the sorted subarray being equal to 
        #                 the inserted element, we will also carry out this sub-step b(ii) instead of continuing reverse 
        #                 traversing and comparing elements down the sorted subarray in sub-step b(i)) the inserted element, 
        #              -> if the pointer goes out of the sorted subarray (which indicates all the elements in the sorted 
        #                 subarray are larger than the inserted element), 

        #              then we have found its correct position in the sorted subarray (which will be the position one index 
        #              after the element the pointer is pointing at in the sorted subarray that is smaller or equal to the 
        #              inserted element). In the case if the pointer goes out of the sorted subarray, it will pointing at 
        #              one index to the left of the first element, at index -1 (which the correct position, which is the
        #              position one index after the element the pointer is pointing at, will be the element at index 0,
        #              the first element, at the beginning of the sorted subarray). We will then insert/transfer the 
        #              inserted element into the correct position (the position one index after the element in the sorted 
        #              subarray that is smaller or equal to the inserted element) using the 'anchor' variable, which stored 
        #              the inserted element seperately since we cannot retrieve it from the unsorted List anymore as it is 
        #              of deleted if the element on the immediate left of the inserted element is not smaller or equal 
        #              to the inserted element. When this sub-step b(ii) runs, this marks the end of a step 2 of the 
        #              Insertion Sort Algorithm for the iteration of this inserted element.
        # 
        #              (Note, for cases if the element on the immediate left of the inserted element is smaller or equal to 
        #              the inserted element, sub-step b(i) will never had run for that inserted element, and the inserted 
        #              element will never have been deleted (see the 'note' section in sub-step b(i) above). Then the 
        #              correct position in the sorted subarray for the inserted element would be the inserted element's 
        #              initial position.)


        #    Lets say we are currently in the third iteration, where the pointer is pointing at the fourth element 
        #    ('17'), and we are going to insert/transfer the fourth element ('17') from the unsorted subarray to the sorted 
        #    subarray in such a way such that the sorted subarray remains sorted. 

        #    Visualisation of how step 2 of Insertion Sort Algorithm works algorithmically:
        #    a. First we will introduce a new pointer, 'j', initially pointing at the element one index to the left of 
        #       the inserted element ('38') (which will be in the sorted subarray). (Let the variable 'i' represent the 
        #       inserted element ('17') for this iteration that will be the element we want to insert/transfer over from 
        #       the unsorted subarray to the sorted subarray)
        #            ss           us                     
        #       <----------><------------->                  'anchor' (variable) = 17
        #       [21][29][38][17][4][25][11]
        #                 ^   ^
        #                (j) (i) 

        #       (Note that in an earlier line of code we have also stored in the inserted element ('17') into the 'anchor' 
        #       variable)

        #    b. Next, we will compare the inserted element ('17') to the element the pointer 'j' is pointing at in the sorted 
        #       subarray (currently its the element '38')

        #  (first time Step b(i) is run for the third iteration)
        #  b(i) Since the element in the sorted subarray that this pointer is pointing at ('38') is larger than the inserted
        #       element ('17'), we will first need to sort of 'shift' the element this pointer is pointing at ('38') to the 
        #       right to sort of 'make space' to insert/transfer the inserted element ('17') from the unsorted subarray to 
        #       the sorted subarray when we do find a correct position for it. We will do this by copy-pasting the element 
        #       this pointer is pointing at ('38') to also be the element on the right
        #            ss           us                     
        #       <----------><------------->                  'anchor' (variable) = 17
        #       [21][29][38][38][4][25][11]
        #                 ^   ^
        #                (j) (i) 

        #       We will now shift the pointer 'j' to point at the previous element (the element one index to the left) ('29')
        #       in the sorted subarray (reverse traversing).
        #            ss           us                     
        #       <----------><------------->                  'anchor' (variable) = 17
        #       [21][29][38][38][4][25][11]
        #             ^       ^
        #            (j)     (i) 

        #       (Note that since this the first time during this iteration that step b(i) is run, the inserted element 
        #       ('17') got effectively deleted from the unsorted List. Hence, we needed to save the inserted element ('17') 
        #       earlier in this code, which we did, storing it in the 'anchor' variable in order to prevent the inserted 
        #       element ('17') from being lost)

        #  (second time Step b(i) is run for the third iteration)
        #  b(i) Since the element in the sorted subarray that this pointer is pointing at ('29') is larger than the inserted
        #       element ('17'), we will first need to sort of 'shift' the element this pointer is pointing at ('29') to the 
        #       right to sort of 'make space' to insert/transfer the inserted element ('17') from the unsorted subarray to 
        #       the sorted subarray when we do find a correct position for it. We will do this by copy-pasting the element 
        #       this pointer is pointing at ('29') to also be the element on the right
        #            ss           us                     
        #       <----------><------------->                  'anchor' (variable) = 17
        #       [21][29][29][38][4][25][11]
        #             ^       ^  
        #            (j)     (i) 

        #       We will now shift the pointer 'j' to point at the previous element (the element one index to the left) ('21')
        #       in the sorted subarray (reverse traversing).
        #            ss           us                     
        #       <----------><------------->                  'anchor' (variable) = 17
        #       [21][29][29][38][4][25][11]
        #         ^           ^
        #        (j)         (i) 

        #  (third time Step b(i) is run for the third iteration)
        #  b(i) Since the element in the sorted subarray that this pointer is pointing at ('21') is larger than the inserted
        #       element ('17'), we will first need to sort of 'shift' the element this pointer is pointing at ('21') to the 
        #       right to sort of 'make space' to insert/transfer the inserted element ('17') from the unsorted subarray to 
        #       the sorted subarray when we do find a correct position for it. We will do this by copy-pasting the element 
        #       this pointer is pointing at ('21') to also be the element on the right
        #            ss           us                     
        #       <----------><------------->                  'anchor' (variable) = 17
        #       [21][21][29][38][4][25][11]
        #         ^           ^
        #        (j)         (i) 

        #       We will now shift the pointer 'j' to point at the previous element (the element one index to the left) ('29')
        #       in the sorted subarray (reverse traversing).
        #            ss           us                     
        #       <----------><------------->                  'anchor' (variable) = 17
        #       [21][21][29][38][4][25][11]
        #     ^               ^
        #    (j)             (i) 
      
        #       (Note that the pointer 'j' is now out of the range of the unsorted List, pointing at index -1)

        # b(ii)For the insertion/transfer of this inserted element ('17') is the special case where its correct position lies
        #      as the first element in the sorted subarray, In such cases, the pointer will go out of range like so, pointing
        #      at index -1, and the correct position in the sorted subarray, will be the position one index after the element 
        #      the pointer is pointing at, at the element at index 0, the first element in the sorted subarray since all the 
        #      elements in the sorted subarray currently are all larger than the inserted element ('17'). We will then
        #      insert/transfer the inserted element ('17'), using the 'anchor' variable, to the correct position in the sorted
        #      subarray, at index 0 of the unsorted List.
        #            ss           us                     
        #       <----------><------------->                  'anchor' (variable) = 17
        #       [17][21][29][38][4][25][11]
        #     ^               ^
        #    (j)             (i) 

        


        #   2a. Introduce a pointer pointing at the element one index to the left of the inserted element (which will
        #       be in the sorted subarray)
        j = i - 1
        
        #   2b. This pointer will be traversing in reverse down the sorted subarray (via the while loop and the code 'j -= 1'
        #       in the while loop), and comparing each element in the sorted subarray to the inserted element in order to find 
        #       the correct position in the sorted subarray for the inserted element such that the sorted subarray remains 
        #       sorted. 

        #       b(i) If both the conditions, 'j >= 0' and 'anchor < number_list[j]' are True, then the while loop will run,
        #            and the element the pointer 'j' is pointing at will sort of 'shift' to the right by copy-pasting the 
        #            element this pointer is pointing at to also be the element on the right (such as there is now a duplicate 
        #            of the element this pointer is pointing at on the index at the right) by the line of code
        #            'number_list[j + 1] = number_list[j]'. 
        
        #            The pointer 'j' is then shifted to point at the previous element (the element one index to the left) in 
        #            the sorted subarray (reverse traversing) by the line of code 'j -= 1'
        #             
        #       b(ii) -> The condition, 'anchor < number_list[j]' checks if the element the pointer 'j' is pointing at in
        #                the sorted subarray is larger than the inserted element. If it is not (means it is smaller or equal
        #                to the inserted element), then this while loop will be terminated, as the correct position has been 
        #                found (at the position one index after the element the pointer 'j' is pointing at) and the code 
        #                after this while loop will run.
        #             -> The condition, 'j >= 0' checks if the pointer 'j' is still in range of the unsorted List. If it is not, 
        #                like in the special case like above where the pointer 'j' becomes index -1, then the while loop will also
        #                be terminated, as the correct position has been found (at index 0 of the unsorted List) and the code 
        #                after this while loop will run.
        while j >= 0 and anchor < number_list[j]:
            number_list[j + 1] = number_list[j]
            j -= 1
        
        #   b(ii) Here is when the while loop is broken, and the correct position in the sorted subarray is found. We will then 
        #         insert/transfer the inserted element into the sorted subarray from the unsorted subarray using the 'anchor'
        #         variable
        number_list[j + 1] = anchor



if __name__ == '__main__':
    nums_list = [21, 38, 29, 17, 4, 25, 11]

    insertion_sort(nums_list)
    
    print(nums_list)

    #We will try to run different testcases through our Insertion Sort Algorithm to check if your program work for all these 
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
        insertion_sort(elements)
        print(elements)
