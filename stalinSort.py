class Node:
    """Simple node for singly-linked list"""
    def __init__(self, value, next=None):
        """Create a new node, with optional next node pointer"""
        self.value = value
        self.next = next

def stalin_sort(l):
    if l.next == None:
        print(l.value)
    elif l.value > l.next.value:
        print(l.value)
        l = l.next.next
        stalin_sort(l)
    else:
        print(l.value)
        l = l.next
        stalin_sort(l)


node4 = Node(value=3, next = None)
node3 = Node(value=2,next=node4)
node2 = Node(value=1,next=node3)
node1 = Node(value=1,next=node2)
stalin_sort(node1)