#This computer program is in the Big O Notation of O(1) in Space Complexity

#It is the iterative binary search algorithm (code copy pasted from online)
#(More on binary search in the Data Structures and Algorithms folder later)

#It is hard to see from the code, but in the code, no new variables is created to store the halves
#during the binary search and only works on the original array. Hence Big O Notation for Space
#Complexity is O(1)

def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 7

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")