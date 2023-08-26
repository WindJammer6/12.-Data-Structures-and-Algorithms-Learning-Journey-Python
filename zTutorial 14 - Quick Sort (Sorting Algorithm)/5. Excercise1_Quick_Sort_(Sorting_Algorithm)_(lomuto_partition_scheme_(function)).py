#Question 1:

#Implement Quick Sort Algorithm using Lomuto Partition scheme. This partition scheme is explained in the video 
#tutorial, you need to write python code to implement it.

#Check the pseudo code here: https://en.wikipedia.org/wiki/Quicksort, in the section about the Lomuto Partition
#scheme

def swapping_two_elements_in_a_list(a, b, array):
    if array[a] != array[b] and a != b:
        temp = array[a]
        array[a] = array[b]
        array[b] = temp

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

    return end_pointer


#My answer (with explanation on my logic of my attempt of implementing the code for the Lomuto Partition scheme): 

#From '1. What_is_Quick_Sort.txt', for reference,
    # Here are the steps of Lomuto Partition scheme:
    # (Sub-step 1a)
    # 1. Selecting a pivot. 

    #    Generally, you will want to pick the last element as your pivots for the Lomuto Parititon scheme to 
    #    reduce any error even though technically selecting any element in your unsorted List can still work
    #    as well

    # (Sub-step 1b)
    # 2. Introduce a 'partition index' pointer where the first element is the 'partition index' pointer.

    # 3. We will start moving, and keep moving the 'partition index' pointer down the unsorted List until we 
    #    find an element that is strictly larger than the pivot and stop there ('strictly' because even if there 
    #    is duplicates, with a element equal to the pivot, we still will not stop there, in order for the 'start'
    #    pointer to stop, the element must be strictly larger). We will need to also include comparing 
    #    if the initial element position the 'partition index' pointer is at is strictly larger than the pivot 
    #    during the first iteration only (subsequent iteration there is no need to do so)

    # 4. Then, we will introduce a new pointer, the 'index' pointer, which will initially point at the element 
    #    one index after where the 'partition index' has stopped, and start moving the 'index' pointer down 
    #    the unsorted List until we find an element that is smaller or equal to the pivot and stop there ('equal' 
    #    as if there is duplicates, with an element equal to the pivot, we will also stop there). We will 
    #    need to also include comparing if the initial element position the 'partition index' pointer is at is 
    #    smaller or equal to the the pivot during the first iteration only (subsequent iteration there is no need 
    #    to do so)

    # 5. Once both the 'partition index' and 'index' pointer has stopped, as they have found an element that is 
    #    strictly larger than pivot and an element smaller or equal to the pivot respectively, we will swap the 
    #    positions of the element that the 'partition index' pointer is currently at and the element the 'index' 
    #    pointer is currently at
    #    (Unless the 'index' pointer reaches the pivot, then this step will not run, and will jump to step 7 
    #    instead)

    # 6. Keep repeating steps 3 to 5 until the 'index' pointer reaches the pivot. 

    # 7. Once the 'index' pointer reaches the pivot (which it will stop at since the pivot is smaller or equal
    #    to the element the 'end' pointer is pointing at, which is also the pivot), do a swap in positions of 
    #    the pivot and the element where the 'partition index' pointer is currently at. After doing this, the 
    #    pivot will automatically fall into the right position, with all the remaining unsorted elements falling 
    #    in the correct side with respect to the pivot (despite that they may or may not become sorted with respect 
    #    to the other elements at that same side)
    
