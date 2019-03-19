from tkinter import*
from tkinter import ttk

def get_sum(event):

    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())

    sum = num1+num2
    sumEntry.delete(0, "end")
    sumEntry.insert(0, sum)

#Root = Main window (doesn't have to be called root)
root = Tk()

#Can't add grid to entry stores.
num1Entry = Entry(root)
#Position must be added after
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

#Can't add grid to entry stores.
num2Entry = Entry(root)
#Position must be added after
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

#Can't add grid to entry stores.
sumEntry = Entry(root)
#Position must be added after
sumEntry.pack(side=LEFT)

#Frame (widget) for framing other widgets
frame = Frame(root)

root.mainloop()

# Label(root, text="Description").grid(row=0, column=0, sticky=W)
# Entry(root, width=50).grid(row=0, column=1)
# Button(root, text="Submit").grid(row=0, column=8)
#
# Label(root, text="Quality").grid(row=1, column=0, sticky=W)
# Radiobutton(root, text="New", value=1).grid(row=2,column=0, sticky=W)
# Radiobutton(root, text="Good", value=2).grid(row=3,column=0, sticky=W)
# Radiobutton(root, text="Poor", value=3).grid(row=4,column=0, sticky=W)
# Radiobutton(root, text="Damaged", value=4).grid(row=5,column=0, sticky=W)
#
# Label(root, text="Benefits").grid(row=1,column=1,sticky=W)
# Checkbutton(root, text="Free Shipping!").grid(row=2,column=1,sticky=W)
# Checkbutton(root, text="Bonus Gift").grid(row=3,column=1,sticky=W)
# root.mainloop()


#N E S W NE SE etc
#
# Label(root, text="First name").grid(row=0, sticky=W, padx=4)
# Entry(root).grid(row=0, column=1, sticky=E, padx=4)
#
# Label(root, text="Last name").grid(row=1, sticky=W, padx=4)
# Entry(root).grid(row=1, column=1, sticky=E, padx=4)
#
# Button(root, text="Submit").grid(row=3)

#Pack is not used often, grid is used more
# # #pack(Position widgets inside window) geometry manager
# # #Pack location - Top Right Bottom Left
# # #Fill direction - X Y Both none
# # label.pack()
# # button.pack()
# frame.pack()
#
# #Keep our root visible window/running


#TkInter variable
# labelText = StringVar()
#
# #Doesn't have to be called label
# label = Label(frame, textvariable=labelText)
# button = Button(frame, text="Click Me")
#
# labelText.set("I am a Label")


# #Name of window
# root.title("First GUI!")
#
# #Button
# ttk.Button(root, text="Hello TkInter").grid()