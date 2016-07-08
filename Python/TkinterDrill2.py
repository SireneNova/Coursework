from tkinter import *

win4 = Tk()
v = StringVar()
e = Entry(win4,textvariable=v)
e.pack()
v.get()
v.set("this is set from the program")


win5 = Tk()
lb = Listbox(win5, height=3)
lb.pack()
lb.insert(END,"first entry")
lb.insert(END,"second entry")
lb.insert(END,"third entry")
lb.insert(END,"fourth entry")
sb = Scrollbar(win5,orient=VERTICAL)
sb.pack(side=LEFT,fill=Y)
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
lb.curselection()


win4.mainloop()
win5.mainloop()