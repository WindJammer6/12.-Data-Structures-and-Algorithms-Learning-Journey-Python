#What this function does is that it implements Bubble Sort Algorithm
def bubble_sort(number_list):

    #We will be using the size of the unsorted 'number_list' very often in the Bubble Sort Algorithm ('bubble_sort' 
    #function), so to make the code clean, lets store that in a variable 'size'
    size = len(number_list)

    #What this outer for loop does is that determines the number of times/iterations we will be traversing (fully)
    #through the unsorted 'number_list'. So how many times/iterations minimumly do we need to do in order to fully 
    #sort the unsorted 'number_list'?

    #Lets figure it out step by step. If we only do one iteration of Bubble Sort through this unsorted
    #'number_list', '[38, 28, 29, 7, 2, 15, 9]', this would be the semi-sorted 'number_list' we will get back

        #[28, 29, 7, 2, 15, 9, 38]
    
    #Notice that in the List only has the last element ('38') in the right position/guranteed to be 'sorted'
    #while all other elements remain unsorted

    #Lets do a second iteration of Bubble Sort through this unsorted (but now semi-sorted) 'number_list',
    #this would be the semi-sorted 'number_list' we will get back,

        #[28, 7, 2, 15, 9, 29, 38]

    #Notice that now in the List has 2 elements, the last element ('38') and second last element ('29') in the 
    #right position/guranteed to be 'sorted' while all other elements remain unsorted 

    #Hence from this pattern, since 2 iterations of Bubble Sort allows 2 elements (the last 2) to become guranteed
    #'sorted', you might think that it should minimumly require n iterations to fully get all the elements to
    #become 'sorted' in a 'number_list' of size n (n representing the size of the unsorted 'number_list'). But
    #since at the very last iteration, when there is only one last element left 'unsorted', it will 
    #automatically be guranteed to fall in the right place to become 'sorted'. So we can omit running the last
    #iteration of Bubble Sort, meaning it will minimumly take us (n-1) iterations of Bubble Sort in order to get
    #the unsorted 'number_list' fully sorted instead of n
    for i in range(size - 1):

        #What this inner for loop does is that it creates the comparing and swapping of every 2 elements in the 
        #iteration process through the unsorted 'number_list' 

        #The reason we use 'size - 1' instead of the actual length/size of the unsorted 'number_list', 'size' is
        #because, for example:
            
            #[38, 28, 29, 7, 2, 15, 9]
            
        #In this unsorted List, we only want to traverse until the second last element ('15') as during the 
        #swapping process's code, we are comparing the indexes 'number_list[j]' and 'number_list[j+1]' as 
        #the 2 elements. So we don't want to traverse the unsorted 'number_list' all the way till the 
        #actual length/size of the unsorted 'number_list', 'size', as if 'j' is equal the last element ('9')
        #then we will accidentally go out of range of the unsorted 'number_list'when we call 'number_list[j+1]'
        #since after the last element ('9') there are no more elements
        for j in range(size - 1):

            #This if statement does the comparing of every 2 elements. If the left element of the 2 elements is 
            #greater than the right element, then we will run the code within the if statement (which will swap
            #the positions of the 2 elements).
            if number_list[j] > number_list[j+1]:

                #This is the extra temporary variable used when swapping the 2 elements, storing the left element
                #of the 2 elements (you'll see how this extra temporary variable is used in the next 2 lines of 
                #code during the swapping of the 2 elements)
                temp = number_list[j]

                #These codes does the swapping of the 2 elements by first letting the left element of the 2
                #elements also hold the same value as the right element, then letting the right element hold
                #the value of the left element using the 'temp' extra temporary variable storing the left
                #element's value
                number_list[j] = number_list[j+1]
                number_list[j+1] = temp


if __name__ == '__main__':
    nums_list = [38, 28, 29, 7, 2, 15, 9]

    bubble_sort(nums_list)

    print(nums_list)


    #The 2 inefficiencies of this implementation of Bubble Sort Algorithm:

    #(Note that even if you solve these 2 inefficiencies, the Big O Notation of Time Complexity for Bubble
    # Sort Algorithm is still going to be O(n^2), but solving these 2 inefficiencies may help you cut time
    # wasted which is especially crucial when you trying to run the Bubble Sort Algorithm to sort much 
    # larger data Lists)
    
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

    #   We will be tackling this inefficiency in '3. improving_on_bubble_sort_inefficiency_1.py'


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

    #   We will be tackling this inefficiency in '4. improving_on_bubble_sort_inefficiency_2.py'