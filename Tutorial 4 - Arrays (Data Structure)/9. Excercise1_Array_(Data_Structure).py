#Question 1:
#Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190

#Create a list to store these monthly expenses and using that find out,
#a. In Feb, how many dollars you spent extra compared to January?
#b. Find out your total expense in first quarter (first three months) of the year.
#c. Find out if you spent exactly 2000 dollars in any month.
#d. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list.
#e. You returned an item that you bought in a month of April and got a refund of $200. Make a correction 
#   to your monthly expense list based on this.

monthly_expense = [2200,2350,2600,2130,2190]

#a.
print(monthly_expense[1] - monthly_expense[0])

#b.
print(sum(monthly_expense[0:3]))               #'sum(array, starting number)' function takes in 
                                               #2 parameters, as described above. e.g.
#c.                                            #sum(monthly_expense, 1000), means 
for i in monthly_expense:                      #(total of monthly_expense list) + 1000
    if i == 2000:
        print('I spent exactly 2000 in this month')
    print('I did not spend exactly 2000 in this month')

#d.
monthly_expense.insert(5, 1980)
print(monthly_expense)

#e.
monthly_expense[3] = monthly_expense[3] + 200
print(monthly_expense)


#Better answer for c. and d. (rest is the same as solution)
#c.
print("Did I spent 2000$ in any month? ", 2000 in monthly_expense)

#d.
#monthly_expense.append(1980) (Using the 'append()' function)
#print("Expenses at the end of June:",monthly_expense)