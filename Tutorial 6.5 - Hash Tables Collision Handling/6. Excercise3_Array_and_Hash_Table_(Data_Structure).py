#Question 3:
#'poem.txt' contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in 
#python and print every word and its count as show below. 

#Think about the best data structure that you can use to solve this problem and figure out why you 
#selected that specific data structure.

#First storing the full text file into individual words as elements in an Array/List Data Structure,
#stripping any special characters and new lines, and splitting each word on the spacebar delimiter


#Since I am splitting them by each line in the text file, the split function creates a new list. Hence
#I need to create another for loop to append each word from the split function list to the main 
#'poem_words' list
poem_words = []
with open("poem.txt", "r") as file:
    for line in file:
        temp_list = line.strip('—,;:.!\n').split()
        for i in temp_list:
            poem_words.append(i)

#Now in order to make each word in the 'poem_words' into lowercase, I initially tried doing that to the
#'poem_words' list itself, which didn't work. For some reason, it would work if you append each word
#to another list after lowercasing it from the initial 'poem_words' list
poem_words_lower = []
for word in poem_words:
    poem_words_lower.append(word.lower())

#From Googling, in order to find the frequency of each element in an array/list, you would use a 
#Hash Table/dictionary, with the key being the counter, and value being each unique word
word_frequency = {}
for word in poem_words_lower:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

#Array Data Structure
print(poem_words_lower)

#Hash Table Data Structure
print(word_frequency)