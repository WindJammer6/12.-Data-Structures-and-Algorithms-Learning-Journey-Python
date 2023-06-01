#Question 2:
#'nyc_weather.csv' contains new york city weather for first few days in the month of January. Write a 
#program that can answer following:

#-> What was the temperature on Jan 9?
#-> What was the temperature on Jan 4?

#Figure out data structure that is best for this problem

#Setting up the Data Structure:
weather = {}
with open("nyc_weather.csv", "r") as file:
    for line in file:
        split_list = line.strip().split(',')
        key = split_list[0]
        value = split_list[1]
        #'.update()' is the equivalent to '.append()' (adding element to a List) to add a new element 
        #(key-value pair) to a Dictionary
        weather.update({key:value})

#Cannot remove by index as dictionaries do not have indexes and can only remove by specifying the
#key-value pair's key
del weather['date']

#The most suitable Data Structure for this problem is a Hash Table (or a Dictionary in Python)
print(weather)

#-> What was the temperature on Jan 9?
print(weather['Jan 9'])

#-> What was the temperature on Jan 4?
print(weather['Jan 4'])


#////////////////////////////////////////////////


#Solution:
#Setting up the Data Structure:
weather_dict = {}

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("Invalid temperature. Ignoring the row")

#The best data structure to use here was a dictionary (internally a hash table) because we wanted to know
#temperature for specific day, requiring key, value pair access where you can look up an element by day 
#using O(1) complexity
print(weather_dict)

#-> What was the temperature on Jan 9
weather_dict['Jan 9']

#-> What was the temperature on Jan 4
weather_dict['Jan 4']