from tkinter import *

myEmpList = []



class Employee:
	name = ""
	prefHours = ""
	availability = ""
	availTime = {}
	
	def __init__(self, name, prefHours, availability):
		self.name = name
		self.prefHours = prefHours
		self.availability = availability
		
	def getName(self):
		return self.name
	def getAvai(self):
		return self.availability
	def getPref(self):
		return self.prefHours
		
	def	setName(self, name):
		self.name = name
	def	setAvai(self, avail):
		self.availability = avail
	def setPref(self, pref):
		self.prefHours = pref
		

		
def createEmployee(name, pref, avail):
	newEmp = Employee(name, pref, avail)
	return newEmp
	
	

