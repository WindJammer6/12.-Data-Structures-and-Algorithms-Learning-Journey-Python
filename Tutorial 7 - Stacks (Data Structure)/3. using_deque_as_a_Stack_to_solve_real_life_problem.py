#The recommended approach to implement a Stack in Python is by using the 'deque' special Data
#Structure in the 'collections' Python library.

#What does the 'collections' Python library consist of?
#Python programming language has four collection data types - list, tuple, sets and dictionary. But 
#Python also comes with a library known as 'collections' which has specialized Data Structures 
#which basically covers for the shortcomings of the four data types. Here are the specialised Data
#Structures in Python's 'collections' library:

#1. namedtuple() (common)
#2. deque (common)
#3. Chainmap (common)
#4. Counter (common)
#5. OrderedDict (common)
#6. defaultdict (common)
#7. UserDict
#8. UserList
#9. UserString

#But in the recommended and more actual implementation of a Stack Data Structure in Python, we will
#make use of the 'deque' specialised Data Structure in the 'collections' Python library.

#From the Python documentation: 'deque' is in short for 'Double-Ended Queue'. It is a generalisation
#of stacks and queues and are implemented using doubly Linked-Lists. and there is no need to worry 
#about issues such as Memory Re-allocation, or any other inefficiencies from Arrays and Linked Lists
#as the code under this specialised Data Structure will solve them for you so you can maximise 
#efficiency when implmenting Stack Data Structure.

#Visual representation of how it looks like:

# Adding element ----                                   ---- Adding element
#                   |                                   |
#                  \ /                                 \ /
#                 (Rear)                             (Front)
#                 [ 10 ][ 20 ][ 30 ][ 40 ][ 50 ][ 60 ][ 70 ]
#                   |                                   |
#                   |                                   |
# Removing element <-                                   -> Removing element

#In short to use a 'deque' as a Stack, we just have to treat one end as closed, and not 'push'/'pop'
#any elements from one of the sides (e.g. the left side), and the 'deque' specialised Data Structure 
#will now essentially be a Stack Data Structure

from collections import deque

stack = deque()

#Using 'dir()' function to view the list of methods on a 'deque' specialised Data Structure (or you
#could refer to documentation as well)
print(dir(deque))

#Note that you have methods such as 'append()', 'appendleft()', 'pop()' and 'popleft()' in a 'deque'
#specialised Data Structure, but as long as you only use 'append()' and 'pop()', and not use those
#'left' methods, you are essentially treating 'deque()' as a Stack Data Structure

#'pushing'
stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/India')
stack.append('https://www.cnn.com/China')
print(stack)

#'peeking'
print(stack[-1])

#'popping'
print(stack.pop())
print(stack)


