#Question 2: Write a Python program to get the factorial of a non-negative integer.

#Whats a factorial?
#5! = 1 x 2 x 3 x 4 x 5

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    number_to_factorial = int(input('Enter a number to factorial: '))
    print(factorial(number_to_factorial))
