#Question 3: Write a Python program to get the sum of a non-negative integer.

#My answer correct
def sumDigits(number_string):
    if len(number_string) == 1:
        return number_string
    return number_string[0] + number_string[1:] 

if __name__ == '__main__':
    number_string = str(input('Enter string of numbers you want the sum of: '))
    print(sumDigits(number_string))

#Sample number
def sumDigits2(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits2(int(n / 10))

print(sumDigits2(345))
print(sumDigits2(45))