def lomuto_partition_scheme(number_list, start_index_of_list, end_index_of_list):
    #(Sub-step 1a) 
    #Step 1 of Lomuto Partition scheme
    pivot_index = end_index_of_list
    pivot = number_list[pivot_index]

    #(Sub-step 1b) 
    #During the first run of step 3 to 5 loop of this recursive loop of Lomuto Partition scheme (before step 6
    #comes in to repeat step 3 to 5 again of this recursive loop of Lomuto Partition scheme),
    #Step 2 of Lomuto Partition scheme
    partition_index = start_index_of_list
    
    #Step 3 of Lomuto Partition scheme
    while partition_index < pivot_index and number_list[partition_index] <= pivot:
        partition_index += 1


    #This if and else statement is to consider the edge cases where the unsorted List is already sorted, and
    #during the first time the 'partition_index' moves down the List, it immediately reaches the pivot (last
    #element in the List). Hence the 'index' pointer was never created.

    #Did the 'partition_index' reach the pivot in the first time the 'partition_index' moves down the List?
    #If it did not, create the 'index' pointer,
    if partition_index < pivot_index:
        #Step 4 of Lomuto Partition scheme, creating the 'index' pointer        
        index = partition_index + 1
    #If the 'partition_index' reach the pivot in the first time the 'partition_index' moves down the List, then
    #it means the unsorted List is already sorted, then we will simply just return 'partition_index' since it
    #will be the point of partitioning (see below's explanation at the 'return partition_index' code)
    else:
        return partition_index


    #Step 4 of Lomuto Partition scheme, moving the 'index' pointer down the unsorted List
    #(Note this also considers the fact if upon creation, if the 'index' pointer is already at the pivot, as
    #the code below will not run if 'index' pointer is already at pivot since if the 'index' pointer is at 
    #pivot, the element the 'index' pointer is at (the pivot) will be equal to the pivot and not '>' than
    #pivot, and the 'index' pointer will stop incrementing, which is the desired effect we want. Also, for this
    #case where the 'index' pointer is already at the pivot upon creation, the outer while loop below (where
    #'Step 6 of Lomuto Partition scheme' is at, which facilitates the repeating of steps 3 to 5 until the 
    #'index' pointer reaches the pivot, will not run at all since the 'index' pointer is already at the pivot, 
    #and in this case, it will jump to step 7, swapping the position of the pivot and the element the 'index'
    #pointer is pointing at at ending this recursive loop of Partitioning (Lomuto Partition scheme))
    while index < pivot_index and number_list[index] > pivot:
        index += 1


    #There is no need to run step 5 since the first time step 2 to 4 is run is hard-coded to consider cases 
    #where, 
        #1. the unsorted List is already sorted, and during the first time the 'partition_index' moves down 
        #   the List, it immediately reaches the pivot (last element in the List). Hence the 'index' pointer 
        #   was never created.
        #2. if upon creation, the 'index' pointer is already at the pivot

    #both of which cases, there is no need to do any swaps between the element the 'index' pointer and the 
    #'partition index' pointer are currently at


    #Step 6 of Lomuto Partition scheme (to repeat steps 3 to 5 (from the 2nd time onwards till 'index' pointer 
    #reaches the pivot), since the first time step 3 to 5 is run is hard-coded in the codes above)
    while index < pivot_index:

        #Step 3 of Lomuto Partition scheme
        while partition_index < pivot_index and number_list[partition_index] <= pivot:
            partition_index += 1

        #Step 4 of Lomuto Partition scheme, moving the 'index' pointer down the unsorted List (since the
        #'index' pointer is already created in the code above)
        while index < pivot_index and number_list[index] > pivot:
            index += 1

        #Step 5 of Lomuto Partition scheme
        if index < pivot_index:
            swapping_two_elements_in_a_list(partition_index, index, number_list)


    #Step 7 of Lomuto Partition scheme
    swapping_two_elements_in_a_list(pivot_index, partition_index, number_list)

    #Since during the recursive loops in the Quick Sort Algorithm ('quick_sort' function) (see below), we will need 
    #to return the point of partitioning, which is the point where the pivot will be at after it swaps positions with 
    #the element at the 'end' pointer. It needs to return this so that we will know where to mark out the boundaries 
    #for the smaller left and right sides/parts to do our Quick Sort Algorithm ('quick_sort' function) recursively. 
    
    #However, we cannot be returning the 'pivot_index' since the 'pivot_index' is technically not pointing at the 
    #point of partitioning at the end of one recursive loop of the Lomuto Partition scheme after the swap between
    #the pivot and the element at the 'partition index' pointer
        # Before the swap between the pivot and the element at the 'partition index' pointer (after 'index' pointer 
        # reaches the pivot pointer):
        #       ----------                       (Let 'p' be pivot,
        #       |        |                            'par' be 'partition index' pointer,
        #      \ /      \ /                           'i' be 'index' pointer)
        #       0  1  2  3   4   5   6 
        #     [11][9][2][7][15][29][28]
        #                        ^  /\   
        #                    (par)(i)(p)

        # Before the swap between the pivot and the element at the 'partition index' pointer (after 'index' pointer 
        # reaches the pivot pointer):
        #      0  1  2   3   4   5   6 
        #     [7][9][2][11][15][28][29]
        #                        ^  /\   
        #                    (par)(i)(p)

    #Notice that after the swap between the pivot and the element at the 'partition index' pointer the pointer at 
    #the point of partitioning ('28') is not the pivot pointer (it is still pointing at whatever the last element 
    #at index 6 is), but the 'partition index' pointer. Hence, we will return the 'partition index' pointer as the 
    #point of partitioning instead of the pivot 
    return partition_index


def quick_sort(number_list, start_index_of_list, end_index_of_list):

    if start_index_of_list >= end_index_of_list:
        return

    else:
        partitioning_point = lomuto_partition_scheme(number_list, start_index_of_list, end_index_of_list)
        quick_sort(number_list, start_index_of_list, partitioning_point - 1)
        quick_sort(number_list, partitioning_point + 1, end_index_of_list)


if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [11, 2, 4, 7, 6],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [9, 11],
        [],
        [6],
        [10, 7, 8, 9, 1, 5],
        [3, 0, 6, 2, 4, 9],
        [15, 12, 10, 18, 5, 9],
        [15, 20, 15, 10, 15, 30],
        [100, 80, 90, 70, 60, 50],
        [4, 3, 2, 6, 7, 4, 8, 4]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(elements)

#My answer works to sort the testcases of various unsorted List, however Solution looks more optimised and concise
#(see '5. Excercise1(Solution)_Quick_Sort_(lomuto_partition_scheme_(function)).py')