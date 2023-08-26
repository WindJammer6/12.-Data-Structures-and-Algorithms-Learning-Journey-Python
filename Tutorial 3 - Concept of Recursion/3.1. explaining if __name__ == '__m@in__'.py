#Came across something completely new to me in Python in this tutorial, so figured I'll side track
#a little to explain what 'if __name__ == '__main__':' is

#Basically how it works is that it works somewhat like 'def main()' but a little more than
#just an entry point to your code

#It is a conditional statement (cuz of the 'if' statement), and basically runs the code underneath
#it, if the conditional is True, which will always be True, if you run it normally like a normal
#Python script/file like so:

def echo(text: str, repetitions: int = 3) -> str:
    #Imitating a real-world echo.
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))

#So, since the if statement in 'if __name__ == "__main__":' will always be True whenever you run a
#normal Python script/file normally and basically just run the code underneath, it, then whats
#the point of this code?

#This line of code becomes very important when you are importing this file to other files and
#want to use the functionality of this file's code into other files


#Let me explain abit more on what each word mean in 'if __name__ == "__main__":'
#__name__ means name of the file you are currently running
#"__main__" means the main file where the code came from

#So, 'if __name__ == "__main__":' means if the file name you are running is the file where this code 
#originated from (not imported from/to), this conditional will be True, and the codes under
#'if __name__ == "__main__":' will run while if this file is imported script/file to another Python
#file, the code under 'if __name__ == "__main__":' will not run as the if statement will be False
#as in the other file the name of that other file, is not '==' '__main__', (name of the other file is
#not equal to the main file the code originated from.