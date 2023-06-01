#Question 3:
#Create a list of all odd numbers between 1 and a max number. Max number is something you need to 
#take from a user using input() function

max_number = int(input('Please enter a Max Integer Number: '))

list_of_odd_numbers = []

for i in range(1, max_number+1):
    list_of_odd_numbers.append(i)
    
for i in list_of_odd_numbers:
    if i % 2 == 0:
        list_of_odd_numbers.remove(i)
        
print(list_of_odd_numbers)


#Solution (it is abit more concise than my provided answer):
#max = int(input("Enter max number: "))

#odd_numbers = []

#for i in range(1, max):
#    if i % 2 == 1:
#        odd_numbers.append(i)

#print("Odd numbers: ", odd_numbers)