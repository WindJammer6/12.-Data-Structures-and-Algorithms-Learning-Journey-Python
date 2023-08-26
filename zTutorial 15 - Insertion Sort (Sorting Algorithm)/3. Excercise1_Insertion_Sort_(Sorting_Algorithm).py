#Question 1:
#Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of 
#the list so far on each new element.

#Recall that the median of an even-numbered list is the average of the two middle numbers in a sorted list.

#For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
    # 2
    # 1.5
    # 2
    # 3.5
    # 2
    # 2
    # 2

def insertion_sort(number_list):

    for i in range(1, len(number_list)):

        anchor = number_list[i]

        j = i - 1
 
        while j >= 0 and anchor < number_list[j]:
            number_list[j + 1] = number_list[j]
            j = j - 1

        number_list[j + 1] = anchor


#My answer (I modified the Insertion Sort Algorithm ('insertion_sort' function) to create the algorithm to answer 
#this qn):
def modified_insertion_sort(number_list):

    #Had to hardcode this in since the for loop only starts from the second element onwards. In
    #order to print the median for the first median of the sorted subarray, with only the first
    #element in the unsorted List in it, and since the first median of the sorted subarray only
    #have one element, the first element, the first median of the sorted subarray has to be this
    #first element anyway. Hence I hardcoded this in to get the desired output (see question above)
    print(number_list[0])
    
    for i in range(1, len(number_list)):

        anchor = number_list[i]

        j = i - 1

        while j >= 0 and anchor < number_list[j]:
            number_list[j + 1] = number_list[j]
            j = j - 1
        
        number_list[j + 1] = anchor
        
        
        #To deal with cases if during this for loop iteration we have an even number index, which means there is an 
        #odd number of elements in the sorted subarray
        if i % 2 == 0:
            #Using the double slash rounds down the float to get an integer whole number to find the middle element
            #in the sorted subarray so far in this for loop iteration
            print(number_list[i//2])

        #To deal with cases if during this for loop iteration we have an odd number index, which means there is an 
        #even number of elements in the sorted subarray
        else:
            #Using the single slash gives float decimal numbers to find the average of the two middle numbers in the
            #sorted subarray so far in the for loop iteration
            median_number = (number_list[i//2] + number_list[i//2 + 1])/2
 

            #This works since the modulo operator (%) is used to check if the remainder when dividing the 
            #float by 1 is 0. If the float has a decimal place other than '.0' (e.g. '.5'), then the modulo operator 
            #(%) of that float will not be 0. Else, if the float has a decimal place of '.0', then the modulo operator
            #(%) of that float will be 0

            #If the 'median_number' float has a '.0' as its decimal place, then print it as an integer 
            #instead of as a float
            if median_number % 1 == 0:
                print(int(median_number))
            #Else, the 'median_number' float has a decimal place of any other number (e.g. '.5') other 
            #than '.0', then keep it as a float and print it
            else:
                print(median_number)


if __name__ == '__main__':
    nums_list = [2, 1, 5, 7, 2, 0, 5]

    modified_insertion_sort(nums_list)


    #All works well, my answer looks correct, Solution code is not working for some reason so won't be uploading Solution