#Question 1:

#Sort the elements of a given list using Shell Sort, but with a slight modification. Remove all the repeating 
#occurances of elements while sorting.

#Traditionally, when comparing two elements in Shell Sort, we swap if first element is bigger than second, 
#and do nothing otherwise.

#In this modified Shell Sort with duplicate removal, we will swap if first element is bigger than second, 
#and do nothing if element is smaller, but if values are same, we will delete one of the two elements we are 
#comparing before starting the next pass for the reduced gap.

#For example, given the unsorted list [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3], after sorting using Shell Sort 
#without duplicates, the sorted list would be:
    #[0, 1, 2, 3, 5, 7, 8, 9]

def shell_sort(number_list):

    gap = len(number_list)//2

    while gap > 0:


        #~~~(Start of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~
        
        for i in range(gap, len(number_list)):

            anchor = number_list[i]

            j = i - gap

            while j >= 0 and anchor < number_list[j]:
                number_list[j + gap] = number_list[j]
                j -= gap

            number_list[j + gap] = anchor

        #~~~(End of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~


        gap = gap // 2


#My answer:
def modified_shell_sort(number_list):

    gap = len(number_list)//2
    initial_unsorted_list_size = len(number_list)

    while gap > 0:


        #~~~(Start of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~
        
        #Manually creating my 'i' index/pointer since I'm not using a for loop anymore to initiate the 'i' 
        #index/pointer for me
        i = gap

        #I needed to change the for loop to a while loop, while incrementing the 'i' index/pointer manually in order
        #for the code to work. If I use the for loop, during deletion of duplicate elements during the gap iterations, 
        #I might go out of index range of the initial unsorted List due to the 'range()' function in the for loop
        #being fixed and not flexible to exiting the for loop from any changes within the for loop itself. Hence
        #I need a while loop to solve this problem
        #for i in range(gap, len(number_list)):
        while i < initial_unsorted_list_size:

            anchor = number_list[i]

            j = i - gap

            while j >= 0 and anchor < number_list[j]:
                number_list[j + gap] = number_list[j]
                j -= gap

            number_list[j + gap] = anchor
            
            #If element the pointer is at is equal to an 'gap'th element on its left in the initial unsorted List,
            #this means there is a duplicate, and we will hence choose to delete either one of the duplicates. In 
            #this case, we will delete the duplicate element on the left after we shifted the element the pointer 
            #is pointing at to its correct position within the smaller subarray during the Insertion Sort within
            #this modified Shell Sort Algorithm
            #Visulisation:
                # Initial unsorted List before smaller subarray undergo Insertion Sort:
                #     [2][1][5][7][4][0][5][1][2][9][5][8][3]                  gap = 3           (Let 'p' be the pointer)
                #                           ^
                #                          (p)

                # Smaller subarray before Insertion Sort:                        Smaller subarray after Insertion Sort:
                #     [ ][1][ ][ ][4][ ][ ][1][ ][ ][ ][ ][ ]        -->         [ ][1][ ][ ][1][ ][ ][4][ ][ ][ ][ ][ ]
                #                                                             (no change since smaller subarray is already sorted)


                # We will then delete the duplicate element on the left in the smaller subarray after Insertion Sort:
                # Before deletion:
                #     [ ][1][ ][ ][1][ ][ ][4][ ][ ][ ][ ][ ]                  gap = 3
                #                           ^
                #                          (p)

                # After deletion:
                #              (deleted)
                #                 ///
                #     [ ][1][ ][ ]   [ ][ ][4][ ][ ][ ][ ][ ]                  gap = 3
                #                           ^
                #                          (p)
            if anchor == number_list[j]:
                number_list.remove(number_list[j + gap])

                #Manually decreasing the 'initial_unsorted_list_size' so that the program dont go out of index 
                #range of the List and exit the while loop when the program reaches the end of the current initial
                #unsorted List (the size of the initial unsorted List may vary throughout this modified Shell Sort
                #Algorithm due to the on-the-fly deletion of duplicate elements during the this modified Shell Sort
                #Algorithm's gap iterations)
                initial_unsorted_list_size -= 1

                #Notice that we do not increment pointer 'i' in if statement condition since the index is already 
                #sort of 'shifted' to the right automatically when a duplicate element was deleted in the initial
                #unsorted List

                #Lets say the element we want to delete is the element at index 3 ('5'), and pointer 'i' is
                #currently at index 7 ('8')

                #Visualisation:
                #Before deletion:
                #Index: 1  2  3  4  5  6  7  8  9  10 11 12 13          
                #      [2][1][5][7][4][0][8][1][2][9][5][8][3]                  i = 7           (Let 'p' be the pointer)
                #                         ^
                #                        (p)

                #After deletion:
                #Index: 1  2 /// 3  4  5  6  7  8  9  10 11 12          
                #      [2][1]   [7][4][0][8][1][2][9][5][8][3]                  i = 7           (Let 'p' be the pointer)
                #                            ^
                #                           (p)

                #We can see that although the pointer 'i' is still at index 7, it is now sort of pointing to the
                #next element already ('1') after deletion of the element at index 3 ('5') instead of the element ('8')
                #before deletion of the element at index 3 ('5'). Hence we should not incremenet pointer 'i' manually 
                #again in this if statement condition
            

            #Else the element the pointer is pointing at is larger than the 'gap'th element on its left in the initial
            #unsorted List or that the element the pointing at is smaller than all the 'gap'th element on its left
            #in the initial unsorted List and the pointer 'j' in the 'gap-ed' Insertion Sort goes out of the index 
            #range, then we will do nothing to the initial unsorted List, and just increment the pointer 'i' to the
            #next index on its right
            else:
                i += 1

        #~~~(End of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~


        gap = gap // 2


if __name__ == '__main__':
    nums_list = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]

    modified_shell_sort(nums_list)

    print(nums_list)


    #My answer works, couldn't quite understand the Solution which I uploaded in 
    #'6. Excercise1(Solution)_Shell_Sort_(Sorting_Algorithm).py'