#Imports to be used#
from tkinter import *
from employee import *
#from PyPDF2 import PdfFileWriter, PdfFileReader

#Main body, creates main window and buttons	
root = Tk()
canvaswidth = 500
canvasheight= 500
y = 20
x2 = 500
C = Canvas(root, width = canvaswidth, height = canvasheight)
C.grid(row = 0)

x = 0
while x != 10:
	C.create_line(0, y, x2, y, width = 2.5)
	y = y + 20
	x = x + 1

mainMenu = Menu (root)

root.geometry("500x500")
root.mainloop()
	
