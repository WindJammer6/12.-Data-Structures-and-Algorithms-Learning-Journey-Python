#Question 1:
#Design a food ordering system where your python program will run two threads,

#-> Place Order: This thread will be placing an order and inserting that into a queue. This thread 
#   places new order every 0.5 second. (hint: use time.sleep(0.5) function)
#-> Serve Order: This thread will serve the order. All you need to do is pop the order out of the 
#   queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second
#   after place order thread is started.

#Get yourself familiar with the concept of multithreading in python with the link provided in the 
#excercise. (I've explored it in '5.1. What_is_Multithreading.py' and 
#'5.2. implementing_Multithreading.py')

#Pass following list as an argument to place order thread,
#   orders = ['pizza','samosa','pasta','biryani','burger']

#This problem is a producer, consumer problem where 'place_order()' thread is producing orders whereas
#'server_order()' thread is consuming the food orders. Use Queue class implemented in a video tutorial.

import time
import threading

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
    
    def front_element(self):
        return self.buffer[-1]
    
    def __repr__(self):
        return '{}'.format(self.buffer)


#My answer:
def place_order(queue, list_of_orders):
    for order in list_of_orders:
        queue.enqueue(order)
        print(queue)                #To check status of the queue at each for loop iteration
        print("Now placing order:", order)
        time.sleep(0.5)

def serve_order(queue):
    while True:
        #If queue not empty, 'dequeue()' the queue. Else, break out of the while loop and
        #end this function
        if queue.is_empty() is False:
            print("\nNow serving order:", queue.dequeue())
            time.sleep(2)
        else:
            break


if __name__ == '__main__':
    #Formatting when using Multithreading is taken from '5.1. What_is_Multithreading.py' and 
    #'5.2. implementing_Multithreading.py')
    order_queue = Queue()

    orders = ['pizza','samosa','pasta','biryani','burger']

    place_order_thread = threading.Thread(target=place_order, args=(order_queue,orders,))
    serve_order_thread = threading.Thread(target=serve_order, args=(order_queue,))

    place_order_thread.start()
    time.sleep(1)
    serve_order_thread.start()

    place_order_thread.join()
    serve_order_thread.join()

    #To show end of the program
    print('Placing and serving of orders complete!')

    #All works well, my answer looks correct, Solution looks quite similar so won't be uploading 
    #Solution