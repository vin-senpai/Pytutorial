#A clean version of the program.


#The project consist of three topics:
#Introduction to programming.
#Basic Syntax
#and Relational operators.


#The flow of the program goes like this:
#Shows the main screen -> ask user to choose a topic(between 1-3) -> load the topic through print and raw strings -> user can enter/type q or c to continue or quit the program.


#topic var
topic = 0
#First topic
def topic1():
    #make topic global to access
    global topic
    ##first content
    content_intro = """
                                        #Introduction to python programming.

*What is a programming language?

  -programming languange is a special type of languange that's used to communicate with computers.        
  they are created to make doing computer instructions much easier.

  
  -example of an programming languange is Python. 
  Python is a widely used multi-purpose programming languange that is considered 
  an easier programming languange than other type of programming languange(like C, C++..etc).
  it is closely similar to english words that's why it is easy to use.

  -Python was created by a dutch software engineer Guido van Rossum on 1991. He made python with the purpoes of
  making programming languange easy to write and read while also remaining a powerful languange.
"""
#We divide the text so that it will be presentable and clean.
    content_intro2 = """#Where is python used?

  -Python is used on a lot of things, but most of the time it is used on data analysis and machine learning(A.I), but python is not limited
  on that. it can also be used to make games(pygame), make a app(kivy), web development(Django/Flask), or for making an script that can 
  automate task on your PC.  
""" 

    print(content_intro)
    #wait for any input so that it will print the second part.
    input("")
    print(content_intro2)


    #ask user to go back to main menu or continue next page.
    user_choice = str(input("press q to go back to main menu | press n to move to next topic     "))
    
    if user_choice.__contains__('q'):
        topic = -1
    elif user_choice.__contains__('n'):
        topic += 1
    

#Second topic
def topic2():
    #make topic global to access
    global topic
    #second content(basic syntax):
    content_syntax1 = """
                                                        #Basic Python syntax
*Python syntax are like a simple english words. words are to used to communicate to other people. just like on python(or any other programming languange),
Syntax are like words, they are simple words used to perform a specific task(like to draw, to load something etc...).there are a lot of python syntax but,
we will only tackle a little bit of them.


*The first and most used syntax on python is Print().
-Print is used to display something to the terminal(screen). for example to print 'Hello world':
"""

    content_syntax2 = """
Code
+-----------------------+
|print("Hello World)"   |
|                       |
|                       |
+-----------------------+

Output
+-------------+
|Hello world  |
|             |
+-------------+      


"""

    content_syntax3 = """
*Next one is input().
-Input is used to take user input from the terminal. it's just the way of computer asking the user to communicate/or send any message. """


    content_syntax4 = """
Example:    
Code
+--------------------------------------------------------------------------------------------------+
|question = input("What is your name?") #This is a variable. we will tackle it later on.           |
|print("Hello " + question)                                                                        |
+--------------------------------------------------------------------------------------------------+

Output
+--------------------------------+
|What is your name? Luffy        |
|Hello Luffy                     |
|                                |
+--------------------------------+

"""

    #Print content
    print(content_syntax1)
    #wait for user input to continue
    input("press Enter to continue \n\n")
    print(content_syntax2)
    input("press Enter to continue \n\n")
    print("\n" * 40)
    print(content_syntax3)
    input("press Enter to continue \n\n")
    print(content_syntax4)


    #ask user to go back to main menu or continue next page.
    user_choice = str(input("press q to go back to previous topic | press n to move to next topic     "))
        
    if user_choice.__contains__('q'):
        topic -= 1
    elif user_choice.__contains__('n'):
        topic += 1

