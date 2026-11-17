#This is the version 2 of the program. this time, it has UI using tkinter. we will add some editor, quiz, and a lot of things in here.

import tkinter
import tkcode
from tkinter import ttk


#Initialize the window 
root = tkinter.Tk()
root.geometry("1280x900")

#set the root screen
root.columnconfigure(0,weight=2)
root.rowconfigure(0,weight=1)
frame = ttk.Frame(root,padding=5)

#style
style = ttk.Style()
style.theme_use("clam")

#For textx
style.configure(
    "main.TLabel",
    font=("Arial",50),
    foreground = "#ffffff",
    background = "#706000"
)

style.configure(
    "learn.TLabel",
    font=("Arial", 15)
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
    "codeeditor.TButton",
    background="red",
    foreground="white"
)

style.map(
    "main.TButton",
    foreground = [('active','pink'),('pressed', 'red'),('!active', 'white')],
    background = [('active', 'darkblue'),('pressed', 'red')]
)

style.map(
    "codeeditor.TButton",
    background = [('active','darkred')]
)





#This is where the topic(intro to program, syntax..etc) goes. we will make it in one function inorder to easily manage it.
def learn():
    #Access the topic variable and make maincontent global for change_topic function a
    global topic
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

"""
    #make the content variables global 
    global content1
    global content2
    global content3
    global content4
    global panedwin
    #Split the raw strings into content parts
    content1 = rawstring[0:760] 
    content2 = rawstring[760:1105]
    content3 = rawstring[1097:1496]
    content4 = rawstring[1495:1800]
    print(content4)
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

    next = ttk.Button(panedwin, text="Next",command=lambda: change_topic(1)).grid(column=2,row=2,padx=5,pady=7)
    prev = ttk.Button(panedwin, text="Previous", command=lambda: change_topic(-1)).grid(column=0,row=2,padx=5,pady=10)


    #Insert the panedwin on the frame.
    panedwin.insert()


#This is used for showing code and for the playground
def code_editor(enable):
    if enable == True:
        #initialize the code editor.
       global codeeditor
       codeeditor = tkcode.CodeEditor(panedwin,language="python",height=5)
       codeeditor.grid(row=1,column=1,ipady=3)
       #Add the run button
       run_button = ttk.Button(panedwin, text="Run",style="codeeditor.TButton",command=output)
       run_button.grid(row=1,column=2)
    elif enable == False:
        #Destroy it if not enabled
        codeeditor.destroy()

#This is the output function to show the output of the code from the codeeditor.
def output():
    print(codeeditor.content)
#This will serve as the topic index for changing the topics on 'learn' function.
topic = 0

def change_topic(t):
    #Acces topic var
    global topic
    print(topic)
    if t == 1:
        topic += 1
    elif t == -1 and topic >= 1:
        topic -= 1

    if topic == 0:
        maincontent.set(content1)
    elif topic == 1:
        maincontent.set(content2)
    elif topic == 2:
        maincontent.set(content3)
        code_editor(False)
    elif topic == 3:
        maincontent.set(content4)
        #here we will show an entry to act as a code editor
        code_editor(True)
        #Set the built in code for this content.
        codeeditor.content = "print(\"hello world\")"



    
def main_screen():
    #Create the main frame to put the widgets.
    
    frame.grid(column=0, row=0, sticky='nsew')

    frame.columnconfigure(1,weight=1,pad=50)

    #Add a text widget inside the frame.
    text = ttk.Label(frame,text="Pytutorial",style="main.TLabel")
    text.grid(column=1, row=1, sticky="n",pady=100)

    #Add the buttons
    btn1 = ttk.Button(frame,text="Learn python",style="main.TButton",command=learn)
    btn1.grid(column=1,row=2,pady=80)

    btn2 = ttk.Button(frame,text="Playground",style="main.TButton")
    btn2.grid(column=1,row=3)





main_screen()
root.mainloop()