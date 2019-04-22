#Imports to be used
from tkinter import *
from employee import *

#This functions creates menus for whatever window was passed to it
def creatMenu(window):
	myMenNew = Menu(window)
	myMenNew.add_command(label = "New")
	myMenNew.add_command(label = "Save")
	myMenNew.add_command(label = "Exit", command = exit)
	window.add_cascade(label = "File", menu = myMenNew)

#This function creates the buttons for the main window
def createButtons(window):
	cEmployee = Button(window, text = "Add Employee", command = addEmployeeWindow)
	cSchedule = Button(window, text = "Create Schedule", command = createTopLevel)
	cAvailabl = Button(window, text = "Update Availability", command = createTopLevel)


	cEmployee.place(bordermode = OUTSIDE, width = 100, height = 50)
	cSchedule.place(width = 100, height = 50, y = 55)
	cAvailabl.place(width = 100, height = 50, y = 110)
	
	
#This function will create a new window with a menu
def createTopLevel():
	newTop = Toplevel()
	gnuMenu = Menu(newTop)
	creatMenu(gnuMenu)
	newTop.config(menu = gnuMenu)
	#createButtons(newTop)
	newTop.mainloop()

#This is used to create the add employee function and window
def addEmployee(nameEntry, prefEntry, M, T, W, R, F, S, U, avaiM, avaiT, avaiW, avaiR, avaiF, avaiS, avaiU):
	avail = ""
	if avaiM.get() == 1:
		avail =  avail + "M"
	if avaiT.get() == 1:
		avail =  avail + "T"
	if avaiW.get() == 1:
		avail =  avail + "W"
	if avaiR.get() == 1:
		avail =  avail + "R"
	if avaiF.get() == 1:
		avail =  avail + "F"
	if avaiS.get() == 1:
		avail =  avail + "S"
	if avaiU.get() == 1:
		avail =  avail + "U"
		
	employeeFile = open('employees.txt', 'a')
	gnuEmployee = Employee(nameEntry.get(), prefEntry.get(), avail)
	myEmpList.append(gnuEmployee)
	nameEntry.delete(0,END)
	prefEntry.delete(0,END)
	M.deselect() 
	T.deselect() 
	W.deselect()
	R.deselect()
	F.deselect()
	
	employeeFile.write(gnuEmployee.getName())
	employeeFile.write(gnuEmployee.getPref())
	employeeFile.write(avail)
	employeeFile.write("\n")
	
	employeeFile.close()
	
	
	
	
def addEmployeeWindow():
	avaiM = IntVar()
	avaiT = IntVar()
	avaiW = IntVar()
	avaiR = IntVar()
	avaiF = IntVar()
	avaiS = IntVar()
	avaiU = IntVar()
	
	
	newTop = Toplevel()
	
	label1 = Label(newTop, text ="Employee Name")
	label2 = Label(newTop, text = "Availability")
	label3 = Label(newTop, text = "Prefhours   ")
	
	M = Checkbutton(newTop, text = "Mon",  variable = avaiM, onvalue = 1, offvalue = 0)
	T = Checkbutton(newTop, text = "Tue",  variable = avaiT, onvalue = 1, offvalue = 0)
	W = Checkbutton(newTop, text = "Wed",  variable = avaiW, onvalue = 1, offvalue = 0)
	R = Checkbutton(newTop, text = "Thur", variable = avaiR, onvalue = 1, offvalue = 0)
	F = Checkbutton(newTop, text = "Fri",  variable = avaiF, onvalue = 1, offvalue = 0)
	S = Checkbutton(newTop, text = "Sat",  variable = avaiS, onvalue = 1, offvalue = 0)
	U = Checkbutton(newTop, text = "Sun",  variable = avaiU, onvalue = 1, offvalue = 0)
	S.select()
	U.select()
	
	
	M.place(x = 90, y = 80)
	T.place(x = 90, y = 100)
	W.place(x = 90, y = 120)
	R.place(x = 90, y = 140)
	F.place(x = 90, y = 160)
	S.place(x = 90, y = 180)
	U.place(x = 90, y = 200)
	
	nameEntry = Entry(newTop, bd = 5)
	avaiEntry = Entry(newTop, bd = 5)
	prefEntry = Entry(newTop, bd = 5)


	nameEntry.place(x = 100, y = 0)
	#avaiEntry.place(x = 100, y = 80)
	prefEntry.place(x = 100, y = 40)

	label1.place(x=0, y=0)
	label2.place(x=0, y = 80)
	label3.place(x=0, y = 40)
	

	myBut = Button(newTop, text = "Add Employee", command =lambda: addEmployee(nameEntry, prefEntry, M, T, W, R, F, S, U, avaiM, avaiT, avaiW, avaiR, avaiF, avaiS, avaiU))
	myBut.place(x = 0, y = 120)
	
	
	gnuMenu = Menu(newTop)
	creatMenu(gnuMenu)
	newTop.config(menu = gnuMenu)
	newTop.geometry("500x300")
	newTop.mainloop()



def startUp():
	employeeFile = open('employees.txt', 'r')	
	for line in employeeFile:
		name = ""
		prefH = ""
		avail = ""
		i = 0
		while i < len(line):
			if line[i].isdigit():
				prefH += line[i]
			elif line[i].isupper() and i > 0:
				avail += line[i]
			elif line[i] == "\n":
				nope = ""
			else:
				name += line[i]
			i = i + 1
		
		myEmpList.append(createEmployee(name, prefH, avail))
	employeeFile.close()
		


startUp()

	
	
	
	
#Main body, creates main window and buttons	
root = Tk()

mainMenu = Menu (root)
creatMenu(mainMenu)
createButtons(root)


root.config(menu = mainMenu)
root.geometry("500x300")
root.mainloop()
	