#Third topic
def topic3():
    #Make topic global to access 
    global topic

    #This one will tackle variables and basic arithmetic operations
    content_variables1 = """
                                                    #Variables
*Variables are like containers/box. they are used to store different kind of items. in python, variables
stores different data type. they are different data types on python:
-Int -> Numbers.
-Str/String -> Texts.
-Float/Double -> decimals like 0.5, 0.6 etc
-Boolean -> True or False
"""
    content_variables2 = """
*Data types are kind of identifiers(I.D). they are used to determine what is what or which is which on a program/code.
Just imagine it like this, Variable is the Box, while the data type is the content of the box. variables can be named,
just like how you put a name on a Box.
"""

    content_variables3 = """
Example:
+---------------------------------------------------------------------------------------------------------+
|box1 = 10 #This box contains a number(Int)                                                               |
|box2 = "Hello world!" #This one is a text(String). remember to always surround it on a Double quotation. |
|box3 = 0.5 #this one is a decimal(float/double)                                                          |
|box4 = True #This one is a boolean. it can only contain True or False                                    |
+---------------------------------------------------------------------------------------------------------+

*Inorder to print the value of the variables, you just put it inside the print() syntax
"""

    content_variables4 = """

Example:
Code
+---------------------------------------+
|print(box1) #Outputs 10                |
|print(box2) #Outputs "Hello world!"    |
|print(box3) #Outputs 0.5               |
|print(box4) #Outputs True              |
+---------------------------------------+

Output
+-------------------+
|10                 |
|Hello world!       |
|0.5                |
|True               |
+-------------------+
"""
    #Print the contents
    print(content_variables1)
    input("press Enter to continue")
    print(content_variables2)
    input("press Enter to continue")
    print(content_variables3)
    input("press Enter to continue")
    print(content_variables4)


    #ask user to go back to main menu or continue next page.
    user_choice = str(input("press q to go back to previous topic | press n to move to next topic     "))
            
    if user_choice.__contains__('q'):
        topic -= 1
    elif user_choice.__contains__('n'):
        topic += 1

#Fourth topic
def topic4():
    #Make topic accessable globally
    global topic
    #Content
    content_arithmetic = """
                                            #Arithmetic operation
*Now that we understand how variables and data types work together, we will now tackle arithmetic operations!
Arithematic operations are mathematical operations that can be used to add, subtract, multiply, or divide a value.
Here are a list of arithemetic operation on python:
"""

    content_arithmetic2 = """
+-------------------------------------------------------------------------------+         
|   + --> Addition       | 5 + 1 = 6                                            | 
|   - --> Subtraction    | 5 - 1 = 4                                            |
|   / --> Division       | 5 / 2 = 2.5                                          |
|   * --> Multiplication | 10 * 2 = 20                                          | 
|  // --> Floor division | 5 // 2 = 2 #Notice that it outputs 2 instead of 2.5  |
|   % --> Modulus        | 10 % 3 = 1                                           |
|  ** --> Exponentiation | 5 ** 2 = 25 #It's the same as 5 x 5                  |
+-------------------------------------------------------------------------------+
"""

    content_arithmetic3 = """
*The arithemtic shown can be performed on variables(only Int and Float). Here's an example:

"""
    content_arithmetic4 = """
Code
+-----------------------------------+
|box1 = 10                          |
|box2 = 5                           |
|result = box1 + box2 # 10 + 5      |
|print(result) # 15                 |
+-----------------------------------+

Output
+-------------------+
|15                 |
|                   |
+-------------------+
"""


    #prints the content
    print(content_arithmetic)
    input("press Enter to continue")
    print(content_arithmetic2)
    input("press Enter to continue")
    print(content_arithmetic3)
    input("press Enter to continue")
    print(content_arithmetic4)

    #ask user to go back to main menu or continue next page.
    user_choice = str(input("press q to go back to previous topic | press n to move to next topic     "))
            
    if user_choice.__contains__('q'):
        topic -= 1
    elif user_choice.__contains__('n'):
        topic += 1

#Main screen/Main menu
def main_menu():
    #Topic variable to choose topic from lessons.
    global topic
    #The content
    content = r"""
Welcome to Pytutorial book!
please choose a topic:
    1. Introduction to programming.
    2. Basic syntax.
    3. Variables
    4. Arithmethic operation
    5. Relational operations
"""

    print(content) #print content

    #ask user for choices
    choices = int(input("Please enter a topic(1-3): "))

    match choices:
        case 1:
            topic = 1
        case 2:
            topic = 2
        case 3:
            topic = 3
        case 4:
            topic = 4
        case _:
            raise ValueError("Invalid value! only accepts between 1-5!")


#The main loop
main_menu()

ext = False
while not ext:
    if topic == 1:
        print("\n" * 50)
        topic1()
    elif topic == 2:
        print("\n" * 50)
        topic2()
    elif topic == 3:
        print("\n" * 50)
        topic3()
    elif topic == 4:
        print("\n" * 50)
        topic4()
    elif topic == -1:
        main_menu()
    #ask user to go back to main menu or go to next topic

   


    

    


