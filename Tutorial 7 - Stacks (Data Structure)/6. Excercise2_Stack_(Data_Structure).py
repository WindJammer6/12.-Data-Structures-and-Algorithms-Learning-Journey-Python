#Question 2:
#Write a function in python that checks if paranthesis in the string are balanced or not. 
#Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.

#Examples: is_balanced("({a+b})")              --> True
#          is_balanced("))((a+b}{")            --> False
#          is_balanced("((a+b))")              --> True
#          is_balanced("))")                   --> False
#          is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

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
    def is_balanced(self):
        if self.is_empty() is True:
            print("This Stack is empty!")
        else:
            parenthesis_dict = {'[' : 0,
                                ']' : 0,
                                '(' : 0,
                                ')' : 0,
                                '{' : 0,
                                '}' : 0}

            for i in self.container:
                if i in parenthesis_dict.keys():
                    parenthesis_dict[i] += 1
            
            #To check status of the 'parenthesis.dict' dictionary
            print(parenthesis_dict)

            if parenthesis_dict['['] == parenthesis_dict[']'] and parenthesis_dict['('] == parenthesis_dict[')'] and parenthesis_dict['{'] == parenthesis_dict['}']:
                print(True)
            else:
                print(False)


#Solution:
def is_match(char1, char2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[char1] == char2

#Solutions is quite smart in terms of how it used a Stack Data Structure to solve this. 
 
#If the code comes across '(', '[' or '{', it will 'push' it into the 'Stack'. 

#If the code comes across ')', ']' or '}', it will check if the 'Stack' is empty. If it is,
#means the closed parenthesis came before the open parenthesis, and hence will return False
#and exit the for loop. If there is something in the 'Stack', it checks if there is any
#matching available open parenthesis (that has not already been matched yet and has a key
#for the incoming closed parenthesis to match to) defined by the above 'is_match()' function.
#If no matches, the function returns False and exits the for loop

#If all is well so far, the loop resets to find the next '(', '[' or '{' or ')', ']' or '}'
def is_balanced_answer(string):
    stack = Stack()
    for char in string:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        if char == ')' or char == '}' or char == ']':
            if stack.size() == 0:
                return False
            if not is_match(char,stack.pop()):
                return False

    return True          



if __name__ == '__main__':
    #Testing my function
    stack = Stack()
    stack2 = Stack()
    stack3 = Stack()
    stack4 = Stack()
    stack5 = Stack()
                                        #Desired output:
    string = "({a+b})"                  #True      
    string2 = "))((a+b}{"               #False
    string3 = "((a+b))"                 #True
    string4 = "))"                      #False
    string5 = "[a+b]*(x+2y)*{gg+kk}"    #True

    for i in string:
        stack.push(i)

    for i in string2:
        stack2.push(i)

    for i in string3:
        stack3.push(i)

    for i in string4:
        stack4.push(i)

    for i in string5:
        stack5.push(i)
                                        #My output:
    stack.is_balanced()                 #True
    stack2.is_balanced()                #True
    stack3.is_balanced()                #True
    stack4.is_balanced()                #False
    stack5.is_balanced()                #True

#My answer for the second string is not correct, hence my approach to the function is wrong. Reason
#is because I only considered the number of each parenthesis' side (e.g. number of open or closed
#parenthesis respectively and see if they are equal, giving True is equal and False otherwise).

#I forgot to consider if the brackets do not close each other such as ')('. Even if number of 
#parenthesis side is the same, but they do not close each other hence should be False instead of
#True. Also, I didn't even make use of properties of a Stack Data Structure and treated it as it was
#an Array

    #Testing solution answer:                            #Solution output:
    print(is_balanced_answer("({a+b})"))                 #True
    print(is_balanced_answer("))((a+b}{"))               #False
    print(is_balanced_answer("((a+b))"))                 #True
    print(is_balanced_answer("))"))                      #False
    print(is_balanced_answer("[a+b]*(x+2y)*{gg+kk}"))    #True