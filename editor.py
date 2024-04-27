from tkinter import *

root = Tk() 
root.geometry("350x250") 
root.title("Sticky Notes") 
root.minsize(height=250, width=350) 
root.maxsize(height=250, width=350) 

text_info = Text(root) 
text_info.pack(fill=BOTH, expand=True) 

root.mainloop()