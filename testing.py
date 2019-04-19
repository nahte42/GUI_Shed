from tkinter import *
from employee import *

def creatMenu(window):
	myMenNew = Menu(window)
	myMenNew.add_command(label = "New")
	myMenNew.add_command(label = "Save")
	myMenNew.add_command(label = "Exit", command = exit)
	window.add_cascade(label = "File", menu = myMenNew)

def createButtons(window):
	cEmployee = Button(window, text = "Add Employee", command = createTopLevel)
	cSchedule = Button(window, text = "Create Schedule", command = createTopLevel)
	cAvailabl = Button(window, text = "Update Availability", command = createTopLevel)


	cEmployee.place(bordermode = OUTSIDE, width = 100, height = 50)
	cSchedule.place(width = 100, height = 50, y = 55)
	cAvailabl.place(width = 100, height = 50, y = 110)

def createTopLevel():
	newTop = Toplevel()
	gnuMenu = Menu(newTop)
	creatMenu(gnuMenu)
	newTop.config(menu = gnuMenu)
	#createButtons(newTop)
	newTop.mainloop()

root = Tk()

myMen = Menu (root)
creatMenu(myMen)
createButtons(root)


root.config(menu = myMen)
root.mainloop()



