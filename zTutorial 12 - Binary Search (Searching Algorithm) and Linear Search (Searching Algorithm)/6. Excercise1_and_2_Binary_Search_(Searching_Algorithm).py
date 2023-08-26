#Question 1:

#When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is 
#that?
    
    #numbers = [1,4,6,9,10,5,7]

#My answer: This is because Binary Search Algorithm only works on sorted Lists. The List that Binary Search 
#Algorithm works on needs to be sorted first for it to work, otherwise, it will not produce the desired output. 
#Here, the provided List, 'numbers', is not sorted.

#(My answer is correct after checking with the provided solution)


#Question 2:

#Find index of all the occurances of a number from sorted list.

    #numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    #number_to_find = 15  

#This should return 5,6,7 as indices containing number 15 in the array.

def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
        
    return -1

def iterative_binary_search(numbers_list, number_to_find):

    left_index = 0
    right_index = len(numbers_list) - 1
    middle_index = 0

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_number = numbers_list[middle_index]

        if middle_number == number_to_find:
            return middle_index
        
        if middle_number < number_to_find:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

    return -1

def recursive_binary_search(numbers_list, number_to_find, left_index, right_index):

    if right_index < left_index:
        return -1
    
    middle_index = (left_index + right_index) // 2
    if middle_index >= len(numbers_list) or middle_index < 0:
        return -1
    middle_number = numbers_list[middle_index]

    if middle_number == number_to_find:
        return middle_index
    
    if middle_number < number_to_find:
        left_index = middle_index + 1
    else:
        right_index = middle_index - 1

    return recursive_binary_search(numbers_list, number_to_find, left_index, right_index)

#My answer:
#Basically, I copied the code from the 'iterative_binary_search' function and modifying it
def find_all_occurances_of_a_number_from_sorted_list(numbers_list, number_to_find):

    indexes_storing_number_to_find = []

    left_index = 0
    right_index = len(numbers_list) - 1
    middle_index = 0

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_number = numbers_list[middle_index]

        if middle_number == number_to_find:
            found_number_index = middle_index

            while found_number_index > -1:
                if numbers_list[found_number_index - 1] == number_to_find:
                    indexes_storing_number_to_find.append(found_number_index - 1)
                    found_number_index -= 1
                else:
                    break
            
            indexes_storing_number_to_find.append(middle_index)

            found_number_index = middle_index
            while found_number_index < len(numbers_list):
                if numbers_list[found_number_index + 1] == number_to_find:
                    indexes_storing_number_to_find.append(found_number_index + 1)
                    found_number_index += 1
                else:
                    break

            return indexes_storing_number_to_find
        
        if middle_number < number_to_find:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

    return indexes_storing_number_to_find


#Solution:
def find_all_occurances(numbers, number_to_find):
    index = iterative_binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index - 1
    while i >= 0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

#Both my answer annd solution works the same, but the way of implementing by the solution is
#much cleaner than mine since it leverages on using the 'iterative_binary_search' function by 
#directly while I naively copy-pasted the full code again. 

#After comparing my answer and solution, the idea is the same, that once the number to be 
#searched for is found, due to the fact that we definitely know that the List we are using 
#Binary Search Algorithm on must be sorted, if the number we are looking for has any duplicates, 
#it must definitely all be side by side in terms of index with each other in the sorted List.

#So this 'find_all_occurances_of_a_number_from_sorted_list' function will search the left and 
#right side of the index where the number is found for duplicates and appending them to a 'found'
#List and returning that at the end of the function (both have the same idea just that my function's
#code answer looks a bit more messy and unreadable compared to the solution's function's code)


if __name__ == '__main__':
    nums_list = [1,4,4,4,46,9,11,15,15,15,17,21,34,34,56]
    num_to_find = 15
    num_to_find2 = 34
    num_to_find3 = 4

    index = find_all_occurances_of_a_number_from_sorted_list(nums_list, num_to_find)
    print(f"Number {num_to_find} found using modified iterative Binary Search at indexes {index}")

    index2 = find_all_occurances_of_a_number_from_sorted_list(nums_list, num_to_find2)
    print(f"Number {num_to_find2} found using modified iterative Binary Search at indexes {index2}")

    index3 = find_all_occurances_of_a_number_from_sorted_list(nums_list, num_to_find3)
    print(f"Number {num_to_find3} found using modified iterative Binary Search at indexes {index3}")



    
