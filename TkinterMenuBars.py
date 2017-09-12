
# Exercise
# Menu Bars 


from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# to quit an application use this defining
def quit_app():
    root.quit()

def show_about(event=None):
    messagebox.showwarning(
        "About",
        "Welcome to Menu Bar Exercise 2017"
    )


root = Tk()


the_menu = Menu(root)

# Adding the -----File Menu------
# tearoff should always be on 0. OS's don't use this as much.
file_menu = Menu(the_menu, tearoff=0)

file_menu.add_command(label="Open")

file_menu.add_command(label="Save")
# adds a line that separates alternatives
file_menu.add_separator()

file_menu.add_command(label="Quit", command=quit_app)
# Add pulldown menu title (File) to menu bar
the_menu.add_cascade(label="File", menu=file_menu)
# ------Font Menu (inside View Menu)------

text_font = StringVar()
text_font.set("Times")


def change_font(event=None):
    print("Font Picked: ", text_font.get())


font_menu = Menu(the_menu, tearoff=0)

font_menu.add_radiobutton(label="Times",
                          variable=text_font,
                          command=change_font)

font_menu.add_radiobutton(label="Courier",
                          variable=text_font,
                          command=change_font)

font_menu.add_radiobutton(label="Ariel",
                          variable=text_font,
                          command=change_font)


# ----- VIEW MENU -----
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

# Add the pull down menu to the menu bar
the_menu.add_cascade(label="View", menu=view_menu)
# ----------Help Menu----------

help_menu = Menu(the_menu, tearoff=0)
# Command-H works on Windows, OSX, Linux.
# In others: Command-O, Shift+Ctrl+S etc.
help_menu.add_command(label="About",
                      accelerator="Command-H",
                      command=show_about)
the_menu.add_cascade(label="Help", menu=help_menu)
# binds or shortcuts to little keys
root.bind('<Command-A>', show_about)
root.bind('<Command-a>', show_about)

# To make the menu bar show on screen
root.config(menu=the_menu)

root.mainloop()
