from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def quit_app():
    root.quit()

def show_about(event=None):
    messagebox.showwarning(
        "About",
        "Made in 2019"
    )

root = Tk()

the_menu = Menu(root)

file_menu = Menu(the_menu, tearoff=0)

file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()

file_menu.add_command(label="Quit", command=quit_app)

the_menu.add_cascade(label="File", menu=file_menu)

# ---- View menu -----

view_menu = Menu(the_menu, tearoff=0)

# Variable changes when line numbers is checked
# or unchecked
line_numbers = IntVar()
line_numbers.set(1)

# Bind the checking of the line number option
# to variable line_numbers
view_menu.add_checkbutton(label="Line Numbers",
                          variable=line_numbers)

view_menu.add_cascade(label="Fonts", menu=font_menu)

the_menu.add_cascade(lael="View")

root.config(menu=the_menu)

root.mainloop()