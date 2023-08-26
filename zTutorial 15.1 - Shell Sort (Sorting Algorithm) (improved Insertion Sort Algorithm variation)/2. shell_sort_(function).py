#What this function does is that it implements Shell Sort Algorithm.

#From '1. What_is_Shell_Sort.txt', for reference,
# Here are the steps of Shell Sort Algorithm:
# 1. Shell Sort Algorithm uses the concept of a gap. You can technically start with a gap of any number, and you
#    can decide how you want to decrement it as well every time when the gap is decreased (until when gap becomes 1).
#    Usually, Shell Sort uses a gap that is half the size of the initial unsorted List, and we will decrement the gap 
#    by half after every gap's iteration (if this gap's iteration's gap is a float/has decimals due to the size of the 
#    initial unsorted List being an odd number, then just round down that number to the nearest whole number/integer 
#    (e.g. if initial unsorted List size is 9, 9 /2 = 4.5 ~(round down) 4 (which will be this gap's iteration's gap)))

#    Note: - There are other methods to decide on the size of the gap and how much to decrement it after each gap's
#            iteration but this is the most common method
#          - If the gap value is a decimal due to the initial unsorted List having an odd number size, or the previous
#            gap value is an odd number, and you got a decimal gap value after halving, just round down that decimal 
#            gap value to the nearest whole number/integer

# 2. We will then create a pointer pointing at the element with index equal to the gap

# 3. So what does this gap mean? It means that you will have to carry out Insertion Sort at every 'gap'th element in the 
#    initial unsorted List to the left of the element this pointer is pointing at inclusive, which will form the smaller 
#    subarray. 

#    Note: - The smaller subarray does not always only consist of 2 elements. It can contain as many elements as long 
#            as they are the 'gap'th elements in the initial unsorted List (that will be seperated by the gap) to the 
#            left of the element the pointer 'p' is pointing at inclusive, while we are still within the index range 
#            of the initial unsorted List/that the 'gap'th element exists in the initial unsorted List

# 4. After carrying out Insertion Sort on the smaller subarray, we will move the pointer one index to the right 
#    (just one index to the right, not by the gap!) 

# 5. Repeat steps 3 and 4 until the pointer reaches the end of the initial unsorted List

# 6. After the pointer has reached the end of the initial unsorted List, we will decrement the gap by half 
#    (if this gap's iteration's gap is a float/has decimals due to the previous gap's iteration's gap being an odd
#    number, then just round down that number to the nearest whole number/integer (e.g. if previous gap's iteration's
#    gap is 7, 7/2 = 3.5 ~(round down) 3 (which will be this gap's iteration's gap)))

#    Also notice that the initial unsorted List, after running Insertion Sort through the smaller subarrays, and 
#    semi-iterating via the pointer through the initial unsorted List, the larger elements in the initial unsorted List
#    have now moved towards the end of the initial unsorted List, and vice versa (smaller elements in the initial 
#    unsorted List towards the front of the initial unsorted List). Hence, Insertion Sort should now require fewer 
#    number of comparison and shifting operations being done in step 2b(i), thanks to Shell Sort Algorithm. You can 
#    clearly see this from the comparison below. This is how Shell Sort solves the problem of Insertion Sort (see 'So 
#    what is the problem of Insertion Sort Algorithm that Shell Sort Algorithm solves?' section above)

# 7. Repeat steps 2 to 6 until gap is less than 1. The last gap's iteration will be guranteed to be gap as 1, 
#    regardless of the initial gap value that the Shell Sort algorithm started with (which depends on the size of
#    the initial unsorted List)(e.g. 15 /2 ~ 7 /2 ~ 3 /2 ~ 1,  or  9 /2 ~ 4 /2 ~ 2 /2 ~ 1)

#    (Note: In code we will just put create step 7 via a while loop, with the condition 'gap > 0' or 'gap >= 1' since
#    we want to cut this while loop at the end of the gap (1) iteration, and after the gap is further halved, and 
#    rounded down (1 /2 ~ 0.5 ~(round down) ~ 0), gap will definiely be 0 at the next iteration/less than one, proving
#    these conditions to be false, and causing the while loop to stop running and exit out of it)


