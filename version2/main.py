#This is the version 2 of the program. this time, it has UI using tkinter. we will add some editor, quiz, and a lot of things in here.

import tkinter
from tkinter import ttk


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
style.map(
    "main.TButton",
    foreground = [('active','pink'),('pressed', 'red'),('!active', 'white')],
    background = [('active', 'darkblue'),('pressed', 'red')]
)


def learn():
    #Clear the current screen.
    for children in frame.winfo_children():
        children.destroy()

     #The frame for learning section.
    lbtn1 = ttk.Panedwindow(frame,width=500,height=500)
    lbtn1.grid(column=1,row=4,pady=130)
    #The main text widget
    txt = ttk.Label(lbtn1, text="Here i am remembering those memorise again").grid(column=1,row=0)
   
    bt = ttk.Button(lbtn1, text="Next").grid(column=0,row=1,padx=5,pady=7)
    bt = ttk.Button(lbtn1, text="Previous").grid(column=2,row=1,padx=5,pady=10,sticky=("S"))
    lbtn1.insert(1,bt)

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