#Solution for Excerice 1 (my answer is in '5. Excercise1_Quick_Sort_(lomuto_partition_scheme_(function)).py')

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

#Solution:
def lomuto_partition_scheme(number_list, start_index_of_list, end_index_of_list):
    pivot = number_list[end_index_of_list]
    partition_index = start_index_of_list

    for i in range(start_index_of_list, end_index_of_list):
        if number_list[i] <= pivot:
            swapping_two_elements_in_a_list(i, partition_index, number_list)
            partition_index += 1

    swapping_two_elements_in_a_list(partition_index, end_index_of_list, number_list)

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
        [100, 80, 90, 70, 60, 50]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(elements)