# Imports
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from idlelib.colorizer import ColorDelegator
from idlelib.percolator import Percolator

# Defining how to create a new file
def new_file():
    if text_area.get(1.0, tk.END) != '\n':
        if messagebox.askokcancel("Save", "Do you want to save the current file?"):
            save_file()
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Text Editor")

# Defining how to open an existing file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"{file_path} - Text Editor")

# Defining how to save a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_path} - Text Editor")

# Defining a confirmation message to quit the program
def exit_editor():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

# Defining the word count calculation
def word_count():
    text = text_area.get(1.0, tk.END)
    words = len(text.split())
    messagebox.showinfo("Word Count", f"Words: {words}")

# Initializing the main window
root = tk.Tk()
root.title("Untitled - Text Editor")
root.geometry("800x600")

# Creating a text widget with a scroll bar
text_area = ScrolledText(root, undo=True, wrap=tk.WORD)
text_area.pack(expand=True, fill='both')

# Adding syntax highlighting
Percolator(text_area).insertfilter(ColorDelegator())

# Creating a menu bar
menu_bar = tk.Menu(root)

# Adding File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)

# Adding Tools menu
tools_menu = tk.Menu(menu_bar, tearoff=0)
tools_menu.add_command(label="Word Count", command=word_count)
menu_bar.add_cascade(label="Tools", menu=tools_menu)

# Configuring the menu bar
root.config(menu=menu_bar)

# Running the application
root.mainloop()