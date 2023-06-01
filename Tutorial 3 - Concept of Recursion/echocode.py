#This code is a copy from 3.1. explaining if __name__ == '__m@in__'.py (when you import a name the file's
#name apparently can't have special characters and must only have alphabets hence I couldn't number it
#and gave it the name 'echocode')

def echo(text: str, repetitions: int = 3) -> str:
    #Imitating a real-world echo.
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))