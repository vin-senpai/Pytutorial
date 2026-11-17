#This is the version 2 of the program. this time, it has UI using tkinter. we will add some editor, quiz, and a lot of things in here.

import tkinter
import tkcode
import subprocess
import sys
import os
from tkinter import ttk


#Initialize the window 
root = tkinter.Tk()
root.geometry("1280x900")
#set the root screen
root.columnconfigure(0,weight=2)
root.rowconfigure(0,weight=1)

panedwin = None
#style
style = ttk.Style()
style.theme_use("clam")
print(sys.executable)
#For textx
style.configure(
    "main.TLabel",
    font=("ansi",50),
    foreground = "#ffffff",
    background = "#706000"
)

style.configure(
    "learn.TLabel",
    font=("Arial", 12)
)


#For frame
style.configure(
    "TFrame",
    background = "#202020"
)
#For button

style.configure(
    "main.TButton",
    font=("Arial", 30),
    background="#21a2da",
    borderwidth=0,
)

style.configure(
    "codeeditorrun.TButton",
    background="red",
    foreground="white"
)

style.configure(
    "codeeditorclear.TButton",
    background="darkgray"
)

style.map(
    "main.TButton",
    foreground = [('active','pink'),('pressed', 'red'),('!active', 'white')],
    background = [('active', 'darkblue'),('pressed', 'red')]
)

style.map(
    "codeeditorrun.TButton",
    background = [('active','darkred')]
)

style.map(
    "codeeditorclear.TButton",
    background=[('active', 'gray')]
)





#This is where the page(intro to program, syntax..etc) goes. we will make it in one function inorder to easily manage it.
def learn():
    #Access the page variable and make maincontent global for change_page function a
    global page
    global maincontent
    #Clear the current screen.
    for children in frame.winfo_children():
        children.destroy()
    
    #Initialize the content variable
    
    rawstring = """
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

  #Where is python used?

  -Python is used on a lot of things, but most of the time it is used on data analysis and machine learning(A.I), 
  but python is not limited on that. it can also be used to make games(pygame), make a app(kivy), web development(Django/Flask), 
  or for making an script that can 
  automate task on your PC.  
  

   #Basic Python syntax
  *Python syntax are like a simple english words. words are to used to communicate to other people. just like on python(or any other programming languange),
  Syntax are like words, they are simple words used to perform a specific task(like to draw, to load something etc...).there are a lot of python syntax but,
  we will only tackle a little bit of them.
  
  
  *The first and most used syntax on python is Print().
  -Print is used to display something to the terminal(screen). for example to print 'Hello world':

  *Next one is input().
-Input is used to take user input from the terminal. it's just the way of computer asking the user to communicate/or send any message. 
"""
    #this is the part 2 of raw string.
    rawstring2 = """
                                                        #Variables
*Variables are like containers/box. they are used to store different kind of items. in python, variables
    stores different data type. they are different data types on python:
-Int -> Numbers.
-Str/String -> Texts.
-Float/Double -> decimals like 0.5, 0.6 etc
-Boolean -> True or False

*Data types are kind of identifiers(I.D). they are used to determine what is what or which is which on a program/code.
Just imagine it like this, Variable is the Box, while the data type is the content of the box. variables can be named,
just like how you put a name on a Box. 

*Inorder to print the value of the variables, you just put it inside the print() syntax
Example:


                                                    #Arithmetic operation
*Now that we understand how variables and data types work together, we will now tackle arithmetic operations!
Arithematic operations are mathematical operations that can be used to add, subtract, multiply, or divide a value.
Here are a list of arithemetic operation on python: 

                                                    #Relational Operator
*Relational operator are used to compare two values. just like in Math, we used ==(is equals), >(greater than), <(less than). 
Most of the time, we use this inside an IF block(a syntax used for making decision). ENDD

*What is IF?
-(if) keyword is used to make decision on python. we put conditions inside and then it will check if it's True or Not.
-for example:


Python has a variety of operators it can used to compare values.
Here's and table of python's relational operator:


"""
    #make the content variables global 
    global content1
    global content2
    global content3
    global content4
    global content5
    global content6
    global content7
    global content8
    global content9
    global content10
    global panedwin
    #Split the raw strings into content parts
    content1 = rawstring[0:760] #intro 
    content2 = rawstring[760:1105]
    content3 = rawstring[1097:1496] #Syntax
    content4 = rawstring[1495:1650]
    content5 = rawstring[1652:1900]
    #content 6 and above use another rawstring variable(because the index number is alread too high!)
    content6 = rawstring2[50:361] #Variables
    content7 = rawstring2[357:634]
    content8 = rawstring2[636:732]
    content9 = rawstring2[787:1085] #Arithmethic
    content10 = rawstring2[1140:1372] 
    
    print(f"Start: {rawstring2.find("Relational Operator")}")
    print(f"End: {rawstring2.find("ENDD")}")
    
    maincontent = tkinter.StringVar()
    #Apply the string on the maincontent stringvar
    maincontent.set(content1)

     #The frame for learning section.
    panedwin = ttk.Panedwindow(frame,width=500,height=500)
    panedwin.grid(column=1,row=4,pady=130)
    panedwin.columnconfigure(1, weight=3)
    panedwin.rowconfigure(1,weight=3)
    #The main text widget
    txt = ttk.Label(panedwin, textvariable=maincontent, style="learn.TLabel", wraplength=450, relief='sunken')
    txt.grid(column=1,row=0)
    #The buttons.
    next = ttk.Button(panedwin, text="Next",command=lambda: change_page(1)).grid(column=2,row=3,padx=5,pady=7)
    prev = ttk.Button(panedwin, text="Previous", command=lambda: change_page(-1)).grid(column=0,row=3,padx=5,pady=10)


    #Insert the panedwin on the frame.
    #load the code editor but hide it first.
    code_editor()
    codeeditor.grid(column=1,row=2)
    codeeditor.master.grid_forget()
    panedwin.insert()



    


