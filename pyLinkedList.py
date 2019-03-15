# Implementation of a linkedlist in python.  Inlcudes a node class as well.
# Nodes need to have the following methods, set contents, get contents, get
# next
# Linked list needs to have add, insert,remove,append (add to end).

from Node import Node


class Linked_List:

    def __init__(self, name, end=None, head=None):
        self.name = name  # just for bookkeeping
        self.head = head
        self.end = end

    def append(self, node_to_add):  # adds node to the end of the LinkedList
        current_node = self.head

        while current_node.next_node != None:  # traverses from head until the n-1 node
            current_node = current_node.next_node
        current_node.next_node = node_to_add
        node_to_add.next_node = None

    def find(self, node_to_find):
        try:
            current_node = self.head
            pos = 0
            flag = False
            while current_node:
                if current_node == node_to_find:
                    flag = True
                    return pos
                pos += 1
                current_node = current_node.next_node
            if not (flag):
                return -1
        except Exception as e:
            print('Encountered an exception searching for the specifed value reporting error: ' + e)

    def len(self):
        current_node = self.head
        counter = 1
        while current_node.next_node != None:
            counter += 1
            current_node = current_node.next_node
        return counter

    def getHead(self, head):
        return self.head

    def getEnd(self):
        return self.end

    def insertAt(self, insertion_point,
                 insertion_node):  # insertAt will insert a node +1 to the right of the insertion_point
        current_node = self.head
        flag = False
        while current_node:
            if current_node == insertion_point:
                current_node = insertion_point
                insertion_node.next_node = current_node.next_node  # first we update insertion_node's next_node to the value of insertion_point's
                # next node
                current_node.next_node = insertion_node  # then we update insertion_point's next_node value to be that of the
                # insertion_node

            current_node = current_node.next_node
        if not (flag):
            insertion_point = insertion_point.name
            print('Unable to find element ' + insertion_point)

    def iterOver(self):  # print out all entries in the list
        current_node = self.head
        while current_node:
            print(current_node,current_node.content)
            current_node = current_node.next_node


if __name__ == '__main__':
    Node1 = Node(content='This is node 1', name='Node1')
    Node2 = Node(content='This is node 2', name='Node2')
    Node4 = Node(content='this is node 4 and it will be inserted between 2 and 3', name='Node3')
    Node3 = Node(content='This is node 3 and should be the last node', name='Node4')
    LinkedList1 = Linked_List(name='list1', head=Node1, end=Node3)
    LinkedList1.append(Node1)
    LinkedList1.append(Node2)
    LinkedList1.insertAt(Node2, Node4)
    LinkedList1.append(Node3)
    # print(LinkedList1.getEnd())
    LinkedList1.iterOver()
