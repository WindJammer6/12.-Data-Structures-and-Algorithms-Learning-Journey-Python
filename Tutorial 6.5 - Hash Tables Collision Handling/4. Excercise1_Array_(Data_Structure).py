#Question 1:
#'nyc_weather.csv' contains new york city weather for first few days in the month of January. Write a 
#program that can answer following:

#-> What was the average temperature in first week of Jan?
#-> What was the maximum temperature in first 10 days of Jan?

#Figure out data structure that is best for this problem.

#Setting up the Data Structure:
weather = []
with open("nyc_weather.csv", "r") as file:
    for line in file:
        #Had to use 'strip()' function here as some of the values have '\n' behind them
        split_list = line.strip().split(',')
        temperature = split_list[1]
        weather.append(temperature)

#Removing the headers 'temperature(F)'
weather = weather[1:]

#Converting the elements in the list to integers instead of strings
weather_ints = []
for i in weather:
    i = int(i)
    weather_ints.append(i)

#The most suitable Data Structure for this problem is an Array (or a List in Python)
print(weather_ints)

#-> What was the average temperature in first week of Jan?
#Adding up the temperatures from index 0 to 7 in the csv file, so can divide by the total number with the
#number of days later from index 0 to 7 (7) to find average temperature
number = 0
for i in weather_ints[0:7]:
    number += i

average_temperature = number/len(weather_ints[0:7])

print(average_temperature)

#-> What was the maximum temperature in first 10 days of Jan?
print(max(weather_ints))

#OR 
#Can try implementing it without the function, aligning the numbers in the array in ascending 
#order/value then taking the largest value


#////////////////////////////////////////////////


#Solution:
#Setting up the Data Structure:
arr = []

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature. Ignoring the row")

#The best data structure to use here was a list because all we wanted was access of temperature elements
print(arr)

#-> What was the average temperature in first week of Jan?
sum(arr[0:7])/len(arr[0:7])

#-> What was the maximum temperature in first 10 days of Jan
max(arr[0:10])
