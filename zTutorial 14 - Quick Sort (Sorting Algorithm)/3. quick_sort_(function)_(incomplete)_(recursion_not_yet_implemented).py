def swapping_two_elements_in_a_list(a, b, array):
    if array[a] != array[b] and a != b:
        temp = array[a]
        array[a] = array[b]
        array[b] = temp

def hoare_partition_scheme(number_list):
    #(Sub-step 1a) 
    #Step 1 of Hoare Partiton scheme
    pivot_index = 0
    pivot = number_list[pivot_index]

    #(Sub-step 1b) 
    #Step 2 of Hoare Partiton scheme
    start_pointer = pivot_index + 1
    end_pointer = len(number_list) - 1

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


#What this function does is that it implements Quick Sort Algorithm.

#From '1. What_is_Quick_Sort.txt', for reference,
    # Here are the steps of Quick Sort Algorithm:
    # 1. During the first recursive loop of Partitioning on the initial unsorted List,

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

def quick_sort(number_list):

        #1. During the first recursive loop of Partitioning (via Hoare Parititon scheme in this tutorial) on the 
        #   initial unsorted List, which covers the sub-steps 1a and 1b (see the 'hoare_partition_scheme' 
        #   function above))
        hoare_partition_scheme(number_list)

        #2. See the next file '4. implementing_recursion_to_hoare_partition_scheme_(function)_and_quick_sort_(function).py'


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



#Notice that for now, the Hoare Partition scheme ('hoare_partition_scheme' function) and Quick Sort Algorithm 
#('quick_sort' function) is sort of hard-coded, and is only running one loop of (Hoare Partition scheme) 
#Partitioning. So how can we implement the recursion aspect to allow our program to do multiple recursive 
#loops (checking the left and right side/parts of the pivot recursively) until the unsorted List becomes sorted?