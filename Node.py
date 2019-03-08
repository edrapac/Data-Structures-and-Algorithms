# created seperate node file for portability
class Node:

	def __init__(self, content, next_node = None):
		self.content = content
		self.next_node = next_node

	def setContent(self,content):
		self.content = content

	def getContent(self):
		return self.content

	def setNext(self,next_node):
		self.next_node = next_node

	def getNext(self):
		return self.next_node

	def __repr__(self):       #this is mainly for ease of use so we can just print a node and get its content without having to explicitly call methods
		return self.content
