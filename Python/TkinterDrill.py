from tkinter import *

win=Tk()

b1 = Button(win,text="One")
b2 = Button(win,text="Two")
b3 = Button(win,text="THREE")
b4 = Button(win,text="FOUR")

b1.pack(side=LEFT,padx=10)
b2.pack(side=LEFT,padx=10)
b4.pack(side=BOTTOM,pady=10)
b3.pack(side=RIGHT,padx=10)


win2 = Tk()
b5 = Button(win2,text="One")
b6 = Button(win2,text="Two")
b5.grid(row=0, column=0)
b6.grid(row=1, column=1)

l = Label(win2, text="This is a label")
l.grid(row=1,column=0)

win3 = Tk()
f = Frame(win3)
b7 = Button(f, "One")
b8 = Button(f, "Two")
b9 = Button(f, "Three")
b7.pack(side=LEFT)
b8.pack(side=LEFT)
b9.pack(side=LEFT)
m = Label(win3,"This label is over all buttons")
m.pack()
f.pack()

b7.configure(text="Uno")

def but7() : print ("Button one was pushed")
b7.configure(command=but7)

win.mainloop()
win2.mainloop()
win3.mainloop()