#Here are 2 relatively simple functions, 'calc_square()' and 'calc_cube()' 

#'calc_square()' function takes in a List of numbers, and squaring all the numbers in that List, and 
#then returning another List storing all the squared numbers.
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

#'calc_cube()' function takes in a List of numbers, and cubes all the numbers in that List, and 
#then returning another List storing all the cubed numbers.
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


#This is the input List (Added the right limit number as '100001' to include '100000', while excluding
#'100001'). It needed to be a big List in order to make any noticable time duration differences in run 
#time between the 2 functions
array = range(1,100001)
output_square = calc_square(array)
output_cube = calc_cube(array)

print(output_square)
print(output_cube)