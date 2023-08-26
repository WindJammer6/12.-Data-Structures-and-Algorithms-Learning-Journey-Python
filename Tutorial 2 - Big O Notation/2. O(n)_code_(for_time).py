#This computer program is in the Big O Notation of O(n) in Time Complexity

#Its about taking a list of numbers and returning another list of the numbers after squaring it

#This is because the for loop (iteration) in the 'get_squared_numbers(numbers)' function will loop for
#n number of times (number of elements in the 'numbers_list') before the code will produce the output.

#time = a*n + b

#By the 2 steps, 
#    1. Keep fastest growing term, which gives you a*n
#    2. Drop constants, which gives you n
#It is Big O Notation O(n)

def main():
    numbers_list = [2,5,8,9]
    print(get_squared_number(numbers_list))


def get_squared_number(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

main() 