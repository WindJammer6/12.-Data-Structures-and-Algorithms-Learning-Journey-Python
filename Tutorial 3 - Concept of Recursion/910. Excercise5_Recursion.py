#Question 5: Write a Python program to calculate the harmonic sum of n-1.
#Note: The harmonic sum is the sum of reciprocals of the positive integers.
#Example: 1 + 1/2 + 1/3 + 1/4 + ...
def harmonic_sum(n):
    if n < 2:                    #Shouldnt use n == 0 as it will crash the program if user decides to
        return 1                 #put negative number
    return 1/n + harmonic_sum(n-1) 

if __name__ == '__main__':
    number = int(input('Please enter a number: '))
    print(harmonic_sum(number))