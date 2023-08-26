#What this function does is that it is implementing Linear Search Algorithm
def linear_search(numbers_list, number_to_find):

    #When you call the 'enumerate' function on a List, it will return you the indexes and their corresponding 
    #element of that List
    for index, element in enumerate(numbers_list):

        #If element we are currently at in the List during the for loop, is the element we are looking for,
        #we will then return that element's index
        if element == number_to_find:
            return index
        
    #After looping through the whole List, if the element we are looking for cannot be found, we will return 
    #'-1' to show False output (number you are looking for is not found in List). 

    #Note that it is common practice to return the integer '-1' when we cannot find the element we are looking
    #for in Search Algorithms
    return -1


if __name__ == '__main__':
    #In Linear Search, the List does not necessarily need to be sorted. But we are using a sorted List in 
    #this case so we can use the same sorted List to compare Linear Search and Binary Search (see 
    #'3. iterative_binary_search_(function).py'). Note that for Binary Search, in order to use it to search 
    #for an element, Binary Search requires that List to be sorted for it to work, otherwise, Binary Search 
    #will fail if the List is unsorted (unlike for Linear Search, which will still be able to work for unsorted
    #List)
    nums_list = [4, 9, 11, 17, 21, 25, 29, 32, 38]
    num_to_find = 32

    index = linear_search(nums_list, num_to_find)
    print(f"Number found at index {index} using Linear Search")