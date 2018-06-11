from tkinter import Tk, PhotoImage, Frame, Button, TOP
from tkinter.ttk import Notebook

root = Tk()
scheduledimage=PhotoImage(...)
note = Notebook(root)

tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
Button(tab1, text='Exit', command=root.destroy).pack(padx=100, pady=100)

note.add(tab1, text = "Tab One")
note.add(tab2, text = "Tab Two")
note.add(tab3, text = "Tab Three")
note.pack()
root.mainloop()
exit()