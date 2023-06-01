#This computer program is in the Big O Notation of O(n^2) in Time Complexity as well

#Its also about finding duplicate numbers in a list of numbers

#time = a*n^2 + b*n + c

#By the 2 steps, 
#    1. Keep fastest growing term, which is a*n^2
#    2. Drop constants, which gives you n^2
#It is Big O Notation O(n^2) (you can ignore b*n as when n becomes very big, n becomes insignificant
#compard to n^2)

numbers = [3,2,4,3,6,8,6]

#This chunk of code undergoes n^2 iterations
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            numbers[i] = None
            break

#This chunk of code undergoes n iterations
for i in range(len(numbers)):
    if numbers[i] == None:
        print(f'The number at index {i}, in the list has a duplicate')