#This is the output function to show the output of the code from the codeeditor.
def output(main):
    #Set the main editor.
    if main == 1:
        current_editor = codeeditor
    elif main == 2:
        current_editor = playground_editor
    else:
        raise ValueError("Invalid input")
   
    #first we save the python file
    current_editor.save_to_file("outputfile.py")
    #then we get the file name
    file = "outputfile.py"
    #here we use the subprocess module to communicate with python so that the file will be compiled.
   #output = subprocess.Popen([sys.executable,"-u",file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,stdin=subprocess.PIPE,text=True)
    #output = subprocess.Popen(["cmd", "/k", sys.executable,file])

    logpath = os.path.abspath("log.txt") #The name of the log file to store our program logs
    subprocess.run(f'start /wait "" cmd /c " {sys.executable} "outputfile.py" -u > "{logpath}" 2>&1" ',shell=True) #This function will create a window a open cmd to run our python script

    #And then we store the result into our widget.
    ##First we need to open and read the log file 
    with open('log.txt','r') as log:
        result = log.read()
    ##we just use another tkinter window in here so the user can easily close the output window instead of text.
    
    global output_window
    output_window = tkinter.Toplevel()
    if result:
        ttk.Label(output_window, text="OUTPUT: ", font=("Arial",30,"bold"),anchor="center").grid(row=0, ipadx=20)
        ttk.Label(output_window, text=result, font=("Monospace",40)).grid(row=1)

    output_window.mainloop()

#The playground
def playground():
    #Clear the root window

    for i in root.winfo_children():
        i.destroy()

    #Load the editor    
    global side_frame
    playground_frame = ttk.Frame(root)
    side_frame = ttk.Frame(root)

    side_frame.pack(side=["left"],expand=1)
    playground_frame.pack(side="right",expand=1)

    #Add buttons

    #Save button
    save_btn = ttk.Button(side_frame, text="Save")
    save_btn.grid(row=1)

    #Load button
    load_btn = ttk.Button(side_frame, text="Load")
    load_btn.grid(row=2)

    #Run button
    run_btn = ttk.Button(side_frame, text="Run", command=lambda: output(2))
    run_btn.grid(row=3)

    #Back button
    back_btn = ttk.Button(side_frame,text="Back",command=goback)
    back_btn.grid(row=4,pady=30)
    #Make the editor global
    global playground_editor


    playground_editor = tkcode.CodeEditor(playground_frame,font=("Arial",20))
    playground_editor.grid(column=1)


def goback():
    #Clear the root window

    playground_editor.master.grid_remove()
    #Load the main screen.
    side_frame.pack_forget()

    #Delete the remaing widgets
    for ii in root.winfo_children():
        ii.destroy()

    main_screen()
    

#Clear button functionality
def clear():
    codeeditor.content = " "
    playground_editor = " "
   
#This is used for showing code and for the playground
def code_editor():
    global codeeditor
    global run_button
   
    #initialize the code editor.
    codeeditor = tkcode.CodeEditor(panedwin,language="python",height=5,font=("Arial",15))
    codeeditor.grid(row=2,column=1,ipady=3)
    #Add the run button
    run_button = ttk.Button(codeeditor, text="Run",style="codeeditorrun.TButton",command=lambda: output(1))
    run_button.place(relheight=0.3,relwidth=0.2,relx=0.8)
    #Add Clear button
    clear_button = ttk.Button(codeeditor, text="Clear",style="codeeditorclear.TButton",command=clear)
    clear_button.place(rely=0.5,relheight=0.5,relwidth=0.2,relx=0.8)






  
