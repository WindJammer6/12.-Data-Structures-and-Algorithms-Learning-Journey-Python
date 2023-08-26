#We can technically use an Array/Linked List as a Stack Data Structure, though this is not encouraged as
#it is less efficient than using an actual Stack Data Structure.

#The problem with using a List in Python/dynamic Array is that when it grows in size, it will undergo
#Memory Re-allocation (refer to 'Tutorial 4 - Arrays (Data Structure)'), which is Big O Notation of 
#Time Complexity of O(n) which is what an actual Stack Data Structures do not undergo (the 
#technicalities of the code to make this possible is pre-done by others when during implementation 
#of a Stack we import pre-existing special Data Structures (LifoQueue and deque, which we can choose 
#to use as a Stack from other Python Libraries)), and hence does not waste time during the action 
#of 'pushing'/inserting more elements at Memory Re-allocation (additional O(n)) compared to an 
#Array Data Structure


#Here is an attempt to use an Array (Python's List) to a Stack Data Structure to solve the real life
#scenario described in '1. What_is_a_Stack.txt':

#Creating the so called List as a Stack, 'pushing' the website links accessed in order down the Stack, 
#the new last element each time a latest element is inserted (as last index) as the top of the Stack
#Data Structure
stack_list = []

stack_list.append('https://www.cnn.com/')
stack_list.append('https://www.cnn.com/world')
stack_list.append('https://www.cnn.com/India')
stack_list.append('https://www.cnn.com/China')         #The website on China news will be at the top
                                                       #of the Stack since it was appended last, and
                                                       #is at the last index of the 'stack_list'

print(stack_list)

#If you want to only retrieve, but not remove the latest website link accessed, we can 
#retrieve it by index in Python, also known as 'peeking' into a Stack Data Structure
print(stack_list[-1])
print(stack_list)      #As you can see, latest/last element is not removed and is still
                       #in the 'stack_list'

#Now if we want to retrieve and remove the latest website link accessed, we can use 
#'pop(position=-1)' function, which according to Python's documentation, removes and returns 
#an element at a specific index in a list. (by putting an integer at the 'position' 
#parameter) By default, the parameter is -1, removing and returning the last element 
# of the list.

print(stack_list.pop())
print(stack_list)

print(stack_list.pop())
print(stack_list)

print(stack_list.pop())
print(stack_list)

print(stack_list.pop())
print(stack_list)

#Once you remove everything from the list, you have an empty list. If you try to execute 
#'pop()'  again, you will get an error as you cannot 'pop()' from an empty list
print(stack_list.pop())



