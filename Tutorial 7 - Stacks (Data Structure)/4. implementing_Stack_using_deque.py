#What we are trying to do here is create an actual Stack Data Structure. (meaning its not like we 
#are modifying how we use other Data Structures such as List/Linked List/deque in such that how a
#Stack would behave) This 'Stack' class here is an actual Stack Data Structure instead of another
#Data Structure under the hood (even though we are building it from 'deque' specialised Data 
#Structure but we are modifying it, and so-called 'locking' its behaviour as a Stack, and storing
#these modifications under a 'Stack' class)

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()      #btw, container and data structure are 2 terms that are
                                      #sometimes exchangable in meaning. I think its ok to think
                                      #of a container as a Data Structure in this context

    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    #So I can use the 'print()' function on my 'Stack' class to look at my 'Stack' object
    def __repr__(self):
        return '{}'.format(self.container)
    

if __name__ == '__main__':
    stack = Stack()

    stack.push(5)

    print(stack.peek())

    print(stack.pop())
    print(stack)

    print(stack.is_empty())  #Output should be True if Stack is empty, False if Stack not empty

    stack.push(67)
    stack.push(7)
    stack.push(748)

    print(stack.size())
    print(stack)
