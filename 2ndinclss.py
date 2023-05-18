#import the tkinkter library
import tkinter as tk 
from tkinter import ttk

#declare a function for the event of choosing an item from the widget. 
def on_select(event):

    #Create an item object that obtains the value of the selected item. 
    selected_item = event.widget.get()
    print("Selected item:", selected_item)

#create the root window object 
root = tk.Tk()
root.title("Nafiva thee developer")

#create the array of choices 
choices = [" Choice 1 ", " Choice 2 ", " Choice 3 ", " Choice 4 "]

#create the combo box object
combo_box = ttk.Combobox(root, values=choices)

combo_box.bind("<<ComboboxSelected>>", on_select)
#Pack the object to the screen with the Geometry manager. 
combo_box.pack()

#mainloop keeps the root parent window visible.
root.mainloop()
