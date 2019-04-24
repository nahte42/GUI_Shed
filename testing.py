#Imports to be used#
from tkinter import *
from employee import *


#Main body, creates main window and buttons	
root = Tk()

C = Canvas(root)
C.create_line(0,20,300,20)
C.grid(row = 0)

mainMenu = Menu (root)

root.geometry("500x500")
root.mainloop()
	
