#This computer program is in the Big O Notation of O(n^2) in Time Complexity

#Its about finding duplicate numbers in a list of numbers

#This is because of the 2 for loop (iteration) in the code will loop for n*n number of times (number of 
#elements in the 'numbers' list), 1st n number of loops to iterate through the list to select every 
#element in the list, and 2nd n number of loops to iterate/scan every other element after the selected 
#element to check for matching numbers as the selected number before the code will produce the output.

#time = a*n^2 + b

#By the 2 steps, 
#    1. Keep fastest growing term, which is a*n^2
#    2. Drop constants, which gives you n^2
#It is Big O Notation O(n^2)

numbers = [3,6,2,4,3,6,8,9]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):              #The 'range()' function takes up to 3 parameters,
        if numbers[i] == numbers[j]:                #e.g. 'range(3, 20, 2)', giving you a sequence of
            print(f'{numbers[i]} is a duplicate')   #numbers 3 to 19, but increment of 2 instead of 1
            break                                   #(prints every alternate number instead of all numbers)

