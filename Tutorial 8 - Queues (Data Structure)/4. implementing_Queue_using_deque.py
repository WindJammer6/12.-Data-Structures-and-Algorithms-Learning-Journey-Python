#What we are trying to do here is create an actual Queue Data Structure. (meaning its not like we 
#are modifying how we use other Data Structures such as List/Linked List/deque in such that how a
#Queue would behave) This 'Queue' class here is an actual Queue Data Structure instead of another
#Data Structure under the hood (even though we are building it from 'deque' specialised Data 
#Structure but we are modifying it, and so-called 'locking' its behaviour as a Queue, and storing
#these modifications under a 'Queue' class)

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()         #Difference between Queue and Stack: in Stack, I used the 
                                      #name '.container' instead to show 'Data Structure', but here
                                      #the name 'buffer' is used instead to show 'Memory Buffer' 
                                      #from the real life scenario described using Queue Data 
                                      #Structure in '1. What_is_a_Queue.txt', but you could use
                                      #'container' if you want

    #Difference between Queue and Stack: in Queue this is equivalent to Stack's 
    #'def push(self, value)', note here is 'appendleft()', not 'append()'!
    def enqueue(self,value):
        self.buffer.appendleft(value)

    #Difference between Queue and Stack: in Queue this is equivalent to Stack's 
    #'def pop(self, value)'
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    #So I can use the 'print()' function on my 'Queue' class to look at my 'Queue' object
    def __repr__(self):
        return '{}'.format(self.buffer)
    

if __name__ == '__main__':
    queue = Queue()

    #You can think of the team pushing stock prices data into the Memory Buffer at NYSE using
    #'enqueue()'
    queue.enqueue({    
        'company':'Walmart',
        'timestamp': '15 apr, 11.01am',
        'price': 131.10
    })

    #You can think of the team consuming stock prices data from the Memory Buffer at Yahoo Finance
    #using 'dequeue()'
    print(queue.dequeue())
    print(queue)

    print(queue.is_empty())  #Output should be True if Queue is empty, False if Queue not empty

    queue.enqueue({    
        'company':'Walmart',
        'timestamp': '15 apr, 11.01am',
        'price': 131.10
    })
    queue.enqueue({    
        'company':'Walmart',
        'timestamp': '15 apr, 11.02am',
        'price': 131.12
    })
    queue.enqueue({    
        'company':'Walmart',
        'timestamp':'15 apr, 11.03am',
        'price': 135
    })
    print(queue.dequeue())
    print(queue.size())
    print(queue)
