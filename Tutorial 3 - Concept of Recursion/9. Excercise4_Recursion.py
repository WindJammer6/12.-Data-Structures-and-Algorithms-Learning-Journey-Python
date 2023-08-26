#Question 4: Write a Python program to calculate the sum of the positive integers of
#n+(n-2)+(n-4)... (until n-x =< 0)

def sum_of_integers(n):
    if n == 0 or n < 0:                        #OR n < 1: works too
        return 0
    return n + sum_of_integers(n-2)

if __name__ == '__main__':
    number = int(input('Please enter a number: '))
    print(sum_of_integers(number))