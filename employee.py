class Employee:
	name = ""
	prefHours = ""
	availability = ""
	
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

	
employeeFile = open('employees.txt', 'r')	
#test = employeeFile.readline()
#print(test)


myEmpList = []


#create the array of employee objects from a file
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

employeeFile = open('employees.txt', 'w')


#write array of employees to file
for x in myEmpList:
	employeeFile.write(x.getName())
	employeeFile.write(x.getPref())
	employeeFile.write(x.getAvai())
	employeeFile.write("\n")
	
employeeFile.close()