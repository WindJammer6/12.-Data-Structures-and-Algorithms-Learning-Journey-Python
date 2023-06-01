#Question 6: Write a Python program to calculate the value of 'a' to the power of 'b'.
#Test Data :
#(power(3,4) -> 81 OR 3 x 3 x 3 x 3

def power(a,b):
    if b == 1:
        return 1
    return a * power(a, b-1)

if __name__ == '__main__':
    number = float(input('Please enter a number (can be decimal): '))
    to_power = int(input('Please enter a number (must be int): '))
    print(power(number, to_power))