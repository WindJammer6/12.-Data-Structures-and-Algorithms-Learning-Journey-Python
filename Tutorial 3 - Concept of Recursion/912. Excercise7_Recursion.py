#Question 7:  Write a Python program to find the greatest common divisor (GCD) of two integers.

#About the '%' symbol: The % symbol in Python is called the Modulo Operator. It returns the remainder 
#of dividing the left hand operand by right hand operand. It's used to get the remainder of a division 
#problem.

#My answer is wrong as I used iterative function instead of recursive
def GCD(a,b):

    common_divisors = []

    if a > b or a == b:                           #can use 'for i in range(1,min(a,b)) also so don't
        for i in range(1,b+1):                    #need split the scenarios into if a > b or a ==b, and
            if (a % i == 0) and (b % i == 0):     #else a < b
                common_divisors.append(i) 
            else:
                pass
    else:
        for i in range (1, a+1):
            if (a % i == 0) and (b % i == 0):
                common_divisors.append(i)
            else:
                pass
    return max(common_divisors)

if __name__ == '__main__':
    first_number = int(input('Please enter a number: '))
    second_number= int(input('Please enter a number: '))
    print(GCD(first_number, second_number))


#Sample answer
def Recursive_gcd(a, b):
	low = min(a, b)
	high = max(a, b)

    #For cases where the smaller number is divisible by the larger number and the code will 
    #return the smaller number as the greatest common divisor, (the new 'high' in the new recursive
    #loop). 
    
    #It is able to do this as during th enext recursive loop, due to the 'high%low' parameter which 
    #will be equal to 0 if the 'high' (larger number) is divisible by the 'low' (smaller number), 
    #and in the new recursive loop, the new 'low' will be 0 (the '%' symbol either returns 0 or 1), 
    #and will exit the recursive loop by returning the new 'high' (which will be the previous recursive 
    #loop's 'low' (please do not mistake the returned, new 'high' as the old 'high' (original larger 
    #number), it is the new 'high', not the original 'high' (original larger number)). The final output 
    #will be the new 'high', which is the smaller number.
	if low == 0:
		return high
    #For cases where in the first recursive loop, the 'low' (smaller number) is already 1, hence
    #greatest common divisor can only be 1 regardless of what is the larger number and exit the
    #recursive loop, returning 1 as the output
	elif low == 1:
		return 1
	else:
		return Recursive_gcd(low, high%low)
print(Recursive_gcd(7,14))

