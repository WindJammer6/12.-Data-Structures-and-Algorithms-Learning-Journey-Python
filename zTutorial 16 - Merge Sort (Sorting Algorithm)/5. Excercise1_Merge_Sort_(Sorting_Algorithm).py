#Question 1:

#Modify merge_sort function such that it can sort the following list of athletes as per the time taken by them in the marathon,
    #elements = [
    #        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
    #        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
    #        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
    #        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    #    ]


#the merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,
    #merge_sort(elements, key='time_hours', descending=True)

#This will sort elements by time_hours and your sorted list will look like,
    #elements = [
    #        {'name': 'rajab', 'age': 12, 'time_hours': 3},
    #        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
    #        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    #        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    #    ]


#if you call the merge_sort function like this,
    #merge_sort(elements, key='name')

#This will sort elements by name (alphabetical order) and your sorted list will look like,
    #elements = [
    #        { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
    #        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
    #        { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
    #        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
    #    ]

#My answer:
def modified_merge_two_smaller_sorted_lists_to_a_merged_sorted_list_in_ascending_order(smaller_sorted_list_a, smaller_sorted_list_b, array, sorting_dictionary_key):

    i = j = k = 0

    while i < len(smaller_sorted_list_a) and j < len(smaller_sorted_list_b):
        if smaller_sorted_list_a[i][sorting_dictionary_key] <= smaller_sorted_list_b[j][sorting_dictionary_key]:
            array[k] = smaller_sorted_list_a[i]
            i += 1

        else:
            array[k] = smaller_sorted_list_b[j]
            j += 1
        k += 1


    while i < len(smaller_sorted_list_a):
        array[k] = smaller_sorted_list_a[i]
        i += 1
        k += 1

    while j < len(smaller_sorted_list_b):
        array[k] = smaller_sorted_list_b[j]
        j += 1
        k += 1

def modified_merge_two_smaller_sorted_lists_to_a_merged_sorted_list_in_descending_order(smaller_sorted_list_a, smaller_sorted_list_b, array, sorting_dictionary_key):

    i = j = k = 0

    while i < len(smaller_sorted_list_a) and j < len(smaller_sorted_list_b):
        if smaller_sorted_list_a[i][sorting_dictionary_key] >= smaller_sorted_list_b[j][sorting_dictionary_key]:
            array[k] = smaller_sorted_list_a[i]
            i += 1

        else:
            array[k] = smaller_sorted_list_b[j]
            j += 1
        k += 1


    while i < len(smaller_sorted_list_a):
        array[k] = smaller_sorted_list_a[i]
        i += 1
        k += 1

    while j < len(smaller_sorted_list_b):
        array[k] = smaller_sorted_list_b[j]
        j += 1
        k += 1

def modified_merge_sort(array, sorting_dictionary_key, sort_in_descending_order=False):

    if sorting_dictionary_key != 'name' and sorting_dictionary_key != 'age' and sorting_dictionary_key != 'time_hours':
        print('Please enter an existing sorting category!')
        return

    if len(array) <= 1:
        return array
    
    middle_element_index = len(array)//2
    
    left_smaller_subarray = array[:middle_element_index]
    right_smaller_subarray = array[middle_element_index:]

    modified_merge_sort(left_smaller_subarray, sorting_dictionary_key, sort_in_descending_order)
    modified_merge_sort(right_smaller_subarray, sorting_dictionary_key, sort_in_descending_order)

    if sort_in_descending_order is False:
        modified_merge_two_smaller_sorted_lists_to_a_merged_sorted_list_in_ascending_order(left_smaller_subarray, right_smaller_subarray, array, sorting_dictionary_key)
    else:
        modified_merge_two_smaller_sorted_lists_to_a_merged_sorted_list_in_descending_order(left_smaller_subarray, right_smaller_subarray, array, sorting_dictionary_key)


if __name__ == '__main__':
    athlete_data = [
           { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
           { 'name': 'rajab', 'age': 12,  'time_hours': 3},
           { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
           { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
       ]
    
    modified_merge_sort(athlete_data, "name")
    print(athlete_data)

    modified_merge_sort(athlete_data, "age")
    print(athlete_data)

    modified_merge_sort(athlete_data, "time_hours")
    print(athlete_data)

    modified_merge_sort(athlete_data, "time_hours", sort_in_descending_order=True)
    print(athlete_data)


    #All works well, my answer looks correct, Solution is almost the same so won't be uploading Solution

