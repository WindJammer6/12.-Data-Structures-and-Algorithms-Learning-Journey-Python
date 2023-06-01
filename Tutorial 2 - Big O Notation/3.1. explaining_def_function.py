#Explaining Python's self-made function's accepted parameters
#(side-tracking abit from Data Structures and Algorithms)

#This is the code from the previous file in this folder.

#def main():
#    price_list = [100,200,300,400,500,600]             
#    eps_list = [2,4,6,8,10,12]
#    print(find_first_eps(price_list, eps_list, 2))

#def find_first_eps(prices, eps, index):
#    pe = prices[index]/eps[index]
#    return pe          

#Now, how exactly does the line of code for the self-defined function work?
#    def find_first_eps(prices, eps, index):
#    ...
#According to documentation, there is no limit to how many parameters a self-made function can have,
#as long as you provide the SAME number of parameters into the self-made function in the main code. 
#(no more, no less)

#Hence in this case, the function defined to take 3 parameters, 'prices', 'eps' and 'index', and expects
#3 parameters to be provided in the main code, which there is 'price_list', 'eps_list' and '2'. And hence
#the code works.


#//////////////////////


#Other parameters accepted:
#1. *args (arguments)
#For if you do not know how many arguments that will be passed into your function, add a '*' before the 
#parameter name in the function definition. (hence in main code can put as many arguments as you want)
#The function will then accept a tuple of arguments can access each element accordingly (by index)
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#2. Keyword arguments (using key-value syntax)
#(BTW the way the order of the arguments does not matter in the self-made function and in main code,
#but the parameter name must be the same in the self-made function and main code as it uses the
#exact key name provided in the main code to run the code in the self-made function)
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#3. **kwargs (arbitrary keyword arguments)
#For if you do not know how many keyword arguments that will be passed into your function, add 
#two asterisk '**' before the parameter name in the function definition. (hence in main code can 
#put as many key-value pairs as you want)
#The function will then accept a dictionary of arguments, and can access the items accordingly (by key)

def my_function(**kid):
  print("His last name is " + kid["lastname"])

my_function(firstname = "Tobias", lastname = "Refsnes")

#4. Default Parameter Value
#You can enter a default parameter value if in the main code there is no argument received, by
#adding a '=' after after a function's parameter then it will use that default parameter value to run 
#the code inside the self-made function if there that parameter is not provided
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#5. The 'pass' Statement
#Self-made function definitions cannot be empty, but if you for some reason have a function definition 
#with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass


#///////////////////


#Side note: Recursion in a self-made function
#Python also accepts function recursion, which means a defined function can call itself within the
#function. (More in the Data Structures and Algorithms folder later)
