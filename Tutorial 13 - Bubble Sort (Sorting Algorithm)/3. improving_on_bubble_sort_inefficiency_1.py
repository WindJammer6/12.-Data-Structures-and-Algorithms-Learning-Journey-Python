#Here is the inefficiency we will try to solve here with our updated, more efficient Bubble Sort Algorithm 
#('bubble_sort') function:
#1. Lets say you have already iterated with Bubble Sort through the unsorted 'number_list' twice already,
#   and you now have this semi-sorted 'number_list':

    #[28, 7, 2, 15, 9, 29, 38]
    #                  ///////

#   Now you technically only need to just run the next (third) iteration of Bubble Sort up to the third
#   last element ('9') because you the last 2 elements are already guranteed to be sorted by the previous
#   2 iterations of Bubble Sort. 
# 
#   (To explain further, for the fourth iteration of Bubble Sort you only need to run it up to the fourth
#    last element as the last 3 elements are already guranteed to be sorted by the previous 3 iterations 
#    of Bubble Sort and so on...)

#   Currently what this implementation of Bubble Sort Algorithm is doing is that in every iteration of
#   Bubble Sort, it is traversing and comparing the 2 elements up until the last element, which is
#   redundant, since for example at the third iteration, the last 2 elements are already guranteed to be
#   sorted, and it will be a waste of time if the program try to compare and swap them again. 
# 
#   Hence it will save time if the program could reduce the sorting area after every iteration by ignoring 
#   the 'sorted' elements (the number of 'sorted' elements at the end of the unsorted 'number_list' depend
#   on which iteration of Bubble Sort the program is at) at the end of the unsorted 'number_list' during
#   that iteration of Bubble Sort

#Importing the 'wrapped function' 'time_it' from 'time_it.py' (you can find this file in this tutorial's directory),
#so that we can add a Decorator (with the 'wrapped function''s name as the Decorator/'tag' ('@time_it')) to the 
#'inefficient_bubble_sort' and 'bubble_sort' functions to add/modify the functionalities of these functions to be 
#able to measure/track their own respective runtimes 
from time_it import time_it

#This 'inefficient_bubble_sort' function contains the code of the inefficient 'bubble_sort' function from
#the previous file, '2. bubble_sort_(function)_and_the_inefficiencies_of_this_bubble_sort_implementation.py', 
#which we will be using to compare the runtime with updated, more efficient 'bubble_sort' function below
@time_it
def inefficient_bubble_sort(number_list):
    size = len(number_list)

    for i in range(size - 1):
        for j in range(size - 1):
            if number_list[j] > number_list[j+1]:
                temp = number_list[j]

                number_list[j] = number_list[j+1]
                number_list[j+1] = temp

#This is the updated, more efficient Bubble Sort Algorithm ('bubble_sort' function) that solves inefficiency 
#pointer 1 (as described above)
@time_it
def bubble_sort(number_list):
    size = len(number_list)

    for i in range(size - 1):

        #The only difference between the 'inefficient_bubble_sort' and 'bubble_sort' functions is that the 
        #'bubble_sort' function has the additional '-i' in the inner for loop.

        #What this additional '-i' does is that using this unsorted List, for example,

            #[38, 9, 29, 7, 2, 15, 28]
             
        #If we are in the second iteration of Bubble Sort, in which the semi-sorted unsorted List will look 
        #like this,

            #  0  1  2   3  4   5   6 
            #[28, 7, 2, 15, 9, 29, 38]
            #                     ////

        #'i' will be 1, and hence (size - 1 - i) = 5 (in this example, size (of our unsorted 'number_list') = 7),
        #and the inner for loop will only loop until index 4, up to comparing elements at index 4 and index 5, 
        #ignoring the element at index 6, which it can, in order to save time, since this last element (element 
        #at index 6) is already guranteed to be sorted by the first iteration and so on for the other 
        #iterations... 
         
        #(e.g. 'i' will be 2 for the third iteration, and you just apply the same logic here until the (n-1) 
        # iteration, where n represents the size of the unsorted 'number_list' which in this case n = 7)
        for j in range(size - 1 - i):
            if number_list[j] > number_list[j+1]:
                temp = number_list[j]

                number_list[j] = number_list[j+1]
                number_list[j+1] = temp


if __name__ == '__main__':
    #This number List ('nums_list') is too small, if you try to measure the runtimes between the 
    #'inefficient_bubble_sort' and 'bubble_sort' functions, you will realise that you don't see a noticeable 
    #difference in runtime, and will both have a runtime almost close to 0.0 milliseconds. In order to really see 
    #the difference in effectiveness between the 'inefficient_bubble_sort' and 'bubble_sort' functions in terms of 
    #Time Complexity, we will need to use a larger number List ('large_sorted_list')

    # nums_list = [38, 9, 29, 7, 2, 15, 28]
    large_sorted_list = [i for i in range(1001)]

    #You will notice the difference in runtimes between the 2 'inefficient_bubble_sort' and 'bubble_sort' functions,
    #with the 'inefficient_bubble_sort' function taking a longer runtime than the 'bubble_sort' function
    inefficient_bubble_sort(large_sorted_list)
    bubble_sort(large_sorted_list)

    # print(nums_list)
    print(large_sorted_list)