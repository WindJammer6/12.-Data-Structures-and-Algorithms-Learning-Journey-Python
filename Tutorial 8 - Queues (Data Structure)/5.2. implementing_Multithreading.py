#Python Multithreading scenario:
#For a given list of numbers, calculate and print the square and cube of every number in the 
#list:

#   Input: [2,3,8,9]
#   Output: square_list -> [4,9,64,81] 
#           cube_list   -> [8,27,512,729]

#at the 'same time' ('' quotes included as Python actually can never truly run 
#multiple threads at the same time due to GIL but only rapidly switches between threads during 
#idle time in seperate threads) via Multithreading


#Example of implementing Multithreading in Python:
import time
import threading

#This function takes in a list parameter and prints out the square of all numbers in the list
def calc_square(numbers):
    print("Calculating square numbers:")
    for n in numbers:
        #We tell the program to 'sleep()' for 0.2 seconds here in each iteration of the for
        #loop to provide idle time for Python to switch to execute the next thread, which will
        #be to execute 'calc_cube(numbers)' function. In actual context, True Multithreading
        #may occur, but sometimes programms cheat and does 'Multithreading' by keeping your CPU
        #at work even during idle time in a thread (such as during loading or waiting for a web 
        #service) by switching/divert processing power to work on other threads during this idle
        #time and resuming working on this thread when the idle time has ended (it may or may 
        #not still work on other threads though)
        time.sleep(0.2)
        print("Square number:", n*n)

#This function takes in a list parameter and prints out the cube of all numbers in the list
def calc_cube(numbers):
    print("Calculating cube numbers:")

    for n in numbers:
        #We tell the program to 'sleep()' for 0.2 seconds here in each iteration of the for
        #loop to provide idle time for Python to switch to execute the previous thread, which 
        #will be to execute 'calc_squre(numbers)' function again
        time.sleep(0.2)
        print("Cube number:", n*n*n)

numbers_array = [2,3,8,9]


#////////////////////////////////////////////////


#This is the first run of the program, without doing Multithreading. Notice the time taken to
#execute this Python program is about 1.6s (seen from 
#'time.time() - start_of_program_current_time_since_epoch')

#If you recall, 'time.time()' is defined as the current time passed since the epoch in seconds.
start_of_program_current_time_since_epoch = time.time()

calc_square(numbers_array)
calc_cube(numbers_array)

#This prints out the time taken to execute the codes above the 't' variable, to execute
#'calc_square(numbers)' and 'calc_cube(numbers)'. This works because we took the initial 
#'time.time()' (stored in variable 'start_of_program_current_time_since_epoch') before the 
#execution of the Python program, and then we took the 'time.time()' here again. We subtract 
#these 2 different 'time.time()' to obtain the time taken to run this Python program
print("Done in:", time.time() - start_of_program_current_time_since_epoch)
print("Hah... I am done with all my work!")

print("\n ///////////////// Centre Break /////////////////////// \n")


#First run output:
    # Calculating square numbers:
    # Square number: 4
    # Square number: 9
    # Square number: 64
    # Square number: 81
    # Calculating cube numbers:
    # Cube number: 8
    # Cube number: 27
    # Cube number: 512
    # Cube number: 729
    # Done in: 1.6117348670959473
    # Hah... I am done with all my work!


#///////////////////////////////////////////////////


#This is the second run of the program, with doing Multithreading. Notice the time taken to
#execute this Python program is much shorter (halved) about 0.8s (seen from 
#'time.time() - start_of_program_current_time_since_epoch2'), hence using Multithreading is
#better than the first run of the program
start_of_program_current_time_since_epoch2 = time.time()

#Instead of running 'calc_square(numbers_array)' and 'calc_cube(numbers_array)' one after
#another, we create them as threads via 'threading.Thread'.

#'target=' refers to the target worker function, of the tasks you want to execute (equivalent
#to the 'busy mom' tasks such as 'making phone call' or 'taking care of baby')

#'args=' refers the arguments that you will be passing through your target worker function.
#This parameter only accepts Tuples, so you need to put your argument(s) (if you have
#multiple) into a Tuple when inserting to this parameter
t1 = threading.Thread(target=calc_square, args=(numbers_array,))
t2 = threading.Thread(target=calc_cube, args=(numbers_array,))

#You need to add 'start()' to tell Python when you want to start the execution of your threads.
#By putting them like this, you are telling Python you want to execute these 2 threads in 
#'parallel'
t1.start()
t2.start()

#What 'join()' does is that it tells Python to wait here, and not execute any codes further down
#until the thread has finished its execution and 'rejoined' the main program
t1.join()
t2.join()

print("Done in:", time.time() - start_of_program_current_time_since_epoch2)
print("Hah... I am done with all my work!")


#Second run output:
    # Calculating square numbers:
    # Calculating cube numbers:
    # Square number: 4
    # Cube number: 8
    # Square number: 9
    # Cube number: 27
    # Square number: 64
    # Cube number: 512
    # Square number: 81
    # Cube number: 729
    # Done in: 0.8199136257171631
    # Hah... I am done with all my work!


#///////////////////////////////////////


#Analysis:
#Notice that the second run's output differs from the first run's output as in the first run's 
#output the 2 functions are being executed in sequence, one after another. However, in the
#second run, the 2 functions are run alternatively, as if they were running at the same time, 
#and has a shorter running time compared to the first run of the program.

#So how does Multithreading cause this alternating output and a shorter time?
#It does this by the first 'calc_square()' function runs and prints the first squared number, 
#then the for loop repeats. In the second loop, it started waiting/going idle at the 
#'time.sleep(0.2)'. While the program is waiting, since the other 'calc_cube()' function is
#being executed in parallel, the program runs this second function during the idle time, 
#iterating through the first for loop and printing the first cubed number. When the program
#meets 'time.sleep(0.2)' again in the second 'calc_cube()' function, it has idle time again,
#hence it switches back to running the first 'calc_square()' function because the program is
#'Multithreading', running these 2 function threads in parallel/at the same time.

#Less time is taken due to CPU making use of the idle time to run the 2 functions alternatively
#switching back and forth during the idle time within the for loops of the 2 functions instead
#of wasting the full 0.2 seconds waiting idly during the first run of the program, where the 2
#functions ran sequentially





