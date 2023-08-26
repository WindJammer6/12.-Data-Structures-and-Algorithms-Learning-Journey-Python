#Here is the inefficiency we will try to solve here with our updated, more efficient Bubble Sort Algorithm 
#('bubble_sort') function:
#2. When this implementation of Bubble Sort Algorithm is given a pre-sorted List such as:

    #[1, 2, 3, 4, 5, 6, 7]

#   The problem arises is that this implementation of Bubble Sort Algorithm will still treat this as an
#   unsorted List, and repeat the process of the iterating Bubble Sort (n-1) times through the sorted List
#   when it can actually just iterate through it once and realise that it is already sorted, and just 
#   return the sorted List, without having to waste time iterating through this pre-sorted List

#   Another case would be that lets say we are given this unsorted List:

    #[6, 1, 2, 3, 4, 5, 7]

#   After one iteration of Bubble Sort, this unsorted List will look like this:

    #[1, 2, 3, 4, 5, 6, 7]

#   which already made this List sorted. However, with this implementation of Bubble Sort Algorithm, it 
#   will still repeat the process of the iterating Bubble Sort the remaining (n-1-1) times through this
#   already sorted List, when it didn't have to and could have just returned the sorted List after the
#   first iteration instead of after (n-1) iteration

#   So is there a way to improve this implementation of Bubble Sort Algorithm such that it is able to 
#   detect an already sorted List, either from the start of the Bubble Sort Algorithm , or in the middle
#   of the (n-1) iterations of Bubble Sort, and return the sorted List earlier without wasting time 
#   having to go through the full (n-1) iterations of Bubble Sort when it dosen't have to?

from time_it import time_it

#This 'inefficient_bubble_sort1' function contains the code of the inefficient 'bubble_sort' function from
#the previous file, '2. bubble_sort_(function)_and_the_inefficiencies_of_this_bubble_sort_implementation.py', 
#which we will be using to compare the runtime with updated, more efficient 'bubble_sort' function below
@time_it
def inefficient_bubble_sort1(number_list):
    size = len(number_list)

    for i in range(size - 1):
        for j in range(size - 1):
            if number_list[j] > number_list[j+1]:
                temp = number_list[j]

                number_list[j] = number_list[j+1]
                number_list[j+1] = temp

#This 'inefficient_bubble_sort2' function contains the code of the slightly more efficient Bubble Sort 
#Algorithm (that solves the inefficiency pointer 1 (see '3. improving_on_bubble_sort_inefficiency_1.py', the 
#previous file)) function from the previous file, '3. improving_on_bubble_sort_inefficiency_1.py', which we 
#will be using to compare the runtime with updated, more efficient 'bubble_sort' function below
@time_it
def inefficient_bubble_sort2(number_list):
    size = len(number_list)

    for i in range(size - 1):
        for j in range(size - 1 - i):
            if number_list[j] > number_list[j+1]:
                temp = number_list[j]

                number_list[j] = number_list[j+1]
                number_list[j+1] = temp

#This is the updated, even more efficient Bubble Sort Algorithm ('bubble_sort' function) that solves inefficiency
#pointer 2 (as described above). This 'bubble_sort' function is built on top of the 'inefficient_bubble_sort2' 
#function, which solves inefficiency pointer 1 (see '3. improving_on_bubble_sort_inefficiency_1.py')
@time_it
def bubble_sort(number_list):
    size = len(number_list)

    for i in range(size - 1):

        #The difference between the 'inefficient_bubble_sort2' and 'bubble_sort' functions is that the 'bubble_sort'
        #function has the additional 'swapped = False' in the outer for loop, and the 'swapped = True' in the inner
        #for loop.

        #What these additional 'swapped = False' in the outer for loop, and the 'swapped = True' in the inner
        #for loop does is that initially, before every iteration of Bubble Sort, the variable 'swapped' is False. 
        swapped = False
        for j in range(size - 1 - i):

            #Then, during the iteration of Bubble Sort through the unsorted List, if there is swap of any of the 2 
            #elements, which means that the condition of the if statement in the inner for loop is met, the code in 
            #the if statemenet will run, and the 'swapped' variable will become True. Else, if there was no swap of 
            #any of the 2 elements during that iteration of Bubble Sort, the 'swapped' variable will remain False
            if number_list[j] > number_list[j+1]:
                temp = number_list[j]

                number_list[j] = number_list[j+1]
                number_list[j+1] = temp
                swapped = True

        #If the 'swapped' variable remain False, which indicates there is no swapping of any of the 2 elements 
        #during that iteration of Bubble Sort, then the 'number_list' must already be sorted, and we can break 
        #out of the outer for loop earlier, ending the Bubble Sort Algorithm, 'bubble_sort' function earlier,
        #allowing us to save time by breaking out of the Bubble Sort Algorithm earlier if we have checked that
        #the 'number_list' is already sorted before the end of (n-1) iterations of Bubble Sort through the
        #'number_list'.
        
        #ELse if the 'swapped' variable is True, which indicates there was swapping of 2 elements (dosen't matter
        #how many swaps were made), which indicates that the 'number_list' is still unsorted. Hence we will need
        #to carry out further iterations of Bubble Sort through the 'number_list' and we will still cannot break
        #out of the Bubble Sort Algorithm yet
        if not swapped:                     #'if swapped == False' works as well
            break


if __name__ == '__main__':
    # nums_list = [38, 9, 29, 7, 2, 15, 28]
    large_sorted_list = [i for i in range(1001)]

    #You will notice the difference in runtimes between the 3 'inefficient_bubble_sort1', 
    #'inefficient_bubble_sort2' and 'bubble_sort' functions, with the 'inefficient_bubble_sort1' function 
    #taking the longest runtime, after 'inefficient_bubble_sort2' and then the 'bubble_sort' function
    #with the shortest runtime
    inefficient_bubble_sort1(large_sorted_list)
    inefficient_bubble_sort2(large_sorted_list)
    bubble_sort(large_sorted_list)

    # print(nums_list)
    print(large_sorted_list)


    #////////////////////////////////////////////
    
    
    #Note that you can also use this Bubble Sort Algorithm to sort strings in a unsorted List too (in alphabetical 
    #order). This is because in Python, you can use the '>' and '<' operator to compare characters and strings too
    #as these operators compare the lexicographical order (aka  "dictionary order", i.e., the way in which words 
    #are ordered in a dictionary) when the inputs are characters/strings instead of numbers. For exammple,

        #For characters,
        #'a' < 'b' will give you the output True
        #'a' > 'b' will give you the output False
        #(this is because the alphabet 'a' is further in front of the alphabetical order than the alphabet 'b')

        #For strings,
        #'abc' < 'abx' will give you the output True
        #'abc' > 'abx' will give you the output False
        #(this is because you will expect to find the string 'abc' is further in front of a dictionary (order)
        #than the string 'abx')

    unsorted_string_list = ['mona', 'dhavel', 'aamir', 'tina', 'chang']

    bubble_sort(unsorted_string_list)
    print(unsorted_string_list)