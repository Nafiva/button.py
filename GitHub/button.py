#import the  tkinter class library and rename the class library 
import tkinter as tk

#declare the function for the button click
def button_click():
    print("Button clicked!")

#create the root window 
root = tk.Tk()
root.title("Button Example")

#create the button object, with 3 arguments 
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

#call the main root window, so the window stays open 
root.mainloop()
            