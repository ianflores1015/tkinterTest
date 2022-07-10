from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Simple Calculator")

content = ttk.Frame(root)

input = ttk.Entry(content, width=50)
test_button1 = Button(content, text="test1", width=20)
test_button2 = Button(content, text="test2", width=20)

content.grid(column=0, row=0)
input.grid(column=0, row=0, columnspan=2)
test_button1.grid(column=0, row=1)
test_button2.grid(column=1, row=1)


root.mainloop()
