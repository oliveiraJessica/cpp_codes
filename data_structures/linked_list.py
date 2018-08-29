class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

	def get_data(self):
		return self.data

	def set_next(self, node):
		self.next = node

	def get_next(self):
		return self.next

class List:

	def __init__(self, node):
		self.head = node
		self.tail = self.get_head()

	def get_head(self):
		return self.head
	
	def set_head(self, node):
		self.head = node

	def get_tail(self):
		return self.tail

	def set_tail(self, node):
		self.tail = node

	def append(self, node):
		self.get_tail().set_next(node)
		self.set_tail(node)

	def remove(self, node):
		n = self.get_head()
		if n.get_data() == node.get_data():
			self.set_head(n.get_next())
		else:
			while n.get_next() != None:
				if n.get_next().get_data() == node.get_data():
					if n.get_next().get_next() == None:
						self.set_tail(n)
					else:
						n.set_next(n.get_next().get_next())
				n = n.get_next()

			
