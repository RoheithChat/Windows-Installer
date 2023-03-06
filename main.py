from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import os

# Create a Tkinter root window
root = Tk()

# Set the title of the window
root.title("WineGui")

# Create a style object
style = ttk.Style()

# Set the background color for the buttons
style.configure('TButton', background='#4CAF50')
style.map('TButton', background=[('active', '#2196F3')])  # Update active color to blue


# Create a function to browse for a file
def browse_file():
    # Open a file dialog window
    file_path = filedialog.askopenfilename()
    # Show the path to the selected file
    file_path_text.set(file_path)


# Create a label for the file path
file_path_label = Label(root, text="File Path: ")
file_path_label.grid(row=0, column=0)

# Create a text box for the file path
file_path_text = StringVar()
file_path_entry = Entry(root, textvariable=file_path_text, width=50)
file_path_entry.grid(row=0, column=1)

# Create a browse button to open the file dialog
browse_button = ttk.Button(root, text="Browse", style='TButton', command=browse_file)
browse_button.grid(row=0, column=2)


def install():
    os.system("wine " + '"' + file_path_text.get() + '"')


# Create an install button
install_button = ttk.Button(root, text="Install", style='TButton', command=install)
install_button.grid(row=1, column=1)

# Show the window
root.mainloop()
