#Question 1: Write a Python program to calculate the sum of a list of numbers (using recursion function).

#My answer is wrong as I used iterative function instead of recursive
def sum_list(number_list):
    sum = 0
    for i in number_list:
        sum = sum + number_list[i]
    return sum

if __name__ == '__main__':
    length_of_list = int(input('How long should the list of numbers be: '))

    number_list = []
    for i in range(0,length_of_list):
        number_list.append(i)
    print(sum_list(number_list))


#Sample answer:
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
        
print(list_sum([2, 4, 5, 6, 7]))