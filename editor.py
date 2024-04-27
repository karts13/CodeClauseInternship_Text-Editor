from tkinter import *
from tkinter import filedialog

def new_file():
    text_info.delete(1.0, END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            text_info.delete(1.0, END)
            text_info.insert(1.0, text)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            text_content = text_info.get(1.0, END)
            file.write(text_content)

def cut_text():
    text_info.event_generate("<<Cut>>")

def copy_text():
    text_info.event_generate("<<Copy>>")

def paste_text():
    text_info.event_generate("<<Paste>>")

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
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

text_info = Text(root) 
text_info.pack(fill=BOTH, expand=True) 

root.mainloop()