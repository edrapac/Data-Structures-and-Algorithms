class Node:
    """Simple node for singly-linked list"""
    def __init__(self, value, next=None):
        """Create a new node, with optional next node pointer"""
        self.value = value
        self.next = next

def stalin_sort(l):
    if l.next != None:
        if l.value > l.next.value:
            l.next = l.next.next
            stalin_sort(l)

        else:
            l = l.next
            stalin_sort(l)

#node4 = Node(value=3, next = None)
node3 = Node(value=20,next=None)
node2 = Node(value=10,next=node3)
node1 = Node(value=30,next=node2)
stalin_sort(node1)