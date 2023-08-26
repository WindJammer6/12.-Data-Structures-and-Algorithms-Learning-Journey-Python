#Similar to Stack Data Structure (explained in the Stack Data Structure tutorial), we can technically
#use an Array/Linked List as a Queue Data Structure, though this is not encouraged as it is less 
#efficient than using an actual Queue Data Structure.

#Reason is the same (wasting of time at Memory Re-allocation for dynamic Arrays) as Stack Data Structure,
#which is what an actual Queue Data Structures do not undergo (the technicalities of the code to make 
#this possible is pre-done by others when during implementation of a Queue we import pre-existing special
#Data Structures (LifoQueue and deque, which we can choose to use as a Queue from other Python Libraries)), 
#and hence does not waste time during the action of 'pushing'/inserting more elements at Memory 
#Re-allocation (additional O(n)) compared to an Array Data Structure

#Here is an attempt to use an Array (Python's List) to a Queue Data Structure to solve the real life
#scenario described in '1. What_is_a_Queue.txt':

#Creating the so called List as a Queue, 'pushing' the stock prices data according to earliest time into the 
#Queue, the first element earliest inserted now at the last index, as the first element (last index) at the 
#other end of the Queue Data Structure
queue_list = []

#Whenever an element is inserted at 0th position (first index), the remaining elements gets 'pushed'
#forward, such that the element that was 'pushed' first now becomes the element at the last index,
#a.k.a the first element at the other side of the Queue from where it was inserted from.
queue_list.insert(0, 131.10)
queue_list.insert(0, 131.12)
queue_list.insert(0, 135)

print(queue_list)

#'peeking'. If this was a Stack, you would have gotten the last element added (cuz LIFO), '135', but
#this is a Queue, so you would have gotten the first element added (cuz FIFO), '131.10'
print(queue_list[-1])

#Here is what you get when you 'pop()' an element from the Queue Data Structure (FIFO), unlike Stack,
#which is (LIFO). If this Data Structure were a Stack, you would expect 'pop()' to give you '135',
#(Last element added), but this is a Queue, so you should expect 'pop()' to give you '131.10' instead
#(First element added)
print(queue_list.pop())
print(queue_list)

print(queue_list.pop())
print(queue_list)

print(queue_list.pop())
print(queue_list)

print(queue_list.pop())
print(queue_list)

#Once you remove everything from the list, you have an empty list. If you try to execute 
#'pop()'  again, you will get an error as you cannot 'pop()' from an empty list
print(queue_list.pop())

