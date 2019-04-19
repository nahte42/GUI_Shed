from tkinter import *
from employee import *

def creatMenu(window):
	myMenNew = Menu(window)
	myMenNew.add_command(label = "New")
	myMenNew.add_command(label = "Save")
	myMenNew.add_command(label = "Exit", command = exit)
	window.add_cascade(label = "File", menu = myMenNew)
	
def addEmployee():
	employeeFile = open('employees.txt', 'w')
	gnuEmployee = Employee(nameEntry.get(), prefEntry.get(), avaiEntry.get())
	nameEntry.delete(0,END)
	avaiEntry.delete(0,END)
	prefEntry.delete(0,END)
	myEmpList.append(gnuEmployee)
	for x in myEmpList:
		employeeFile.write(x.getName())
		employeeFile.write(x.getPref())
		employeeFile.write(x.getAvai())
		employeeFile.write("\n")
	
	employeeFile.close()
	
	
def startUp():
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

employeeFile = open('employees.txt', 'r')	
startUp()	
employeeFile.close()	

root = Tk()

myMen = Menu (root)
creatMenu(myMen)


label1 = Label(root, text ="Employee Name")
label2 = Label(root, text = "Availability")
label3 = Label(root, text = "Prefhours   ")

nameEntry = Entry(root, bd = 5)
avaiEntry = Entry(root, bd = 5)
prefEntry = Entry(root, bd = 5)

nameEntry.place(x = 100, y = 0)
avaiEntry.place(x = 100, y = 40)
prefEntry.place(x = 100, y = 80)

label1.place(x=0, y=0)
label2.place(x=0, y = 40)
label3.place(x=0, y = 80)

myBut = Button(root, text = "Add Employee", command = addEmployee)
myBut.place(x = 0, y = 120)




root.config(menu = myMen)
root.geometry("500x200")
root.mainloop()



