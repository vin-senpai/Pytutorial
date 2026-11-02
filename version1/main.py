#A clean version of the program.


#The project consist of three topics:
#Introduction to programming.
#Basic Syntax
#and Relational operators.


#The flow of the program goes like this:
#Shows the main screen -> ask user to choose a topic(between 1-3) -> load the topic through print and raw strings -> user can enter/type q or c to continue or quit the program.


#topic var
topic = 0
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
Input
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
-Input is used to take user input from the terminal. it's just the way of computer asking the user to communicate/or send any message.
Example:

Input
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
    print(content_syntax3)
    
    #ask user to go back to main menu or continue next page.
    user_choice = str(input("press q to go back to main menu | press n to move to next topic     "))
        
    if user_choice.__contains__('q'):
        topic -= 1
    elif user_choice.__contains__('n'):
        topic += 1
      
def topic3():
    pass

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
    3. Relational operator.
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
        case _:
            raise ValueError("Invalid value! only accepts 1,2 or 3!")


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
        topic3()
    elif topic == -1:
        main_menu()
    #ask user to go back to main menu or go to next topic

   


    

    


