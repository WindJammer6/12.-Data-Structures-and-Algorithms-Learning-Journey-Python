#Solution for Excerice 1 (my answer is in '3. Excercise1_Selection_Sort_(Sorting_Algorithm).py')

#What this solution is doing is essentially this:
# def modified_selection_sort(number_list, c):
#     for i in range(len(number_list) - 1):
#         minimum_element_index = i

#         for j in range(i + 1, len(number_list)):
#             if number_list[j][c] < number_list[minimum_element_index][c]:
#                 minimum_element_index = j

#         if number_list[i][c] != number_list[minimum_element_index][c]:
#             number_list[i], number_list[minimum_element_index] = number_list[minimum_element_index], number_list[i]

# def multilevel_selection_sort(number_list, column_sorting_priority_list):

#     modified_selection_sort(number_list, column_sorting_priority_list[1])
#     modified_selection_sort(number_list, column_sorting_priority_list[0])

#It first sorts based on the last criterion in the sorting order (in this case, 'Last Name'), and then within the 
#groups of the same last names, it sorts based on the first criterion (in this case, 'First Name'). The output will 
#be the sorted list of dictionaries as per the specified sorting order.


#///////////////////////////////////////////////////////////////////


#What the '[-1::-1]' does is:
#The notation [-1::-1] is used to reverse a sequence, such as a list, string, or other iterable, in Python. Let's break 
#down what each part of this notation means:

# - The first '-1' represents the starting index. In Python, negative indices count from the end of the sequence. So, -1 
#  represents the last element, -2 represents the second-to-last element, and so on.
# - The second '::' is used to define the step value for slicing. Here, it means that you want to take all elements.
# - The third '-1' represents the stopping index, which is the index before which you want to stop slicing.

#   (E.g. '[0:6:2]' means start from index 0 (inclusive), and end at index 6 (exclusive), by steps of 2)

#When you combine all these parts, [-1::-1] essentially means starting from the last element (index -1), take all 
#elements in reverse order with a step of -1, until you reach the first element.


def multilevel_selection_sort(elements, sort_by_list):
    for sort_by in sort_by_list[-1::-1]:
        for x in range(len(elements)):
            min_index = x
            for y in range(x, len(elements)):
                if elements[y][sort_by] < elements[min_index][sort_by]:
                    min_index = y
            if x != min_index:
                elements[x], elements[min_index] = elements[min_index], elements[x]


if __name__ == '__main__':
    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    print(f'Given unsorted array:', *elements, sep='\n')

    multilevel_selection_sort(elements, ['First Name', 'Last Name'])

    print(f'Array after Multi-Level Sorting:', *elements, sep='\n')