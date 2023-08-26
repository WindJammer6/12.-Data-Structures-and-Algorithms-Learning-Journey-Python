#Question 2:
#You have a list of your favourite marvel super heroes.
#heroes=['spider man','thor','hulk','iron man','captain america']

#Using this find out,
#a. Length of the list
#b. Add 'black panther' at the end of this list
#c. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first 
#   and then add it after 'hulk'
#d. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is 
#   cool). Do that with one line of code.
#e. Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions 
#   available in list)

marvel_heroes = ['spider man','thor','hulk','iron man','captain america']

#a.
print(len(marvel_heroes))

#b.
marvel_heroes.append('black panther')
print(marvel_heroes)

#c.
marvel_heroes.remove('black panther')
marvel_heroes.insert(3, 'black panther')
print(marvel_heroes)

#d.
marvel_heroes[1:3] = ['doctor strange']
print(marvel_heroes)

#e.
marvel_heroes.sort()
print(marvel_heroes)

#print(sorted(marvel_heroes)) works too