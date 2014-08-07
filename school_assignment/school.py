class School():
	def __init__(self, school_name):
		self.school_name = school_name
		self.db = {}
		
	def add(self, name, grade):
		if grade in self.db:
			self.db[grade].add(name)
		else: self.db[grade] = {name}
		
	def sort(self):
		sorted_students = {}
		for i in self.db.keys():
			sorted_students[i] = tuple(sorted(self.db[i]))
		return sorted_students
			
	def grade(self, grade):
		if grade in self.db: 
			return self.db[grade]
		else: return None
		