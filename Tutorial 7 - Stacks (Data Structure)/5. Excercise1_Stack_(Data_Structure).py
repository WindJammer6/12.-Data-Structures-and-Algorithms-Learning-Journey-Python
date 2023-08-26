#Question 1:
#Write a function in python that can reverse a string using stack data structure. Use Stack class 
#from the tutorial.

#Example: reverse_string("We will conquer COVID-19") should return "91-DIVOC reuqnoc lliw eW"

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

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
    
    def __repr__(self):
        return '{}'.format(self.container)
    
    #My answer:
    def reverse_string(self):
        if self.is_empty() is True:
            print("This Stack is empty!")
        else:
            for i in range(self.size()):
                print(self.pop(), end="")

    #Solution: (taking out the string (starting from character at the top of the Stack) from the 
    #Stack Data Structure and storing them, in an another string, 'popping' characterby character
    #until the Stack is empty)

    # def reverse_string(string):
    #     stack = Stack()

    #     for character in string:
    #         stack.push(character)

    #     reverse_str = ''
    #     while stack.size() != 0:
    #         reverse_str += stack.pop()

    #     return reverse_str
        
    
if __name__ in '__main__':
    stack = Stack()
    
    string = "We will conquer COVID-19"
    for i in string:
        stack.push(i)
    print(stack)
    stack.reverse_string()
    print("\n")

    #Testing case if 'Stack' object is empty
    print(stack.is_empty())
    print(stack)
    stack.reverse_string()

    #All works well, my answer looks correct.

