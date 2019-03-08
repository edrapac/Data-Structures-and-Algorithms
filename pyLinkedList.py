#Implementation of a linkedlist in python. Inlcudes a node class as well. Nodes need to have the following methods, set contents, get contents, get next
#Linked list needs to have add, insert,remove,append (add to end). Also needs to have a set current_node, get current_node, set next, get next, get end 

# Done so far: add, get next, set next, get end, set current, 
# Note, Find first, remove from end are both methods that require nodes to know what is before and after them so they are not suitable for a singley-linked list

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



class Linked_List:
	
	def __init__(self,name, current_node = None, next_node = None, end = None,head = None):
		self.name = name     #we just use this to keep track of the name of the linked list more than anything 
		self.current_node = current_node
		self.next_node = next_node

	def setCurrent_node(self, current_node = None):
		self.current_node = current_node
	
	def getCurrent_node(self):
		return self.current_node

	def setHead(self,head):
		self.head = head

	def add(self, node_to_add):   #adds node to next from current_node, not an insert! Next is always null, essentially an append that preserves order
		if self.current_node == None:
			self.current_node = node_to_add
		self.current_node.next_node = node_to_add # current nodes next node is the one added ie Node1.next_node is now Node2
		self.current_node = node_to_add #current node is advanced to Node2
		self.next_node = None #Node2 is now the last in the list, and thus, it's next node is null 

	def getNext(self): #this advances the current node by one and returns it if you want to do stuff with it
		if self.current_node.next is not None:
			self.current_node = self.current_node.next
			return self.current_node 
		else:
			return None


	def length(self):
		self.current_node = self.head
		counter =1
		while self.current_node.next_node != None:
			counter+=1
			self.current_node =self.current_node.next_node
		return counter

	def setNext(self,next_node): #loads a node n+1 into the list but does not advance the current position pointer
		self.current.setNext(next_node)
		return self.current.next # returns the name of the next node for record keeping purposes

	def getEnd(self): #iterates over a linkd list to find the end element, signified by next being None, will not advance the current or next pointer 
		tempCurrent = self.current_node
		tempNext = tempCurrent.next_node
		while tempCurrent.next_node is not None:
			tempCurrent = tempCurrent.next_node
			tempNext = tempCurrent.next_node
		return tempCurrent


	def insertAt(self,insertion_point,insertion_node): # insertAt will insert a node n+1 from the current node n. Will change current node pointer 
		self.current_node = insertion_point #sets current node to N
		insertion_node.next_node = insertion_point.next_node # sets the next node of node(n+1) as the node that was previously the next node of node N
		insertion_point.next_node = insertion_node # sets node(n+1) as the next node of nodeN
		self.current_node = insertion_node
		return self.current_node


	def getCurrentNode(self):
		return self.current_node

	def getNextNode(self):
		return self.current_node.next_node

	def iterOver(self,starting_point): #starting at a given point, iterate forward until no more nodes 
		self.current_node = starting_point
		while self.current_node is not None:
			print(self.current_node)
			self.current_node = self.current_node.next_node


if __name__ == '__main__':
	Node1 = Node(content = 'This is node 1')
	Node2 = Node(content = 'This is node 2')
	Node4 = Node(content = 'this is node 4 and it will be inserted between 2 and 3')
	Node3 = Node(content = 'This is node 3 and should be the last node')
	LinkedList1 = Linked_List(name = 'list1')
	LinkedList1.add(Node1)
	LinkedList1.add(Node2)
	LinkedList1.insertAt(Node2,Node4)
	LinkedList1.add(Node3)
	#print(LinkedList1.getEnd())
	LinkedList1.iterOver(Node1)
	