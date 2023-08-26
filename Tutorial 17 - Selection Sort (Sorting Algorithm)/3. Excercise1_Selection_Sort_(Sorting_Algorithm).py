# Question 1:

# Implement a Multi-Level Sort of a given list of dictionaries based on a given sorting order. If user wants to sort 
# dictionary based on First Key 'A', then Key 'B', they shall pass list of keys in the order of preference as a list 
# ['A','B']. Your code should be able to sort list of dictionaries for any number of keys in sorting order list.

# Using this multi-level sort, you should be able to sort any list of dictionaries based on sorting order preference.

# E.g. A single dictionary entry contains two keys 'First Name' and 'Last Name'. the list should be sorted first 
# based on 'First Name', then based on 'Last Name', w.r.t. common/same 'First Name' entries. For this, one shall past 
# sorting order of preference list ['First Name', 'Last Name'].

# For this, Given the following unsorted sequence List:
    # [
    #     {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    #     {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    #     {'First Name': 'Karan', 'Last Name': 'Kumar'},
    #     {'First Name': 'Jade', 'Last Name': 'Canary'},
    #     {'First Name': 'Raj', 'Last Name': 'Thakur'},
    #     {'First Name': 'Raj', 'Last Name': 'Sharma'},
    #     {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    #     {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    #     {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    #     {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    #     {'First Name': 'Jaya', 'Last Name': 'Seth'},
    #     {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    #     {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    #     {'First Name': 'Aahana', 'Last Name': 'Arora'}
    # ]

# Your algorithm should generate the following sorted list:
    # [
    #     {'First Name': 'Aahana', 'Last Name': 'Arora'}
    #     {'First Name': 'Armaan', 'Last Name': 'Dadra'}
    #     {'First Name': 'Armaan', 'Last Name': 'Kumar'}
    #     {'First Name': 'Ingrid', 'Last Name': 'Galore'}
    #     {'First Name': 'Ingrid', 'Last Name': 'Maverick'}
    #     {'First Name': 'Jade', 'Last Name': 'Canary'}
    #     {'First Name': 'Jaya', 'Last Name': 'Seth'}
    #     {'First Name': 'Jaya', 'Last Name': 'Sharma'}
    #     {'First Name': 'Karan', 'Last Name': 'Kumar'}
    #     {'First Name': 'Kiran', 'Last Name': 'Kamla'}
    #     {'First Name': 'Raj', 'Last Name': 'Nayyar'}
    #     {'First Name': 'Raj', 'Last Name': 'Sharma'}
    #     {'First Name': 'Raj', 'Last Name': 'Thakur'}
    #     {'First Name': 'Suraj', 'Last Name': 'Sharma'}
    # ]

def selection_sort(number_list):
    for i in range(len(number_list) - 1):
        minimum_element_index = i

        for j in range(i + 1, len(number_list)):
            if number_list[j] < number_list[minimum_element_index]:
                minimum_element_index = j

        if number_list[i] != number_list[minimum_element_index]:
            number_list[i], number_list[minimum_element_index] = number_list[minimum_element_index], number_list[i]


#My answer:
def modified_selection_sort(list, index_list, column):
    for i in range(len(index_list)):
        minimum_element_index = i

        for j in range(i + 1, len(index_list)):
            if list[index_list[j]][column] < list[index_list[minimum_element_index]][column]:
                minimum_element_index = j

        if list[index_list[i]][column] != list[index_list[minimum_element_index]][column]:
            list[index_list[i]], list[index_list[minimum_element_index]] = list[index_list[minimum_element_index]], list[index_list[i]]


def algorithm(list, column_sorting_priority_list):
    #For first column that is of the first priority in the 'column_sorting_priority_list',
    for i in range(len(list) - 1):
        minimum_element_index = i

        for j in range(i + 1, len(list)):
            if list[j][column_sorting_priority_list[0]] < list[minimum_element_index][column_sorting_priority_list[0]]:
                minimum_element_index = j

        if list[i][column_sorting_priority_list[0]] != list[minimum_element_index][column_sorting_priority_list[0]]:
            list[i], list[minimum_element_index] = list[minimum_element_index], list[i]


    #For remaining columns,
    for c in column_sorting_priority_list[1:]:
        
        list_common_previous_column_input = []

        for k in list:
            
            list_common_previous_column_input.append(list.index(k))

            if len(list_common_previous_column_input) > 1:

                if k[column_sorting_priority_list[column_sorting_priority_list.index(c) - 1]] != list[list_common_previous_column_input[-2]][column_sorting_priority_list[column_sorting_priority_list.index(c) - 1]]:
                    modified_selection_sort(list, list_common_previous_column_input[:len(list_common_previous_column_input)-1], c)
                    list_common_previous_column_input = [list.index(k)]
        

if __name__ == '__main__':
    name_list = [
        {'First Name': 'Kiran', 'Last Name': 'Kamla', 'Age': 20},
        {'First Name': 'Raj', 'Last Name': 'Nayyar', 'Age': 28},
        {'First Name': 'Suraj', 'Last Name': 'Sharma', 'Age': 31},
        {'First Name': 'Karan', 'Last Name': 'Kumar', 'Age': 27},
        {'First Name': 'Jade', 'Last Name': 'Canary', 'Age': 22},
        {'First Name': 'Armaan', 'Last Name': 'Dadra', 'Age': 39},
        {'First Name': 'Raj', 'Last Name': 'Thakur', 'Age': 30},
        {'First Name': 'Raj', 'Last Name': 'Sharma', 'Age': 28},
        {'First Name': 'Kiran', 'Last Name': 'Kamla', 'Age': 24},
        {'First Name': 'Armaan', 'Last Name': 'Kumar', 'Age': 28},
        {'First Name': 'Jaya', 'Last Name': 'Sharma', 'Age': 29},
        {'First Name': 'Ingrid', 'Last Name': 'Galore', 'Age': 35},
        {'First Name': 'Jaya', 'Last Name': 'Seth', 'Age': 31},
        {'First Name': 'Armaan', 'Last Name': 'Dadra', 'Age': 30},
        {'First Name': 'Kiran', 'Last Name': 'Kamla', 'Age': 34},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick', 'Age': 29},
        {'First Name': 'Aahana', 'Last Name': 'Arora', 'Age': 25}
    ]

    algorithm(name_list, ["First Name", "Last Name", "Age"])

    for i in name_list:
        print(i)