#This will serve as the page index for changing the pages on 'learn' function.
page = 1
def change_page(t):
    #Acces page var
    global page
    
    print(page)
    #Increment/decrement page variable each time the button are pressed
    if t == 1:
        page += 1
    elif t == -1 and page >= 1:
        page -= 1   

    #If the page index reaches 12 or more, reset to 1
    if page > 10:
        page = 0
        codeeditor.master.grid_remove() #Hide thy editor.

    

    if page == 0:
        maincontent.set(content1)
    elif page == 1:
        maincontent.set(content2)
    elif page == 2:
        maincontent.set(content3)
        codeeditor.content = ""
        codeeditor.master.grid_remove()
    elif page == 3:
        maincontent.set(content4)
        #here we will enable our code editor to show the example code.
        codeeditor.master.grid(column=1,row=2)
        #Set the built in code for this content.
        codeeditor.content = "print(\"hello world\")"
    elif page == 4:
        maincontent.set(content5)
        #We will need to enabled code editor in here again
        codeeditor.master.grid(column=1,row=2)
        #set the built in code.
        codeeditor.content = """
ask = input(" What's your name? ")
print(ask)"""

    elif page == 5:
        #WE dont need code editor anymore so hide it.
        codeeditor.master.grid_remove()
        maincontent.set(content6)
    elif page == 6:
        codeeditor.master.grid(column=1,row=2)
        maincontent.set(content7)
        #set the built in code for this content.
        codeeditor.content = """
#Data types
box1 = 10 #This box contains a number(Int)                                                               
box2 = "Hello world!" #This one is a text(String). remember to always surround it on a Double quotation. 
box3 = 0.5 #this one is a decimal(float/double)                                                          
box4 = True #This one is a boolean. it can only contain True or False      
"""
    elif page == 7:
        maincontent.set(content8)
        codeeditor.content = """

box1 = 10 #This box contains a number(Int)                                                               
box2 = "Hello world!" #This one is a text(String). remember to always surround it on a Double quotation. 
box3 = 0.5 #this one is a decimal(float/double)                                                          
box4 = True #This one is a boolean. it can only contain True or False  
#print values
print(box1) #Outputs 10                
print(box2) #Outputs "Hello world!"    
print(box3) #Outputs 0.5               
print(box4) #Outputs True 
""" 
    elif page == 8:
        maincontent.set(content9)
        codeeditor.content = """
# + -> addition
add = 1 + 1 #outputs 2
# - -> subtraction
sub = 5 - 1 #Outputs 4
# * -> multiplication
mult = 5 * 5 #outputs 25
# / -> division
div = 25 / 5 #outputs 5
# // -> floor division
floor_div = 5 // 2 # 2  
# % -> modulus
modulus = 10 % 3 # 1
# ** -> exponent
expont = 5 ** 2 # 25   
"""
    elif page == 9:
        maincontent.set("Here's an example of arithmetic in python:")
        codeeditor.content = """
add = 1 + 1 #outputs 2
sub = 5 - 1 #Outputs 4
mult = 5 * 5 #outputs 25
div = 25 / 5 #outputs 5
floor_div = 5 // 2 # 2
modulus = 10 % 3 # 1
expont = 5 ** 2 # 25

print(add)
print(sub)
print(mult)
print(div)
print(floor_div)
print(modulus)
print(expont)

"""
    elif page == 10:
        maincontent.set(content10)
        codeeditor.content = """
# equal to ==
if 5 == 5:
    print("5 is equal to 5")
# not equal to !=
if 5 != 6:
    print("5 is not equal to 6")
# greater than >
if 5 > 2:
    print("5 is greater than 2")
# less than <
if 5 < 10:
    print("5 is less than 10")
# greater than or equal to >=
if 5 >= 5:
    print("5 is greater than or equal to 5")
# less than or equal to <=
if 5 <= 10:
    print("5 is less than or equal to 10")
"""
    elif page == 11:
        maincontent.set("Here's an example of relational operator in python:")
        codeeditor.content = """

variable = 10

if variable == 10:
    print("it's ten")

if variable != 12:
    print("It's not equal to 12")

if variable > 25:
    print("Its greater than 25")

if variable < 25:
    print("Its less than 25")

if variable >= 25:
    print("Its greater than or equal to 25")

if variable <= 25:
    print("Its less than or equal to 25")


"""



def main_screen():
    #Create the main frame to put the widgets.
    global frame
    frame = ttk.Frame(root,padding=5)

    frame.grid(column=0, row=0, sticky='nsew')

    frame.columnconfigure(1,weight=1,pad=50)

    #Add a text widget inside the frame.
    text = ttk.Label(frame,text="Pytutorial",style="main.TLabel")
    text.grid(column=1, row=1, sticky="n",pady=100)

    #Add the buttons
    btn1 = ttk.Button(frame,text="Learn python",style="main.TButton",command=learn)
    btn1.grid(column=1,row=2,pady=80)

    btn2 = ttk.Button(frame,text="Playground",style="main.TButton",command=playground)
    btn2.grid(column=1,row=3)


main_screen()
root.mainloop()