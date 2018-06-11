from tkinter import *


def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    # Deletes the contents once "Show" is clicked
    e1.delete(0, END)
    e2.delete(0, END)


master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

# Provide default values
e1.insert(10, "Miller")
e2.insert(10, "Jill")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Add buttons to Quit or Show the contents
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop()

