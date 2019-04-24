#Imports to be used#
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
	
