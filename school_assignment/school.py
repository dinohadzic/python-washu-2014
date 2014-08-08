class School():
	def __init__(self, school_name):
		self.school_name = school_name
		self.db = {}
		
	def add(self, name, grade):
		if grade in self.db:
			self.db[grade].add(name)	# If grade already exists, adds name to the grade.
		else: self.db[grade] = {name}	# If grade does not exist, creates the grade 
											#and adds name to it.
	
	def sort(self):
		sorted_students = {}
		for i in self.db.keys():
			sorted_students[i] = tuple(sorted(self.db[i])) 
		return sorted_students	# Loops through the keys of db (grade), and creates 
									#entries in sorted_students, where the grade is the 
									#key, and the tuple of students (now sorted 
									#alphabetically) are the values.							
			
	def grade(self, grade):
		if grade in self.db: 
			return self.db[grade]
		else: return None	# If the grade exists, returns names of the students 
								#in that grade. If the grade doesn't exist, 
								#returns "None."
		