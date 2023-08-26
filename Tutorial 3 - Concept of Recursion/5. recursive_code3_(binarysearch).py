#From the Binary Search Algorithm tutorial there are 2 ways to do create the binary search function, 
#recursive and iterative (though usually iterative is better, but you could do recursion for it)

#Here is the recursive implementation of the binary search algorithm to return the position of `target` 
#in subarray nums[left…right]

def binarySearch(nums, left, right, target):
 
    # Base condition (search space is exhausted)
    if left > right:
        return -1
 
    # find the mid-value in the search space and
    # compares it with the target

    #What '//' does?
    #In Python, you use the double slash '//' operator to perform floor division. 
    #This '//' operator divides the first number by the second number and rounds the result down to the 
    #nearest integer (or whole number).
 
    mid = (left + right) // 2
 
    # overflow can happen. Use below
    # mid = left + (right - left) / 2
 
    # Base condition (a target is found)
    if target == nums[mid]:
        return mid
 
    # discard all elements in the right search space,
    # including the middle element
    elif target < nums[mid]:
        return binarySearch(nums, left, mid - 1, target)
 
    # discard all elements in the left search space,
    # including the middle element
    else:
        return binarySearch(nums, mid + 1, right, target)
 
 
if __name__ == '__main__':
 
    nums = [2, 5, 6, 8, 9, 10]
    target = 5
 
    (left, right) = (0, len(nums) - 1)
    index = binarySearch(nums, left, right, target)
 
    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')