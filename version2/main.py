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
frame = ttk.Frame(root,padding=5)

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
    #make the content variables global 
    global content1
    global content2
    global content3
    global content4
    global content5
    global panedwin
    #Split the raw strings into content parts
    content1 = rawstring[0:760] 
    content2 = rawstring[760:1105]
    content3 = rawstring[1097:1496]
    content4 = rawstring[1495:1650]
    content5 = rawstring[1652:1900]
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
def output():
    #first we save the python file
    codeeditor.save_to_file("outputfile.py")
    #then we get the file name
    file = "outputfile.py"
    #here we use the subprocess module to communicate with python so that the file will be compiled.
   #output = subprocess.Popen([sys.executable,"-u",file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,stdin=subprocess.PIPE,text=True)
    #output = subprocess.Popen(["cmd", "/k", sys.executable,file])

    logpath = os.path.abspath("log.txt") #The name of the log file to store our program logs
    subprocess.run(f'start /wait "" cmd /c " "python" "outputfile.py" -u > "{logpath}" 2>&1" ',shell=True) #This function will create a window a open cmd to run our python script

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

#Clear button functionality
def clear():
    codeeditor.content = " "
   
#This is used for showing code and for the playground
def code_editor():
    global codeeditor
    global run_button
   
    #initialize the code editor.
    codeeditor = tkcode.CodeEditor(panedwin,language="python",height=5,font=("Arial",20))
    codeeditor.grid(row=2,column=1,ipady=3)
    #Add the run button
    run_button = ttk.Button(codeeditor, text="Run",style="codeeditorrun.TButton",command=output)
    run_button.place(relheight=0.3,relwidth=0.2,relx=0.8)
    #Add Clear button
    clear_button = ttk.Button(codeeditor, text="Clear",style="codeeditorclear.TButton",command=clear)
    clear_button.place(rely=0.5,relheight=0.5,relwidth=0.2,relx=0.8)






  

#This will serve as the page index for changing the pages on 'learn' function.
page = 0

def change_page(t):
    #Acces page var
    global page
    
    print(page)
    if t == 1:
        page += 1
    elif t == -1 and page >= 1:
        page -= 1
     

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
        #set the built in code.
        codeeditor.content = """
ask = input(" What's your name? ")
print(ask)"""



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