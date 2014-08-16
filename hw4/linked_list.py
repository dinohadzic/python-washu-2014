class Node:
	def __init__(self, _value = None, _next = None):
		self.value = _value
		self.next = _next
	def __str__(self):
		return str(self.value)

class LinkedList:
	def __init__(self, value):	
		self.size = 1
		self.head = Node(value)		
		
	def length(self):	
		return "Length of list is %d" % self.size
	
	def addNode(self, new_value):	
		self.size += 1
		hold = self.head
		new_value = Node(new_value)	
		while hold.next is not None: hold = hold.next	
		hold.next = new_value	

	def addNodeAfter(self, new_value, after_node):	
		self.size += 1
		hold = self.head
		while str(hold) is not str(after_node):	
			hold = hold.next 
		hold.next = Node(new_value, hold.next) 

	def addNodeBefore(self, new_node, before_node):	
		self.size += 1
		hold = self.head	
		hold2 = hold	
		while str(hold) is not str(before_node): 
			hold2 = hold
			hold = hold.next
		if hold is self.head:	
			self.head = Node(new_node, hold2)
			self.size += 1
			return self.head
		hold2.next = Node(new_node, hold2.next)	

	def removeNode(self, node_to_remove):
		self.size -= 1
		hold = self.head
		if str(hold) is str(node_to_remove):
			self.size -= 1	
			hold = Node(hold.next, hold.next.next)	
			return self.head
		while str(hold.next) != str(node_to_remove):	
			hold = hold.next
		hold.next = hold.next.next	
	
	def removeNodesByValue(self, value):	
		hold = self.head
		if str(value) is str(hold):	
			self.head = Node(hold.next, hold.next.next)	
			self.size -= 1	
		while str(hold.next) != str(value):	
			if hold.next is None:	
				return "Removing node would empty list."
			hold = hold.next 
		hold.next = hold.next.next
		self.removeNodesByValue(value)
		self.size -= 1	
		
	def reverse(self):	
		tempVar = self.head	
		hold = Node(self.head)		
		while tempVar.next is not None:	
			tempVar = tempVar.next	
			hold = Node(tempVar, hold)
		self.head = hold	
		return hold
		
	def __str__(self):	
		hold = self.head
		output = "LinkedList - "
		output += str(hold)	
		while hold.next is not None:
			output += ", " + str(hold.next)
			hold = hold.next
		return output

# Note: all the methods are of complexity 0(n) with the exception of removeNodesByValue(),
# whose complexity I am unsure of. The functions pass the bottom tests.


linked_list = LinkedList(5) # Creates list with 5 as the only value.
print(linked_list) # Displays list of just value 5.
print linked_list.length() # Length of list is 1.

linked_list.addNode(7) # Adds 7 after 5.
linked_list.addNode(60) # Adds 60 after 7.
print(linked_list) # Displays appropriate list: 5, 7, 60
print linked_list.length() # Appropriate length: 3.

linked_list.addNodeAfter(10, 5) # Adds 10 after 5.
linked_list.addNodeAfter(5, 7) # Adds 5 after 7.
print(linked_list) # Displays appropriate list: 5, 10, 7, 5, 60
print linked_list.length() # Appropriate length: 5

linked_list.addNodeBefore(20, 7) # Adds 20 before 7.
print(linked_list) # Displays appropriate list: 5, 10, 20, 7, 5, 60
print linked_list.length() # Appropriate length: 7

linked_list.removeNode(60) # Removes 60.
print(linked_list) # Displays appropriate list: 5, 10, 20, 7, 5
print linked_list.length() # Appropriate length: 5

linked_list.removeNodesByValue(5) # Removes all nodes containing value 5.
print(linked_list) # Displays appropriate list: 10, 20, 7
print linked_list.length() # Appropriate length: 3

linked_list.reverse() # Reverses order of list.
print(linked_list) # Displays appropriate list: 7, 20, 10
print linked_list.length() # Appropriate length: 3










