#The recommended approach to implement a Queue in Python is by using the 'deque' special Data
#Structure in the 'collections' Python library. (same as implementing Stack Data Structure in 
#Python)

#Stuff like what the 'collections' Python library consist of and about 'deque' special Data 
#Structure already covered in the '3. using_deque_as_a_Stack_to_solve_real_life_problem.py'
#What does the 'collections' Python library consist of?

#Visual representation of how 'deque' (a.k.a Double-Ended Queue) special Data Structure looks like:

# Adding element ----                                   ---- Adding element
#                   |                                   |
#                  \ /                                 \ /
#                 (Rear)                             (Front)
#                 [ 10 ][ 20 ][ 30 ][ 40 ][ 50 ][ 60 ][ 70 ]
#                   |                                   |
#                   |                                   |
# Removing element <-                                   -> Removing element

#To use a 'deque' as a Stack, we just have to treat both ends as open, and only exclusively reserve 
#one end of 'deque' for 'push' and the other end exclusively for 'pop' only, and the 'deque'
#specialised Data Structure will now essentially be a Queue Data Structure

from collections import deque

queue = deque()

#Using 'dir()' function to view the list of methods on a 'deque' specialised Data Structure (or you
#could refer to documentation as well)
print(dir(deque))

#Note that you have methods such as 'append()', 'appendleft()', 'pop()' and 'popleft()' in a 'deque'
#specialised Data Structure, but unlike Stack, where you only use  'append()' and 'pop()', in a Queue,
#you must always only append from the left and 'pop' from the right, so you only use 'appendleft()' 
#and 'pop()'. When you do this, you are essentially treating 'deque()' as a Queue Data Structure

#'pushing'
queue.appendleft(131.10)
queue.appendleft(131.12)
queue.appendleft(135)
print(queue)

#'popping'
print(queue.pop())
print(queue)


