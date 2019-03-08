# implements a Stack ADT from scratch using LinkedLists as underlying datstructure.
# to see implementation of LinkedList structure see 'LinkedList.py' in this repository
#Functions required: pyStack() Count() Clear() Clone() Contains() Peek() Pop() Push(Object)
# Functions cont. ToString()

import importlib
import pyLinkedList
#importlib.reload(pyLinkedList)
from Node import Node

class pyStack:

	def __init__(self,Linked_List,size,name=None):
		self.Linked_List = Linked_List
		self.size = size
		self.name = name

	def count(self): #returns amount of elements in the stack by accessing the .length() method of the LinkedList class
		return self.Linked_List.length()

	def Push





if __name__ == '__main__':
	Node1 = Node(content = 'This is node 1')
	Node2 = Node(content = 'This is node 2')
	Node4 = Node(content = 'this is node 4 and it will be inserted between 2 and 3')
	Node3 = Node(content = 'This is node 3 and should be the last node')
	LinkedList1 = pyLinkedList.Linked_List(name = 'list1')
	LinkedList1.add(Node1)
	LinkedList1.setHead(Node1)
	LinkedList1.add(Node2)
	LinkedList1.insertAt(Node2,Node4)
	LinkedList1.add(Node3)
	#newstack = pyStack(Linked_List = LinkedList1,size=None)
	#print(newstack.count())