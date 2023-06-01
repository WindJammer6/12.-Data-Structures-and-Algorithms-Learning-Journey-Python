#This computer program is in the Big O Notation of O(logn) in Space Complexity

#It is the recursive binary search algorithm (code copy pasted from online)
#(More on binary search in the Data Structures and Algorithms folder later)

#It is hard to see from the code, but in the code, new variables is created hence more memory is needed 
#to store the halves from the return statements under the 'binarySearch()' function which tells the 
#computer to make more space to store the saved halves in memory and executing the next recursive
#loop on the new sorted half. Hence Big O Notation for Space Complexity is O(logn). (Theres some math
#behind why its logarithmic and not n but thats not very important)

def binarySearch(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")