from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import os


root = Tk()

root.title("WineGui")


style = ttk.Style()


style.configure('TButton', background='#4CAF50')
style.map('TButton', background=[('active', '#2196F3')])  # Update active color to blue



def browse_file():
    
    file_path = filedialog.askopenfilename()
    
    file_path_text.set(file_path)


file_path_label = Label(root, text="File Path: ")
file_path_label.grid(row=0, column=0)


file_path_text = StringVar()
file_path_entry = Entry(root, textvariable=file_path_text, width=50)
file_path_entry.grid(row=0, column=1)

browse_button = ttk.Button(root, text="Browse", style='TButton', command=browse_file)
browse_button.grid(row=0, column=2)


def install():
    os.system("wine " + '"' + file_path_text.get() + '"')


install_button = ttk.Button(root, text="Install", style='TButton', command=install)
install_button.grid(row=1, column=1)

root.mainloop()
