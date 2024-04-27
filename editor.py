from tkinter import *

root = Tk() 
root.geometry("350x250") 
root.title("Text-Editor") 
root.minsize(height=250, width=350) 
root.maxsize(height=250, width=350) 

# Menu
menu = Menu(root)
root.config(menu=menu)

# File menu
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

text_info = Text(root) 
text_info.pack(fill=BOTH, expand=True) 

root.mainloop()