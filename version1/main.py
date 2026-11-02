#A clean version of the program.


#The project consist of three topics:
#Introduction to programming.
#Basic Syntax
#and Relational operators.


#The flow of the program goes like this:
#Shows the main screen -> ask user to choose a topic(between 1-3) -> load the topic through print and raw strings -> user can enter/type q or c to continue or quit the program.



#Topics

def topic1():
    #shows topic about introduction to python programming
    content = """
*Introduction to python programming.

""" 
    print("\n" * 100) #This acts as a clear() function to clear the terminal.
    print(content)
def topic2():
    pass
def topic3():
    pass

#Main screen/Main menu
def main_menu():
    #The content
    content = r"""
Welcome to Pytutorial book!
please choose a topic:
    1. Introduction to programming.
    2. Basic syntax.
    3. Relational operator.
"""

    print(content) #print content

    #ask user for choices
    choices = int(input("Please enter a topic(1-3): "))

    match choices:
        case 1:
            topic1()
        case 2:
            topic2()
        case 3:
            topic3()
        case _:
            raise ValueError("Invalid value! only accepts 1,2 or 3!")




main_menu()    