def shell_sort(number_list):

    # 1. Shell Sort Algorithm uses the concept of a gap. You can technically start with a gap of any number, and you
    #    can decide how you want to decrement it as well every time when the gap is decreased (until when gap becomes 1).
    #    Usually, Shell Sort uses a gap that is half the size of the initial unsorted List, and we will decrement the gap 
    #    by half after every gap's iteration (if this gap's iteration's gap is a float/has decimals due to the size of the 
    #    initial unsorted List being an odd number, then just round down that number to the nearest whole number/integer 
    #    (e.g. if initial unsorted List size is 9, 9 /2 = 4.5 ~(round down) 4 (which will be this gap's iteration's gap)))

    #    Here, will use the '//' operator, which will half the value of the length of the unsorted initial List, and 
    #    rounding down the output if that output is a float with decimals to the nearest whole number/integer)
    gap = len(number_list)//2

    # 7. Repeat steps 2 to 6 until gap is less than 1. The last gap's iteration will be guranteed to be gap as 1, 
    #    regardless of the initial gap value that the Shell Sort algorithm started with (which depends on the size of
    #    the initial unsorted List)(e.g. 15 /2 ~ 7 /2 ~ 3 /2 ~ 1,  or  9 /2 ~ 4 /2 ~ 2 /2 ~ 1)

    #    (Note: In code we will just put create step 7 via a while loop, with the condition 'gap > 0' or 'gap >= 1' since
    #    we want to cut this while loop at the end of the gap (1) iteration, and after the gap is further halved, and 
    #    rounded down (1 /2 ~ 0.5 ~(round down) ~ 0), gap will definiely be 0 at the next iteration/less than one, proving
    #    these conditions to be false, and causing the while loop to stop running and exit out of it)
    while gap > 0:
        
        
        #~~~(Start of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~


        # 4. After carrying out Insertion Sort on the smaller subarray, we will move the pointer one index to the right 
        #    (just one index to the right, not by the gap!) 

        # 5. Repeat steps 3 and 4 until the pointer reaches the end of the initial unsorted List

        #    Steps 4 and 5 of Shell Sort Algorithm is done by this for loop, which will 'loop' steps 3 and 4 (it technically
        #    doesnt really loop step 2, even though the line of code that implements step 2 is within this for loop, 
        #    you can look at the explanation for the line of code implementing step 2 below) 
         
        #    (Explanation for how this for loop does step 4)
        #    It does step 4 because after every loop, it shifts the pointer one index to the right in the initial unsorted 
        #    List to iterate through the elements starting from the element with index equal to the gap of that gap iteration 
        #    to the last element/end of the initial unsorted List

        #    (Explanation for how this for loop does step 5)
        #    It does step 5 because within this for loop, it contains the codes that implements steps 3, and this code
        #    itself does step 4 after every loop (see above 'Explanation for how this for loop does step 4'). Also, it tells
        #    the program to start at the element with index equal to the gap (from the 'gap' parameter in the 'range()'
        #    function) and stop at the end of the initial unsorted List (from the 'len(number_list)' parameter)
        for i in range(gap, len(number_list)):
            
            # 2. We will then create a pointer pointing at the element with index equal to the gap

            #    During the first loop of the for loop, this line of code executes step 2, which is initiating a pointer
            #    pointing at the element with index equal to the gap, since during the first loop of the for loop, variable 'i'
            #    is the element at the 'gap'th index. It then stores the element the pointer is pointing at into the 'anchor'
            #    variable

            #    However, for subsequent loops, this line of code is not running step 2, but is just storing the element the 
            #    pointer is pointing at (of the index stored in variable 'i') into the 'anchor' variable
            anchor = number_list[i]

            # 3. So what does this gap mean? It means that you will have to carry out Insertion Sort at every 'gap'th element in the 
            #    initial unsorted List to the left of the element this pointer is pointing at inclusive, which will form the smaller 
            #    subarray. 

            #    These codes here is almost identical as the code executing steps 2a and 2b, 2b(i) and 2b(ii) in the 
            #    Insertion Sort Algorithm (see '2. insertion_sort_(function).py' in the 
            #    'Tutorial 15 - Insertion Sort (Sorting Algorithm)' tutorial). But notice that unlike Insertion Sort, in Shell Sort, 
            #    these almost-identical codes have the '1's replaced by the 'gap' variable instead, which is a difference 
            #    between Shell Sort (elements are selected with gaps) and Insertion Sort (elements are selected without gaps/they
            #    are adjacent to each other)
            j = i - gap

            while j >= 0 and anchor < number_list[j]:
                number_list[j + gap] = number_list[j]
                j -= gap

            number_list[j + gap] = anchor


        #~~~(End of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~


        # 6. After the pointer has reached the end of the initial unsorted List, we will decrement the gap by half 
        #    (if this gap's iteration's gap is a float/has decimals due to the previous gap's iteration's gap being an odd
        #    number, then just round down that number to the nearest whole number/integer (e.g. if previous gap's iteration's
        #    gap is 7, 7/2 = 3.5 ~(round down) 3 (which will be this gap's iteration's gap)))

        #    Here, will use the '//' operator, which will half the value of the gap from the previous gap iteration, and 
        #    rounding down the output if that output is a float with decimals to the nearest whole number/integer)
        gap = gap // 2


if __name__ == '__main__':
    nums_list = [70, 3, 1, 56, 34, 12, 9, 13, 80]

    shell_sort(nums_list)
    
    print(nums_list)

    #We will try to run different testcases through our Shell Sort Algorithm to check if your program work for all these 
    #testcases to find any edge cases and cover/deal any details you may have missed if you do encounter any erorrs/bugs 
    #in one of these edge cases/testcases 
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [5]
    ]

    for elements in tests:
        shell_sort(elements)
        print(elements)