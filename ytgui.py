#https://www.tutorialspoint.com/python/python_gui_programming.htm
from tkinter import *
def donothing():
	print("test")

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
	
var = 0
	
root = Tk()

myBut = Button(root, activebackground = 'black')
myBut.pack()

myChk = Checkbutton(root)
myChk.pack()

myEnt =  Entry(root)
myEnt.pack()

myFra = Frame(root, cursor = 'dot')
myFra.pack()

var = "Biatch"
myLab = Label(root, text = var, relief = RAISED, padx = 15)
myLab.pack()

myLis = Listbox(root, height = 4)
myLis.insert(1, "Bitch")
myLis.pack()

myMeb = Menubutton(root, text = "Bizitch")
myMeb.pack()

myMen = Menu (root)
myMenNew = Menu(myMen)
myMenNew.add_command(label = "New", command = donothing)
myMen.add_cascade(label = "file", menu = myMenNew)

myMes = Message(root, text = "bitch test bitch")
myMes.pack()

myRad1 = Radiobutton(root, text="test1", variable = var, value = 1, command = sel)
myRad2 = Radiobutton(root, text="test2", variable = var, value = 2, command = sel)
myRad1.pack(anchor=W)
myRad2.pack(anchor=W)

mySca = Scale(root, activebackground = 'black')
mySca.pack()

myScr = Scrollbar(root, activebackground = 'black')
myScr.pack()

#myText = Text(root)
#myText.pack()

myTop = Toplevel()

root.config(menu = myMen)
root.mainloop()
myTop.mainloop()

mySpi = Spinbox(root, activebackground = 'black', from_=0, to=10)
mySpi.pack()

myPan = PannedWindow(myTop)
myPan.pack(fill=BOTH, expand=1)
left = Label(myPan, text="left pane")
myPan.add(left)

#LabelFrame
#tkMessageBox

