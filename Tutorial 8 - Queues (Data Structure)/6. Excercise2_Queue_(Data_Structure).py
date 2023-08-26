#Question 2: 
#Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in
#main tutorial. Binary sequence should look like:
#    1
#    10
#    11
#    100
#    101
#    110
#    111
#    1000
#    1001
#    1010

#Hint: Notice a pattern above. After 1, second and third number is 1+0 and 1+1. 4th and 5th number 
#      are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

#You also need to add front() function in queue class that can return the front element in the 
#queue.

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def __repr__(self):
        return '{}'.format(self.buffer)
    
    #My answer:    
    def front_element(self):
        return self.buffer[-1]
    
    def last_element(self):
        return self.buffer[0]
    
    def second_last_element(self):
        return self.buffer[1]
    
    def binary_pattern(self, number_of_iterations):
        temp_queue = Queue()

        temp_queue.enqueue('1')

        for i in range(number_of_iterations):
            temp_queue.enqueue(temp_queue.front_element() + '0')
            temp_queue.enqueue(temp_queue.front_element() + '1')

            second_last_of_temp_queue = temp_queue.second_last_element()
            last_of_temp_queue = temp_queue.last_element()

            self.enqueue(second_last_of_temp_queue)
            self.enqueue(last_of_temp_queue)

            temp_queue.dequeue()

        return self.buffer
    
    
#Solution:
def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front_element = numbers_queue.front_element()
        print("   ", front_element)
        numbers_queue.enqueue(front_element + "0")
        numbers_queue.enqueue(front_element + "1")

        numbers_queue.dequeue()


if __name__ == '__main__':
    #Testing my functions
    queue = Queue()

    queue.enqueue('1')
    
    print(queue.binary_pattern(5))

    #Testing solution function:
    produce_binary_numbers(10)

    #All works well, my answer looks correct, but Solution looks more concise, but however do
    #not store the binary numbers in memory as it prints, the front element, then 'dequeue()'
    #that front element after it is used to produce the next 2 elements to 'enqueue()'

    #My answer stores all the binary number produced so far in the 'queue' Queue object as 
    #front elements 'dequeue()'-ed are from a temporary Queue object created within the 
    #'binary_pattern()' function
    