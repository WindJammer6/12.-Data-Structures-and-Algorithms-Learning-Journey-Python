#About Python's 'import' function:
#You can import other files from the same directory to this file, much like how you import a Python
#library. 

#Stuff you can import from another file:
#-> Module: simply a file with a . py extension.
#-> Package: a directory containing an __init__.py file and normally other modules.
#-> Built-in Module: A module that is natively installed with Python.
#-> Object: Anything inside a module/package that can be referenced such as a class, function, 
#   or variable.

#/////////////////////

#Lets try importing the file from 'echocode' to this file.

#We will see how the 'if __name__ == "__main__":' (this code is in the '3.1. explaining if __name__ == 
#'__m@in__'.py' file) works from the other file in this file:

import echocode

text = input("Yell something into a cave: ")
print(echocode.echo(text))

#Lets run this file. The output you will see is that you are only prompted to 'Yell something into a
#cave: ' instead of a mountain as the 'if __name__ == "__main__":' function in the 'echocode' file
#is False when it tries to run in this file (as the full 'echocode' file will be scanned to run, 
#thats how the 'import' function works) but due to the if statement in 'if __name__ == "__main__":' 
#being False, the code under it ('which would have prompted 'Yell something at a mountain') does not 
#run here, while only the code above here will run instead.

#If you try removing the 'if __name__ == "__main__":' function in the 'echocode' file you will find that
#there is a double run of code, the first prompting you to 'Yell something at a mountain', from the
#'echocode' itself, as there is no 'if __name__ == "__main__":' statement preventing it from running
#here, and a second prompting you to 'Yell something into a cave', from the code in this file.

#In conclusion, what 'if __name__ == "__main__":' does is that it is used to control the behavior of 
#our Python code for when it's executed directly (in the same file where it originated from) 
#or imported as a module.